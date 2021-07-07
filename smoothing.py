import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

# 기존까지 gaussianblurring을 사용하였지만 때로는 작동을 하지 않는 경우도 존재한다

# blur을 할 때 작동되는것
# kernel 사이즈를 잡아서 사진에 칸이 잡힌다.

# Averaging: 가운데에 있는 픽셀은 나머지 픽셀들의 평균으로 잡히게 된다
average = cv.blur(img, (3,3))

cv.imshow('Average Blur',average)


# Gaussian Blur --> kernel로 잡힌 사이즈에 각 픽셀에 weight 값을 설정해주게 된다 (less blur)
gauss = cv.GaussianBlur(img,(3,3), 0) # blur과 다르게 세번째 인자는 standard deviation이라는 것
cv.imshow('Gaussian',gauss)


# median Blur --> median 값을 찾는다?? gaussian보다 blur이 더 적게 형성된다 -> noise를 줄일 수 있다
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)


#Bilateral Blur -> retain edges

bilateral = cv.bilateralFilter(img, 10, 15, 15) # sigma space를 크게 잡으면 굉장히 멀리있는 픽셀도 계산되는 픽셀에 영향을 미칠 수 있다. -> 성능이 제일 좋음
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)