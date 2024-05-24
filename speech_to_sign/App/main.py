
from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import io
import speech_recognition as sr
import os
import requests

from bs4 import BeautifulSoup


app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
    return app.send_static_file('index.html')


@app.route("/send_word",methods=['POST'])
def send_word():
    if request.is_json:
        # Parse the JSON data
        json_data = request.get_json()
        # Check if the 'word' key is present in the JSON data
        if 'word' in json_data:
            # Print the value associated with the 'word' key
            print(json_data['word'])
            word_to_search = json_data['word']
            link = extract_hyperlinks(word_to_search)

            print("link:",link)
            if link!="":
                response_data = {
                    "status": "Success",
                    "iframeSrc": link
                }   
            else:
                response_data = {
                    "status": "Failed",
                    "iframeSrc": "No link found"
                }
        print("response_data",response_data)

        return jsonify(response_data)
    else:
        return 'Request must contain JSON data', 400



def extract_hyperlinks(word_to_search):
    url = f"https://divyangjan.depwd.gov.in/islrtc/search.php?search={word_to_search}"

    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for invalid responses
        
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # print(soup)
        iframe_tag = soup.find('iframe')
    
        if iframe_tag:
        # Extract the src attribute from the <iframe> tag
            video_link = iframe_tag.get('src')
            print("Video Link:", video_link)

            # open_url_and_autoplay(video_link)
        # else:
        #     print("No video found on the page.")
        # # Find all <a> tags in the webpage
        # for link in soup.find_all('a'):
        #     # Get the text content of the hyperlink
        #     link_text = link.text.strip()
            
        #     # Check if the word_to_search exists in the hyperlink text
        #     if word_to_search.lower() in link_text.lower():
        #         # Extract the hyperlink URL
        #         hyperlink = link.get('href')
        #         print(f"Hyperlink for '{word_to_search}': {hyperlink}")
            return video_link
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    app.run()