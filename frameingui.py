#framing in the python
from tkinter import *
root =Tk()
root.geometry("734x434")
root.minsize(355,355)
root.maxsize(800,800)
root.title("Vedant's GUI")

f1 = Frame(root,bg="grey",borderwidth=7,padx=2.5,pady=3,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,borderwidth=5,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill=X)
l = Label(f1,text="project tkinter-Notepad",font="Helvetica 10 bold")
l1=Label(f2,text="Open a new file",font="Helvetica 10 bold")
l.pack()
l1.pack()
root.mainloop()
