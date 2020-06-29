import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
from tkinter import *
import os

maingui = Tk()
maingui.title("OCR 프로그램")
maingui.geometry("500x300")

def capturing():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img_ori = cv2.imread("2.jpg")
    image_gray=cv2.cvtColor(img_ori,cv2.COLOR_BGR2GRAY)
    image_blurred=cv2.GaussianBlur(image_gray,(5,5),0)
    image_blurred = cv2.medianBlur(image_blurred, 5)
    text=pytesseract.image_to_string(image_blurred, lang='kor')
    
    return text




def deleting(k,n1):
    deletgui = Toplevel(listing)
    deletgui.title("deleting")
    deletgui.geometry("300x300")
    
    k = (n1.get())
    entry_k = Entry(deleting,textvarible=k).grid(row=1, column=2)
    
    delebut1 = Button(listing,text="삭제",command=popp,activebackground="orange")
    delebut1.pack()

def popp():
    size.pop(k-1)
    
###def saving():
    
    """
    
def lastlist():
    
  """  
    
    
    
def listing():
    listgui = Toplevel(maingui)
    listgui.title("listing")
    listgui.geometry("500x600")
    
    sb = Scrollbar(listgui)
    sb.pack(side = RIGHT, fill = Y)
    lbl = Label(listgui,text = "저장할 리스트")
    ls = Listbox(listgui,yscrollcommand = sb.set)
    
    
    
    newlist = capturing()
    
    size_table=re.split('\n',newlist)
    size=[s for s in size_table]
    
    n=0
    for x in size:
        ls.insert(n,x)
        n=n+1
   
    
   
    lbl.pack()
    ls.pack()
    sb.config(command = ls.yview)
    

    listbut1 = Button(listing,text="삭제",command=deleting,activebackground="orange")
    listbut1.pack()
    ###listbut2 = Button(listing,text="저장",command=saving,activebackground="orange")
    
    ###listbut2.pack()
    
    
but1 = Button(maingui,text="Capture",command=capturing,activebackground="orange")
but2 = Button(maingui,text="List",command=listing,activebackground="orange")
##but3 = Button(maingui,text="저장한 리스트",command=lastlist,activebackground="orange")

but1.pack()
but2.pack()

maingui.mainloop()

