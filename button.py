from tkinter import *

root = Tk()
root.title("Grid Example")#screen title
root.geometry("400x600")#sets the screen geometry

#creating clicked function
def clicked():
    mylbl2=Label(root, text ="You clicked the button!!!").pack()

#creating Label
my_root = Label(root, text ="Button Example!!!", fg="blue",bg="black")
my_root.pack() #packs the label on screen, with padding in x,y.

#creating button
my_btn = Button(root, text ="Click here!", command=clicked) #command
my_btn.pack(pady=50)

root.mainloop()
