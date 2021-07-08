import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # threshold에는 150이, thresh에는 threshold를 가한 이미지 행렬이 전달된다
cv.imshow('Simple Threshold', thresh)


threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # threshold에는 150이, thresh에는 threshold를 가한 이미지 행렬이 전달된다
cv.imshow('Simple Threshold Inverse', thresh_inv)


# Adaptive Thresholding ---> 이상적인 threshold를 찾아서 thresholding을 하게 된다
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9) # ADAPTIVE_THRESH_MEAN_C 대신 ADAPTIVE_THRESH_GAUSSIAN_C를 사용하게 되면 더욱 섬세하게 사진을 찾아낼 수 있다
cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)