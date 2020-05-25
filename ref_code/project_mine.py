import sys
import numpy as np
import cv2

src=cv2.imread("namecard1.jpg") #사진 가져오기

if src is None:
    print('image load failed')
    sys.exit() #사진이 안가져와 졌다면 종료

src=cv2.resize(src,(0,0),fx=0.5,fy=0.5) #크기 조절(노트북 화면이 작아 한번에 보기 위해 실행함)

src_gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) #그레이스케일로 변환

_,src_bin=cv2.threshold(src_gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU) #그레이스케일된 이미지 이진화 <= otsu알고리즘으로 threshold 설정

contours,_=cv2.findContours(src_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#외곽선 검출: 모드-기본, 메소드-가장 바깥쪽 외곽선
#contours=외곽선이 검출된 객체의 개수
#객체 하나의 외곽선 표현 방법
#==> numpy.ndarray ->shape=(K,1,2), dtype=int32(K는 외곽선 좌표 개수)

for pts in contours:
    if cv2.contourArea(pts)<1000:
        continue #객체의 크기가 1000픽셀 이하면 무시

    approx=cv2.approxPolyDP(pts,cv2.arcLength(pts,True)*0.02,True)
    #Ramer-Douglas-Peucker Algorithm을 이용해 꼭짓점 검출
    #margin값에 0.02를 곱해준다
    
    if len(approx) !=4:
        continue #검출된 꼭짓점이 4개가 아니면 무시(영수증은 사각형이므로)


    w,h=900,500
    srcQuad=np.array([[approx[0,0,:]],[approx[1,0,:]],
                      [approx[2,0,:]],[approx[3,0,:]]]).astype(np.float32)
    dstQuad=np.array([[0,h],[w,h],[w,0],[0,0]]).astype(np.float32)
    pers=cv2.getPerspectiveTransform(srcQuad,dstQuad)
    dst=cv2.warpPerspective(src,pers,(w,h))


    cv2.polylines(src,pts,True,(0,0,255))
 
cv2.imshow('src',src)
cv2.imshow('src_gray',src_gray)
cv2.imshow('src_bin',src_bin)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()