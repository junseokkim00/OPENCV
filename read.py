import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg') # 다음 사진을 행렬로 표현하게 된다

# cv.imshow('Cat', img) # 해당 행렬에 관련된 사진을 보여주게 된다.

# reading Videos
capture = cv.VideoCapture('Videos/dog.mp4') # 0,1,2,3 과 같은 int형 수치는 컴퓨터에 내장되어 있는 카메라를 의미하게 된다

while True:
    isTrue, frame = capture.read() # frame의 수치와 frame이 제대로 잘 읽혔는지를 구해준다
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destoryAllWindows() 


#cv.waitKey(0) #다음 키가 누를 때까지 기다린다