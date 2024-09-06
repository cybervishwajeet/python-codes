#grid in python
from tkinter import *
root = Tk()
root.geometry("743x434")
root.title("Griding in GUi")
def getvals():
    print("username:",uservalue.get())
    print("Password:",password.get())

user = Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid()

#varaible classes
#booleanvar,doublevar,Intvar,Stringvar
uservalue=StringVar()
password=StringVar()

user_entry= Entry(root,textvariable=uservalue)
pass_entry= Entry(root,textvariable=password)
user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)
 
Button(text="Submit",command=getvals).grid()
root.mainloop()