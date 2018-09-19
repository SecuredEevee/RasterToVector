import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('test 01.tif')
(h, w )= img.shape[:2]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
edged = cv2.Canny(hsv, 100, 200)
image, contours, hierachy = cv2.findContours(edged,  cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
idx = 0
for c in contours:
    plt.plot(c[:,0, 0], h- c[:,0, 1], linewidth=2)
plt.axis('off')
#plt.show()
plt.savefig("test1.svg", format="svg")