#label and the pack attributes in python
from tkinter import *
root =Tk()
root.geometry("734x434")
root.minsize(355,355)
root.maxsize(800,800)
root.title("Vedant's GUI")
label1=Label(text="Hello this is about the Label and Pack attributes")
label1.pack()
#important label options
'''
text-add ths text
bg - background
fg - foreground
font - sets the font
padx - x padding
pady- y padding
relief - border styling :- sunken, raised ,grove ,ridge
'''
label2= Label(text=''' Python was created by Guido van Rossum, and first 
released on February 20, 1991. While you may know the python as a large
\nsnake, the name of the Python programming language comes from an old BBC
\ntelevision comedy sketch series called Monty Python’s Flying Circus.

\nOne of the amazing features of Python is the fact that it is actually one
\nperson’s work. Usually, new programming languages are developed and published
\nby large companies employing lots of professionals, and due to copyright 
\nrules, it is very hard to name any of the people involved in the project. 
\nPython is an exception.''',bg="black",fg="white",padx=55,pady=65,font=("comicsansms",9,"italic"),borderwidth=3,relief=SUNKEN)

'''
important pack options
anchor = nw
label.pack(anchor="nw")
side = top,bottom,left,right
fill=actual streching of the frame
padx=
pady=

'''
label2.pack(side="bottom",anchor="center",fill=X,padx=55,pady=65)
root.mainloop()