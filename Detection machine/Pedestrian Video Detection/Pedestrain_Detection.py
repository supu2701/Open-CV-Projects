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



Actual Solution code
import cv2
import imutils

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Reading the Image
image = cv2.imread('img.png')

# Resizing the Image
image = imutils.resize(image,
					width=min(400, image.shape[1]))

# Detecting all the regions in the
# Image that has a pedestrians inside it
(regions, _) = hog.detectMultiScale(image,
									winStride=(4, 4),
									padding=(4, 4),
									scale=1.05)

# Drawing the regions in the Image
for (x, y, w, h) in regions:
	cv2.rectangle(image, (x, y),
				(x + w, y + h),
				(0, 0, 255), 2)

# Showing the output Image
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()

