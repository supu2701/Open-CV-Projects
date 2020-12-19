import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
# Write the while loop code here
        #break
while True:
	success,img = cap.read()
	faces = detector.detectMultiScale(img,1.1,4)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
	cv2.imshow("Cam Face detector",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()