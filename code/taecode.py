from tkinter import*


listgui = Toplevel(maingui)
listgui.title("listing")
listgui.geometry("500x600")
    
lbl = Label(listgui,text = "저장할 리스트")
ls = Listbox(listgui)
    
lbl.pack()
ls.pack()
listbut3 = Button(listgui, text="삭제",command = lambda ls=ls: ls.delete(ANCHOR))
    
listbut3.pack()

newlist="안녕하세요 그런 그런 빠바밤"

size_table = re.split('\n',newlist)
size = [s for s in size_table]

n=0
for x in size:
    ls.insert(n,x)
    n=n+1



"""
newlist = capturing()
n = 0;
for x in newlist:
    ls.insert(n,x)
    n = n+1
listbut2 = Button(listgui,text="저장",command=savefile,activebackground="orange")
"""