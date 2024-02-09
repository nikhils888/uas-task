import cv2
import numpy as np
# img = cv2.imread("watch.jpg",cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows
# import os
# print("Current working directory:", os.getcwd())
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1):
        break
    
    cap.release()
cv2.destroyAllWindows()
