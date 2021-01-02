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
