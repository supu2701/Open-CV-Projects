import sys
print(sys.executable)
# /Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

import cv2
import numpy as np

# Create our body classifier
body_classifier = cv2.CascadeClassifier('../../Haarcascades/haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('../../images/walking.avi')

# Loop once video is successfully loaded
while cap.isOpened():

    # Read first frame
    
    # Write code here
    
    
    
    
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()
