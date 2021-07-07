import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

    # -x --> left
    # -y --> up


translated = translate(img, 50, 50)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)

rotated_rotated = rotate(rotated, 45) # rotated로 만들어진 이미지를 다시 rotate 시킴(즉 사진의 크기에 의해 잘린 부분이 그대로 들어나게 됨)

cv.imshow('Rotated',rotated)

cv.imshow('Rotated_rotated', rotated_rotated)


# Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)

cv.imshow('Flip0',flip)

# Cropping

cropped = img[200:300,200:400]

cv.imshow('Cropping',cropped)

cv.waitKey(0)