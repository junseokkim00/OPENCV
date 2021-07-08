# Learning OpenCV

URL: https://www.youtube.com/watch?v=oXlwWbU8l2o&t=3429s

## introduction

    유튜브를 통해서 Python에서 제공하는 OpenCV를 배운 내용을 정리할 것이다.


    ```
    * 매일매일 정리할 것
    * 매일마다 소단원 하나씩은 공부하기
    * git에서 올리는거 까먹지 않기

    ```
    이제 나만 열심히 하면 된다. 화이릥~ 🙃

## 2021/07/08

## **contour detection**

    contour은 일종의 모서리라고 생각하면 된다. 그래서 이 영상에서는 contour을 어떻게 찾게 되는지에 대해서 주요적으로 다루고 있다.

    모서리의 개수가 이미지에 어떤 변화를 주냐에 따라 달라지기 때문에 grayscale과 blur을 시킨 것을 가지고 비교해볼 것이다.

**첫번째 Canny**

    > cv2.Canny("사용하려는 이미지 행렬값", 최소 threshold, 최대 threshold)

    canny를 사용하게 되면 두 가지의 threshold를 잡아주게 된다. 
    min threshold는 maxthreshold보다는 작고 min threshold보다 높은 픽셀에 대해서 작동을 하게 되며 이때는 약한 edge를 구현하게 된다. 
    max threshold는 픽셀 값 중 max threshold가 이 값을 넘게 되면 강한 edge를 구현하게 된다.

**두번째 threshold**

     > ret, thresh = cv.threshold("판단하려는 이미지 행렬값",threshold, 바뀌는 값, 바꾸는 형태)


    - 최소 threshold를 넘으면 그 픽셀은 바뀌는 값으로 바뀜, 넘지 못하면 0
    - 바꾸는 형태는 대표적으로 binary 형태가 있음
    - 바뀐 행렬을 thresh에 저장
    _- ret은 아직은 모름_


**cv2.findContours & cv2.drawContours **

    > contours, hierarchies = cv2.findContours( "행렬값" , 읽어들일 행렬 형태 , 처리 형태 )

    - 읽어들일 행렬 형태로는 RETR_LIST, RETR_TREE, RETR_EXTERNAL이 존재
    - 처리 형태로는  CHAIN_APPROX_NONE, CHAIN_APPROX_SIMPLE이 존재함
    - 읽어들인 행렬은 contours에 저장
    - 새로운 행렬을 읽어들이면서 생긴 hierachy 정보는 hierarchies에 저장

    > cv2.drawContours(행렬값, 그릴 행렬값, 범위, 색상, 굵기)
    - 범위를 -1로 잡으면 전부 잡힘




## **color spaces**

    총 5 가지 방식이 존재함
    - bgr: opencv에서 다룰 때 가장 기본적인 팔레트
    - gray: 모든 값이 회색으로 표현됨
    - hsv: 
    - lab: l*a+b
    - rgb: 사람들이 사용하는 양식

    cv2.cvtcolor을 이용해서 color spaces를 변환할 수 있음(물론 몇 가지 종류는 바로 가능하지는 않음)

    ex) cv2.cvtcolor(img, cv.COLOR_BGR2GRAY): img를 bgr에서 grayscale로 바꾼다는 의미

## **color channel**

모든 이미지는 blue green red를 가지고 있음

**cv2.split**

    > b, g, r = cv.split(img)

    cv2.split을 이용하여 사진의 bgr를 나눌 수 있음

    cv2.imshow를 하게 되었을 때 각 사진은 회색으로 나오게 됨

    split을 통해 얻은 각 이미지 행렬을 살펴보면 기존 사진과 다른 점은 shape 배열의 원소 개수이다.

    기존 img의 원소: (높이, 너비, 색상개수)

    각 color channel의 원소: (높이, 너비)

    이유는 각 color channel 행렬은 하나의 색상이므로 세번째 원소가 1이지만 생략된 것이다.

**cv2.merge**

    cv2.merge를 통해 합칠 수 있다. merge 함수에서는 배열을 파라미터로 받으며 꼭 행렬이 세가지여야한다.

    > merged = cv.merge([b,g,r])

    이때 무조건 행렬의 합성 순서는 blue, green, red여야한다.



## **Blurring**



## 2021/07/08

## **BITWISE operations**

    bitwise 연산자에는 총 4 가지 연산자가 존재한다
    - AND: 교집합을 구하게 된다
    - OR: 합집합을 구하게 된다
    - XOR: 합집합 - 교집합
    - NOT: 선택되지 않은 영역을 선택

    이 연산자들은 다음 범위인 masking에서 사용될 것이다.
