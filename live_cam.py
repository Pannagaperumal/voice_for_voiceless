import cv2
import numpy as np
# import tensorflow as tf

# Load the object detection model
# model = tf.keras.models.load_model('./Dummy_model/keras_model.h5')

# Define the classes
classes = ["Mask", "No Mask"]  # Replace with your class names

# Function to perform object detection
def detect_objects(frame):
    # input_width = 20
    # input_height=25
    # # Preprocess the frame (you may need to adjust this depending on your model)
    # frame = cv2.resize(frame, (input_width, input_height))
    # frame = frame / 255.0
    # frame = np.expand_dims(frame, axis=0)

    # Perform object detection
    # predictions = model.predict(frame)

    # Process the predictions
    # for i in range(len(predictions)):
    #     class_index = np.argmax(predictions[i])
    #     class_name = classes[class_index]
    #     confidence = predictions[i][class_index]
        confidence=0.6
    #     # Display bounding box and class label
        if confidence > 0.5:  # Adjust confidence threshold as needed
    #         # Process bounding box coordinates if available
    #         # Draw bounding box
    #         # cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    #         # Put text with class label and confidence
            class_name="Some word"
            # cv2.putText(frame, f'{class_name} {confidence:.2f}',cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f'{class_name} {confidence:.2f}',(int(0.5), int(4.6)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 255, 0))

        return frame

# Capture video from the camera
cap = cv2.VideoCapture(0)  # Use 0 for default camera, change to other numbers for other cameras

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects in the frame
    frame_with_objects = detect_objects(frame)

    # Display the frame
    cv2.imshow('Object Detection', frame_with_objects)

    # Check for key press and exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
