from tkinter import *

root = Tk()
root.title("Grid Example")#screen title
root.geometry("400x600")#sets the screen geometry

my_root = Label(root, text ="Grid Example!!!", fg="blue",bg="black")
my_root.grid(row=0,column=0, columnspan=2 ) #packs the label on screen, with padding in x,y.
my_root1 = Label(root, text ="Grid ")
my_root1.grid(row=1,column=0, sticky=E)
my_root2 = Label(root, text ="Example!!!")
my_root2.grid(row=2,column=1)

root.mainloop()
