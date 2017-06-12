#!/usr/bin/python

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

for i in xrange(0,10):
    _, img = cam.read()

h = np.zeros((300,256,3))

bins = np.arange(256).reshape(256,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]

for ch, col in enumerate(color):
    hist_item = cv2.calcHist([img],[ch],None,[256],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist = np.int32(np.around(hist_item))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)

h = np.flipud(h)

cv2.imshow("image", img)
cv2.imshow("hist", h)
cv2.waitKey(0)