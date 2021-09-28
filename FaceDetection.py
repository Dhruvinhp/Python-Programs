import cv2
import sys
import cmake

faceCascade = cv2.CascadeClassifier("default.xml")
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 5, min(20,20))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 9), 2)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
"""
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img= cv2.imread(r'C:\Users\HP\Pictures\Vrunda\passportphoto-min.jpg')
img= cv2.resize(img,(500,500))
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
faces=face_cascade.detectMultiScale(gray,1,4)
for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('image',img)
cv2.waitKey()
"""