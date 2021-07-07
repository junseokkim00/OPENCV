import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2],dtype='uint8')


# split color channels

b, g, r = cv.split(img)

cv.imshow('Blue',b) # 검은색에 가까울수록 그 부분에 그 색상이 존재하지 않는다
cv.imshow('Green',g)
cv.imshow('Red',r)




blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('new Blue',blue)
cv.imshow('new Green',green)
cv.imshow('new Red',red)

print(img.shape) # height, width, color
print(b.shape) 
print(g.shape)
print(r.shape)


merged = cv.merge([b,g,r]) # 순서가 무조건 b,g,r이어야함
cv.imshow('Merged image',merged)


cv.waitKey(0)