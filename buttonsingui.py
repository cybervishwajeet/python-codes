from tkinter import *
root =Tk()
root.geometry("655x333")
root.title("Vishwa's GUI")

def hello():
    print("hello tkinter users!")

frame1=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN,padx=5)
frame1.pack(side=LEFT,anchor=NW)
b1 =Button(frame1,fg="red",text="Print now",command=hello)#only fun name must be given in the command 
b1.pack(side="right",padx=5)
b2 =Button(frame1,fg="red",text="copy")
b2.pack(side="right",padx=5)
b3 =Button(frame1,fg="red",text="paste now")
b3.pack(side="right",padx=5)
b4 =Button(frame1,fg="red",text="delete now")
b4.pack(side="right",padx=5)

root.mainloop()
