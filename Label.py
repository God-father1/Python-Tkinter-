from tkinter import *

root = Tk()
root.title("Label Example")#screen title
root.geometry("400x600")#sets the screen geometry

my_root = Label(root, text ="Label Example!!!", fg="blue",bg="black", font=("sansf",24), relief="raised", state = "disabled", height = 100, width=150)#label name and the content
my_root.pack(pady=50,padx=50) #packs the label on screen, with padding in x,y.
root.mainloop()
