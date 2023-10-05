import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87, 11], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    kernel = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(frame, frame, mask=red_mask)

    blue_mask = cv2.dilate(blue_mask, kernel)
    blue_red = cv2.bitwise_and(frame, frame, mask=red_mask)

    green_mask = cv2.dilate(green_mask, kernel)
    green_red = cv2.bitwise_and(frame, frame, mask=red_mask)

    contours, hierarchy = cv2.findContours(
        red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 800):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))
            cv2.putText(frame, "Rojo", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

    contours, hierarchy = cv2.findContours(
        blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 800):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))
            cv2.putText(frame, "Azul", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

    contours, hierarchy = cv2.findContours(
        green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 800):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
            cv2.putText(frame, "Verde", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    cv2.imshow('frame', frame)

    if cv2.waitKey(2) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
