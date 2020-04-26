import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('th.jpg',0)
img2 =cv2.imread('th.jpg')
#img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY_INV)
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thresh1 = cv2.cvtColor(thresh1,cv2.COLOR_BGR2GRAY)
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# hull =[cv2.convexHull(c) for c in contours]
# final= cv2.drawContours(img2,hull,-1,(0,255,0),2)
area =0
for contour in contours:
    if area<cv2.contourArea(contour):
        area=cv2.contourArea(contour)
        cv2.drawContours(img2, contour, -1, (0, 255, 0), 2)



# cv2.imshow("frame",img2)
# cv2.imshow("frame2",thresh1)
cv2.imwrite("target.png", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()