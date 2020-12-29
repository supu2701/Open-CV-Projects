import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detectFaceEye(img):
     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(imgGray, 1.3, 1)
     for fx, fy, fw, fh in faces:
          cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2)
          roi_gray = imgGray[fy : fy + fh, fx : fx + fw]
          roi_color = img[fy : fy + fh, fx : fx + fw]
          eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 0, minSize=(25, 25), maxSize=(30, 30))
          for ex, ey, ew, eh in eyes:
               cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

if __name__ == "__main__":
     img = cv2.imread('modi.jpg')
     detectFaceEye(img)
     cv2.imshow('Image',img)
     cv2.waitKey(0)
     cv2.destroyAllWindows()