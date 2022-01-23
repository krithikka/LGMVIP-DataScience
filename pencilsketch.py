# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:15:54 2022

@author: krithikka
"""
#%%
import cv2
img=cv2.imread('picture.jpg')
greyimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(greyimg)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(greyimg, invertedblur, scale=256.0)
cv2.imwrite("Pencilsketch.png", sketch)
cv2.imshow("original picture",img)
cv2.imshow("pencil sketch",sketch)
cv2.waitKey(0)