import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)


# convert to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # gray로 바꿔주게 된다
cv.imshow('Gray',gray)


# Blur the image -> remove noise of the image
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT) # 아직은 잘 모르지만 일단은 kernel size는 무조건 홀수 -> make blur stronger by increasing the size of kernel
cv.imshow('Blur',blur)

# Edge Cascade by using 'canny edge detector'

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges',canny)

# Dilating the image -> 선 굵게 만듬

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated',dilated)

# Eroding -> 선 얇게 만듬

eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

# Resize

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# Cropping

cropped =img[50:200,200:400]
cv.imshow('Cropped',cropped)





cv.waitKey(0)