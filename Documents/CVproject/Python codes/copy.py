# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 17:02:36 2017

@author: dell
"""

import cv2
import numpy as np

img_rgb = cv2.imread('Scan10008.jpg')



ratio=1000.0/img_rgb.shape[0]
dimension=(540,int(ratio*img_rgb.shape[1]))

img_rgb=cv2.resize(img_rgb,dimension,interpolation=cv2.INTER_AREA)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
print img_gray.shape
template = cv2.imread('template1.jpg',0)
w, h = template.shape[::-1]
print template.shape
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 0)
    print pt
cv2.imshow('Detected',img_rgb)

cv2.waitKey(0)