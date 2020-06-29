import cv2
import pytesseract
#import matplotlib.pyplot as plt
import re
from tkinter import *
import os

maingui = Tk()
maingui.title("OCR 프로그램")
maingui.geometry("500x300")

def capturing():
    global text

    width=640 #길이
    height=480 # 높이

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
                break #q를 누르면 비디오 종료 및 캡쳐
            elif cv2.contourArea(pts)>width*height*0.9:
                break
        else:
            break

    src=frame
    image_gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY) #그레이 
    image_blur=cv2.GaussianBlur(image_gray,(5,5),0) #그레이 + 블러
    cv2.imshow("image",image_blur) #이미지 보기
    cv2.imwrite(r'C:\Users\82107\Desktop\file\project.jpg',image_blur) #filename modify
    print(pytesseract.image_to_string(image_blur ,lang='kor'))
    text = pytesseract.image_to_string(image_blur, lang='kor')


def deleting():
    global newlist
    selection = ls.curselection()
    if(len(selection) == 0):
        return

    value = ls.get(selection[0])
    ind = size.index(value)
    del size[ind]
    ls.delete(selection[0])

def saving():
    global newlist2
    newlist2 = newlist
    
          
def listing():
    global ls
    global size
    listgui = Toplevel(maingui)
    listgui.title("listing")
    listgui.geometry("500x600")
    
    sb = Scrollbar(listgui)
    sb.pack(side = RIGHT, fill = Y)
    lbl = Label(listgui,text = "저장할 리스트")
    ls = Listbox(listgui, yscrollcommand = sb.set)
    
    size_table=re.split('\n',text)
    size=[s for s in size_table]
    
    n=0
    for x in size:
        ls.insert(n,x)
        n=n+1
     
    lbl.pack()
    ls.pack()
    sb.config(command = ls.yview)
    
    listbut1 = Button(listgui, text="삭제",command=deleting)
    listbut1.pack()

    listbut2 = Button(listgui, text="저장",command=saving)
    listbut2.pack()

    return ls

def Finallist():
    listsave = Toplevel(maingui)
    listsave.title("Final Save List")
    listsave.geometry("500x600")
    
    sb = Scrollbar(listsave)
    sb.pack(side = RIGHT, fill = Y)
    lbl = Label(listsave ,text = "최종 저장 목록")
    ds = Listbox(listsave , yscrollcommand = sb.set)
    n = 0
    newlist = [0]
    
    for x in newlist2:
        ds.insert(n,x)
        newlist += size
        n+=1
     
    lbl.pack()
    ds.pack()
    sb.config(command = ls.yview)
    

    
but1 = Button(maingui,text="Capture",command=capturing)
but2 = Button(maingui ,text="최근촬영 List",command=listing)
but3 = Button(maingui, text="최종저장목록", command=Finallist)

but1.pack()
but2.pack()
but3.pack()


maingui.mainloop()
