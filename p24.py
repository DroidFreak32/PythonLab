# p24.py
#Write a program that displays a still fan.
from tkinter import *
    
window=Tk();
canvas=Canvas(window,width=500,height=500,bg="white")
canvas.create_arc(0,0,500,500,start=0,extent=45,fill="black")
canvas.create_arc(0,0,500,500,start=90,extent=45,fill="black")
canvas.create_arc(0,0,500,500,start=180,extent=45,fill="black")
canvas.create_arc(0,0,500,500,start=270,extent=45,fill="black")
canvas.pack() 
window.mainloop()

#############################################
