import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
#Kindly install all these library before run.
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        D=obj.data
        D=str(D)
        
        D=list(D)
        del D[0]
        del D[0]
        del D[-1]
        
        D="".join(D)
        print(D)
        

    cv2.imshow("QR SCAN", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
