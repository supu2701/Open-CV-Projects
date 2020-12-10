import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# Write the while loop code here
        #break

cap.release()
cv2.destroyAllWindows()