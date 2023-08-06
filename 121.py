import cv2
import numpy as np

camera = cv2.VideoCapture(0)

color_lower = (29, 86, 6)
color_upper = (64, 255, 255)

while True:
    (grabbed, frame) = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, color_lower, color_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(frame, frame, mask=mask)

    img2_fg = cv2.bitwise_and(frame, frame, mask=mask_inv)

    output = cv2.addWeighted(img1_bg, 0.3, img2_fg, 0.7, 0)

    cv2.imshow("Invisibility Cloak", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()