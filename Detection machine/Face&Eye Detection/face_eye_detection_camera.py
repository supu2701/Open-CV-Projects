import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detectFaceEye(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(imgGray, 1.1, 4)
    for fx, fy, fw, fh in faces:
        cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2)
        roi_gray = imgGray[fy : fy + fh, fx : fx + fw]
        roi_color = img[fy : fy + fh, fx : fx + fw]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    while True:
        ret, img = cap.read()
        detectFaceEye(img)
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()