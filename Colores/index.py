import cv2
import numpy as np
from Color import Color

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    red = Color(frame, [136, 87, 11], [180,255,255],(0,0,255),"Rojo",800)
    red.detect()

    cv2.imshow("dom", frame)

    if cv2.waitKey(1) == ord("d"):
        break

cap.release()
cap.destroyAllWindows()