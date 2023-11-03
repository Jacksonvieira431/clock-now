from tkinter import *
from time import *


window = Tk()
window.title("Clock Now")
window.geometry("420x150")
window.resizable(1,1)

l = Label(window,
          font=("Arial", 68,"bold"),
          bg="yellow",
            fg="red",
            bd=25)
l.grid(row=0, column=1)
def update():
    t = strftime("%H:%M:%S")
    l.config(text=t)
    window.after(1000, update)
update()
    
window.mainloop()