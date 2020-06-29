import cv2
import numpy as np
import pytesseract


def Ocr():
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
    text=pytesseract.image_to_string(image_blur, lang='Hangul+eng')
    cv2.waitKey(0)

    capture.release()
    cv2.destroyAllWindows()

    return text

def Listing(text):
    print(text)

if __name__ == "__main__":
    ocrresult=Ocr()
    Listing(ocrresult)





