import cv2
import numpy as np

class Color:
    def __init__(self,frame,range_lower,range_upper,rgb,text,area):
        self.frame = frame
        self.hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        self.range_lower = np.array(range_lower, np.uint8)
        self.range_upper = np.array(range_upper, np.uint8)
        self.color_mask = cv2.inRange(self.hsvFrame, self.range_lower, self.range_upper)
        self.kernel = np.ones((5,5), "uint8")
        self.rgb = rgb
        self.text = text
        self.area = area

    def detect(self):
        self.color_mask = cv2.dilate(self.color_mask, self.kernel)
        res_color = cv2.bitwise_and(self.frame, self.frame, mask=self.color_mask)
        contours, hierarchy = cv2.findContours(self.color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 300):
                x,y,w,h = cv2.boundingRect(contour)
                self.frame = cv2.rectangle(self.frame, (x,y), (x+w, y+h), self.rgb,2)
                cv2.putText(self.frame, self.text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, self.rgb)
