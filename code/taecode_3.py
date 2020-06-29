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
    #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img_ori = cv2.imread("2.jpg")
    image_gray=cv2.cvtColor(img_ori,cv2.COLOR_BGR2GRAY)
    image_blurred=cv2.GaussianBlur(image_gray,(5,5),0)
    image_blurred = cv2.medianBlur(image_blurred, 5)
    text=pytesseract.image_to_string(image_blurred, lang='kor')

    return text

def listing():
    listgui = Toplevel(maingui)
    listgui.title("listing")
    listgui.geometry("500x600")
    
    lbl = Label(listgui,text = "저장할 리스트")
    ls = Listbox(listgui)
        
    lbl.pack()
    ls.pack()
    listbut3 = Button(listgui, text="삭제",command = lambda ls=ls: ls.delete(ANCHOR))
        
    listbut3.pack()

    newlist=capturing()

    size_table = re.split('\n',newlist)
    size = [s for s in size_table]

    n=0
    for x in size:
        ls.insert(n,x)
        n=n+1


but1 = Button(maingui,text="Capture",command=capturing,activebackground="orange")
but2 = Button(maingui,text="List",command=listing,activebackground="orange")
but1.pack()
but2.pack()

maingui.mainloop()

