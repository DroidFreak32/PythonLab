# p22.py
'''
Write a program that draws a rectangle or an oval, as shown in Figure below: The user selects a figure from a radio button and specifies whether it is filled by selecting a check button.
'''
from tkinter import *


def process():
    canvas.delete("r1", "r2", "o1", "o2")
    if var1.get() == 1 and var2.get() == 1:
        canvas.create_rectangle(100, 100, 1000, 500, fill="black", tags="r1")
    elif var1.get() == 1 and var2.get() == 0:
        canvas.create_rectangle(100, 100, 1000, 500, tags="r2")
    elif var1.get() == 0 and var2.get() == 0:
        canvas.create_oval(10, 10, 190, 90, tags="o1")
    elif var1.get() == 0 and var2.get() == 1:
        canvas.create_oval(10, 10, 190, 90, fill="black", tags="o2")


window = Tk()
frame = Frame(window)
var1 = IntVar()
var2 = IntVar()
canvas = Canvas(window, width=1280, height=720, bg="white")
r1 = Radiobutton(frame, text="Rectangle", variable=var1, value=1, command=process)
r2 = Radiobutton(frame, text="Oval", variable=var1, value=0, command=process)
c1 = Checkbutton(frame, text="Filled", variable=var2, onvalue=1, offvalue=0, command=process)
canvas.pack()
frame.pack()
r1.grid(row="1", column="1")
r2.grid(row="1", column="2")
c1.grid(row="1", column="3")
window.mainloop()

#############################################
