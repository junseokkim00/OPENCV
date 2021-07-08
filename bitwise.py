import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)


# bitwise AND ---> intersecting region

bitwise_and = cv.bitwise_and(rectangle,circle) # 교집합을 구하게 됨
cv.imshow('Bitwise_AND',bitwise_and)

# bitwise OR ---> non intersecting and intersecting regions

bitwise_or = cv.bitwise_or(rectangle,circle) # 합집합을 구하게 된다
cv.imshow('Bitwise_OR', bitwise_or)

# bitwise XOR ---> non intersecting regions

bitwise_xor = cv.bitwise_xor(rectangle,circle) # 두 영역을 합쳤을 때 한 영역만 존재하는 곳을 선택, 두 영역을 모두 가지고 있는 영역은 삭제
cv.imshow('Bitwise_XOR',bitwise_xor)

# bitwise NOT --->

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise_NOT',bitwise_not)

cv.waitKey(0)