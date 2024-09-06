from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
def printall():
    pass

label1 = Label(root, text="Registration form",width=20,bg="grey",font="Times 20 bold")
label1.place(x=100,y=43)


label2 = Label(root, text="FullName",width=20,font="System 10 bold")
label2.place(x=80,y=130)

entry1 = Entry(root)
entry1.place(x=240,y=130)

label2 = Label(root, text="Email",width=20,font="System 10 bold")
label2.place(x=68,y=180)

entry2 = Entry(root)
entry2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font="System 10 bold")
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Age:",width=20,font="System 10 bold")
label_4.place(x=70,y=280)


entry_2 = Entry(root)
entry_2.place(x=240,y=280)

Button(root, text='Submit',width=20,bg='black',fg='red',font="Courier",command=printall).place(x=170,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
#fonts=Courier 