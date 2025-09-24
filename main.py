# webcam
import cv2
cap=cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 720)
while True:
    success,img=cap.read()
    cv2.imshow("face attendence",img)
    cv2.waitKey(1)
  
  