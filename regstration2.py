#registration form by vedant kale
from tkinter import*
root = Tk()
root.geometry('500x500')
root.maxsize(600,600)
root.minsize(200,200)

root.title(" Basic Registration Form")


def printall():
    print("Username:",fullname.get())
    print("Password:",password.get())
    gender()
    #print("Gender:",gender())
    print("Email:",email.get())
    print("age:",age1.get())
def gender():
    male="male"
    female="female"
    if var.get()==1:
        print("Gender:",male)
    else:
        print("Gender",female)
def checkempty():
     if entry5.get()and entry1.get():
        printall()  
     else:
        print('Username and Password required!!')


reg = Label(root, text="Registration form",width=20,bg="grey",font="Times 20 bold")
reg.place(x=100,y=43)


label2 = Label(root, text="Username:",width=20,font="System 10 bold",fg="red")
label2.place(x=80,y=130)
fullname=StringVar()
email=StringVar()
password=StringVar()

entry1 = Entry(root,textvariable=fullname)
entry1.place(x=240,y=130)

label2 = Label(root, text="Email",width=20,font="System 10 bold")
label2.place(x=68,y=180)

entry2 = Entry(root,textvariable=email)
entry2.place(x=240,y=180)

label3 = Label(root, text="Gender",width=20,font="System 10 bold")
label3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label4 = Label(root, text="Age:",width=20,font="System 10 bold")
label4.place(x=70,y=280)
age1 =IntVar()

entry2 = Entry(root,textvariable=age1)
entry2.place(x=240,y=280)

p1 = Label(root, text="Password:",width=20,font="System 10 bold",fg="red")
p1.place(x=68,y=320)
entry5 = Entry(root,textvariable=password)
entry5.place(x=240,y=320)

Button(root,text='Submit',width=10,bg='black',fg='red',font="Courier",command=lambda:[checkempty]).place(x=100,y=380)
Button(root,text='Print details!',width=15,bg='black',fg='red',font="Courier",command=printall).place(x=250,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
#fonts=Courier ,Times,System