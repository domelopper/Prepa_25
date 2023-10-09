import cv2
import numpy as np
import pytesseract

cap = cv2.VideoCapture(0)

font_scale = 1.5
font = cv2.FONT_HERSHEY_SIMPLEX
counter = 0


while True:
    ret,frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(cv2.medianBlur(img,3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    if((counter%20)==0):
        imgH, imgW,_ = frame.shape
        x1,y1,w1,h1 = 0,0,imgH,imgW
        
        imgchar = pytesseract.image_to_string(img)
        img_boxes = pytesseract.image_to_boxes(img)
        print(imgchar)

        for boxes in img_boxes.splitlines():
            boxes = boxes.split(" ")
            x,y,w,h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(frame,(x,imgH-y), (w,imgH-h), (0,0,255), 3)

        cv2.putText(img,imgchar, (x1 + int(w1/50), y1 + int(h1/50)), font, font_scale, (0,0,255))

    cv2.imshow("frame", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows