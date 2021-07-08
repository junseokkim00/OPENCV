import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')


# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Circle',circle)

mask = cv.bitwise_and(img,img,mask=circle)

cv.imshow('Mask',mask)

# Grayscale histogram을 만들어보자
# gray_hist = cv.calcHist([gray],[0], mask, [256], [0,256]) # 조금만 더 제대로 알아봐야할듯

# print(len(gray_hist))

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins') # pixel intensity
# plt.ylabel('# of pixels') # pixel numbers
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()



# Color Histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins') # pixel intensity
plt.ylabel('# of pixels') # pixel numbers
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    print(i)
    print(col)
    hist = cv.calcHist([img],[i], circle, [256],[0,256]) # bitwise 시킨 것을 mask로 옮기면 안됨 (색상채널의 개수 차이로 에러 발생)
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)