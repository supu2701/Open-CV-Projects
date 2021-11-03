import sys
print(sys.executable)
# from moviepy.editor import VideoFileClip
# Import everything needed to edit/save/watch video clips
# from moviepy.editor import VideoFileClip
from IPython.display import HTML

import cv2
import time
import numpy as np

# Create our body classifier
car_classifier = cv2.CascadeClassifier('../../Haarcascades/haarcascade_car.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('../../images/cars.avi')


# Loop once video is successfully loaded
# Add code here


    # Read first frame
    #ret, frame = cap.read()
    # Complete the code here
    
    
    
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    
    # Extract bounding boxes for any bodies identified
    # Write code for for loop here
    
    
#         cv2.imshow('Cars', frame)
        #fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        #out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()






Solution:
    
    # OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
cap = cv2.VideoCapture('video.avi')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

# loop runs if capturing has been initialized.
while True:
	# reads frames from a video
	ret, frames = cap.read()
	
	# convert to gray scale of each frames
	gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
	

	# Detects cars of different sizes in the input image
	cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	
	# To draw a rectangle in each cars
	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

# Display frames in a window
cv2.imshow('video2', frames)
	
	# Wait for Esc key to stop
	if cv2.waitKey(33) == 27:
		break

# De-allocate any associated memory usage
cv2.destroyAllWindows()

