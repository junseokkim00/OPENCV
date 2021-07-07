import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray,125 , 255, cv.THRESH_BINARY) # threshold는 이미지를 binary하게 만든다. 행렬값중 원소가 125보다 작으면 0으로, 125보다 크면 255로 만든다 -> thresh에 변경된 행렬이 저장됨

cv.imshow('Thresh',thresh)


contours, hierarchies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 255, 255),1)
cv.imshow('Contours drawn',blank)




cv.waitKey(0)