import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5" , "Model/labels.txt")
offset = 20
imgSize = 300
counter = 0

labels = ["Hello","I love you","No","Okay","Please","Thank you","Yes"]

print("i came")
while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

        imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap: wCal + wGap] = imgResize
            prediction , index = classifier.getPrediction(imgWhite, draw= False)
            print(prediction, index)

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap: hCal + hGap, :] = imgResize
            prediction , index = classifier.getPrediction(imgWhite, draw= False)

       
        cv2.rectangle(imgOutput,(x-offset,y-offset-70),(x -offset+400, y - offset+60-50),(0,255,0),cv2.FILLED)  

        cv2.putText(imgOutput,labels[index],(x,y-30),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),2) 
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x + w + offset, y+h + offset),(0,255,0),4)   

        cv2.imshow('ImageCrop', imgCrop)
        cv2.imshow('ImageWhite', imgWhite)

    cv2.imshow('Image', imgOutput)
    cv2.waitKey(1)
# import cv2

# # Load your object detection model here
# # Example:
# # model = ...

# # Function to perform object detection on each frame
# def detect_objects(frame):
#     # Perform object detection using your model here
#     # Example:
#     # detected_objects = model.detect_objects(frame)
    
#     # Placeholder for detected objects
#     # Replace this with your actual detection results
#     detected_objects = [(100, 100, 200, 200)]  # Example bounding box (x_min, y_min, x_max, y_max)
    
#     # Draw bounding boxes on the frame
#     for (x_min, y_min, x_max, y_max) in detected_objects:
#         cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

#     return frame

# # Main function to capture video from the webcam
# def main():
#     # Open webcam
#     cap = cv2.VideoCapture(0)

#     # Check if the webcam is opened correctly
#     if not cap.isOpened():
#         print("Error: Could not open webcam")
#         return

#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         if not ret:
#             print("Error: Failed to capture frame")
#             break

#         # Perform object detection
#         detected_frame = detect_objects(frame)

#         # Display the resulting frame
#         cv2.imshow('Object Detection', detected_frame)

#         # Press 'q' to exit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the capture
#     cap.release()
#     cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
