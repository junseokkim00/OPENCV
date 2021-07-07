import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame, scale=0.75):
    # work for image, video and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('Image',resized_image)


def changeRes(width, height):
    # ONLY USED FOR eh live video
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture('Videos/dog.mp4') # 0,1,2,3 과 같은 int형 수치는 컴퓨터에 내장되어 있는 카메라를 의미하게 된다

while True:
    isTrue, frame = capture.read() # frame의 수치와 frame이 제대로 잘 읽혔는지를 구해준다

    frame_resized = rescaleFrame(frame)


    cv.imshow('Video', frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destoryAllWindows() 