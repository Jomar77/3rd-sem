from tkinter import *
import time
import os
root = Tk()

frameCnt = 30
frames = [PhotoImage(file='images/giphy.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

text = Label(
    root,
    font = ("Calibri", 25, "bold"),
    foreground = "orange",
    background = "blue",
    text = "Jhon Louise Tan \n General Santos City, April 2001"
)

text.pack(side=RIGHT)

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


label = Label(root)
label.pack(side=LEFT)
root.after(0, update, 0)

root.mainloop()
