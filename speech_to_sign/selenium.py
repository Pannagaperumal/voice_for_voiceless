# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# def extract_hyperlink(word_to_search, url):
#     # Set up the Chrome webdriver
#     service = Service('/path/to/chromedriver')  # Path to chromedriver executable
#     driver = webdriver.Chrome(service=service)

#     # Open the webpage
#     driver.get(url)

#     # Find the search bar and input the word to search
# p= extract_hyperlink("Hello","https://indiansignlanguage.org/")
# print(p)
import webbrowser

import requests
from bs4 import BeautifulSoup

from detect_voice import speech_to_text

def open_url_and_autoplay(url):
    # Append '?autoplay=1' to the URL
    url_with_autoplay = url + "?autoplay=1"
    
    # Open the URL in the default web browser
    webbrowser.open(url_with_autoplay)


def extract_hyperlinks(word_to_search, url):
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

            open_url_and_autoplay(video_link)
        else:
            print("No video found on the page.")
        # Find all <a> tags in the webpage
        for link in soup.find_all('a'):
            # Get the text content of the hyperlink
            link_text = link.text.strip()
            
            # Check if the word_to_search exists in the hyperlink text
            if word_to_search.lower() in link_text.lower():
                # Extract the hyperlink URL
                hyperlink = link.get('href')
                print(f"Hyperlink for '{word_to_search}': {hyperlink}")
    
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # word_to_search = input("Enter the word to search: ")
    word_to_search=speech_to_text()
    url = f"https://divyangjan.depwd.gov.in/islrtc/search.php?search={word_to_search}"

    if word_to_search != None:
        extract_hyperlinks(word_to_search, url)
    else:
        print("no word detected")
