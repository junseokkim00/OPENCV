import cv2 as cv
import numpy as np

# making a dummy image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)


# paint the image a certain color
# blank[200:300,300:400] = 0,0,255 
# cv.imshow('Green',blank)

# draw a rectangle

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.rectangle(blank, (200,200), (blank.shape[1],blank.shape[0]), (255,255,0), thickness=cv.FILLED) # cv.FILLED 또는 -1을 입력하게 되면 안이 채워져 있는 직사각혀잉 그려진다

cv.imshow('Rect',blank)


# draw a circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 50, (255,0,255), thickness=-1)
cv.imshow('Circle',blank)

# draw a line

cv.line(blank, (0,0), (blank.shape[1],blank.shape[0]), (0,0,255), thickness = 3)
cv.imshow('Line',blank)


# add text
cv.putText(blank, 'Hello World', (255,255), cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255), 2)
cv.imshow('Add Text',blank)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat',img)

cv.waitKey(0)