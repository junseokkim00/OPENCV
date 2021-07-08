import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)


blank = np.zeros(img.shape[:2],dtype='uint8') # mask를 만드는 행렬값은 반드시 적용시킬 사진과 같은 크기여야한다.
cv.imshow('Blank',blank)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

cv.imshow('Mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)


cv.waitKey(0)