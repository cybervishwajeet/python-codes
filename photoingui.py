from tkinter import *
vedant_root = Tk()

vedant_root.geometry("734x434")#width x height and actually shows how the height will be
vedant_root.minsize(200,100)#width,height
vedant_root.maxsize(980,980)

theo =Label(text="Hello this is Vedant's GUI")
theo.pack()#a label must be packed to get displayed
#this how the photo gets into the gui 
photo1= PhotoImage(file="gray2.png")
vedant_label1=Label(image=photo1)
vedant_label1.pack()




vedant_root.mainloop()


