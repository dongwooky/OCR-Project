import cv2
import numpy as np
from PIL import Image
import pytesseract
import re
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
import os

svl=[]
size=[]
olv=[] #ocr_list_value
ls=None


def ocr():
    width=640
    height=480

    capture=cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

    ret=0
    text=''


    while True:
        ret,frame=capture.read()
        if ret==True:

            cv2.imshow("VideoFrame",frame)
            if cv2.waitKey(33)==ord('q'):
                break
        else:
            break
        
    if ret is True:
        src=frame
        image_gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
        image_blur=cv2.GaussianBlur(image_gray,(5,5),0)
        text=pytesseract.image_to_string(image_blur, lang='Hangul+eng')
    
    cv2.waitKey(0)

    capture.release()
    cv2.destroyAllWindows()

    global olv
    del olv[:]
    olv=noize_removal(text)

    return olv

def noize_removal(source):
    p=re.compile("([가-힣]+)")
    size_table=p.findall(source)
    global size
    for i in range(len(size_table)):
        if ((len(size_table[i])>2)):
            size.append(size_table[i])

    return size

def deleting():
    global size
    selection=ls.curselection()
    if(len(selection)==0):
        return
    
    value=ls.get(selection[0])
    ind=size.index(value)
    del size[ind]
    ls.delete(selection[0])

def saving(size):
    global svl
    src=size
    svl.extend(size)



def gui():
    maingui=Tk()
    maingui.title("OCR 프로그램")
    maingui.geometry("500x300")

    global olv
    
    but1=Button(maingui, text="Capture",command=ocr)
    but1.pack()
    but2=Button(maingui, text="최근 촬영 List",command=lambda:listing(olv))
    but2.pack()
    but3=Button(maingui, text="최종저장목록",command=finallist)
    but3.pack()
    
    maingui.mainloop()

    
def listing(source):
    maingui=tk.Toplevel()
    listgui=tk.Label(maingui, text='listing')
    listgui.pack()

    sb = Scrollbar(listgui)
    sb.pack(side = RIGHT, fill = Y)
    lbl = Label(listgui,text = "저장할 리스트")
    global ls
    ls = Listbox(listgui,height=30,width=40,yscrollcommand = sb.set)
    
    size=source
    
    n=0
    for x in size:
        ls.insert(n,x)
        n=n+1
   
    lbl.pack()
    ls.pack()
    sb.config(command = ls.yview)

    listbut1=Button(listgui, text="삭제",command=deleting)
    listbut1.pack()

    listbut2=Button(listgui, text="저장",command=lambda:saving(size))
    listbut2.pack()

def finallist():
    maingui=tk.Toplevel()
    fl_gui=tk.Label(maingui, text='fianllist')
    fl_gui.pack()

    sb = Scrollbar(fl_gui)
    sb.pack(side = RIGHT, fill = Y)
    lbl = Label(fl_gui,text = "최종 저장 목록")
    ls = Listbox(fl_gui,height=30,width=40,yscrollcommand = sb.set)
    
    global svl
    size=svl
    
    n=0
    for x in size:
        ls.insert(n,x)
        n=n+1
   
    lbl.pack()
    ls.pack()
    sb.config(command = ls.yview)

if __name__ == '__main__':
    gui()
