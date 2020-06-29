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
    img_ori = cv2.imread("C:\users\82106\docudments\git_project\ocr_project\code\2.jpg")
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




    """
    listgui = Toplevel(maingui)
    listgui.title("listing")
    listgui.geometry("500x600")
    
    sb = Scrollbar(listgui)
    sb.pack(side = RIGHT, fill = Y)
    lbl = Label(listgui,text = "저장할 리스트")
    ls = Listbox(listgui,yscrollcommand = sb.set)
    
    ls.insert(1,"newlist")
    ls.insert(2,"newlist")
    ls.insert(3,"newlist")
    ls.insert(4,"newlist")
    ls.insert(5,"newlist")
    ls.insert(6,"newlist")
    ls.insert(7,"newlist")
    ls.insert(8,"newlist8")
    ls.insert(9,"newlist9")
    ls.insert(10,"newlist10")
    ls.insert(11,"newlist11")
    ls.insert(12,"newlist")
    ls.insert(13,"newlist")
    ls.insert(14,"newlist")
    
    lbl.pack()
    ls.pack(side = LEFT)
    sb.config(command = ls.yview)
    
    
    listbut3 = Button(listgui, text="삭제",command = lambda ls=ls: ls.delete(ANCHOR))
    
    listbut3.pack()

    
    newlist = capturing()
    n = 0
    for x in newlist:
        ls.insert(n,x)
        n = n+1
    listbut2 = Button(listgui,text="저장",command=savefile,activebackground="orange")

    
    """

    
but1 = Button(maingui,text="Capture",command=capturing,activebackground="orange")
but2 = Button(maingui,text="List",command=listing,activebackground="orange")
but1.pack()
but2.pack()

maingui.mainloop()

