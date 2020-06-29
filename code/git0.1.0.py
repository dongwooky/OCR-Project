"""
tesseract-ocr 설치
1) https://github.com/UB-Mannheim/tesseract/wiki 에서 exe 파일 다운로드
2) 설치 시 "Additional script data" 항목에서 "Hangul Script", "Hangul vertical script" 항목 체크,
   "Additional language data" 항목에서 "Korean" 항목 체크.
3) 설치 후 시스템 환경변수 PATH에 Tesseract 설치 폴더 추가
   (e.g.) c:\Program Files\Tesseract-OCR
4) 설치 후 시스템 환경변수에 TESSDATA_PREFIX를 추가하고, 변수 값을 <Tesseract-DIR>\tessdata 로 설정
5) <Tesseract-DIR>\tessdata\script\ 폴더에 있는 Hangul.traineddata, Hangul_vert.traineddata 파일을
   <Tesseract-DIR>\tessdata\ 폴더로 복사
6) 명령 프롬프트 창에서 pip install pytesseract 명령 입력
"""

import cv2
import numpy as np
import pytesseract

width=640
height=480

capture=cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


while True:
    ret,frame=capture.read()
    if ret==True:
        frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        _,frame_bin=cv2.threshold(frame_gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        contours,_=cv2.findContours(frame_bin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        for pts in contours:
            if cv2.contourArea(pts)<1000:
                continue

            approx=cv2.approxPolyDP(pts,cv2.arcLength(pts,True)*0.02,True)

            if len(approx) !=4:
                continue

            cv2.polylines(frame,pts,True,(0,0,255),thickness=1)

        cv2.imshow("VideoFrame",frame)
        if cv2.waitKey(33)==ord('q'):
            break
        elif cv2.contourArea(pts)>width*height*0.9:
            break
    else:
        break

src=frame
image_gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
image_blur=cv2.GaussianBlur(image_gray,(5,5),0)
#cv2.imshow("image",image_blur)
print(pytesseract.image_to_string(image_blur, lang='Hangul+eng'))
cv2.waitKey(0)

capture.release()
cv2.destroyAllWindows()