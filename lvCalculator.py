from tkinter import *
from tkinter.messagebox import showinfo
from random import randint

win=Tk()
#win.iconbitmap("heart.ico")
win.title("love calculator")

def cal():
    number=randint(60,100)
    showinfo("love percentage",f"lovebird's love is{number} %")

#open=Image.open("love.jpg")
#render=open
#main=Label(win,image=render)
#main.grid(row=0,columnspan=2)

lable1=Label(win, text="Enter Your name: ", font=("arial",12,"bold"))
lable1.grid(row=1, column=0, stickey="W")

entry1=Entry(win, font=("arial",12,"bold"))
entry1.grid(row=1, column=1)

lable2=Label(win, text="Enter Your Partner name: ", font=("arial",12,"bold"))
lable2.grid(row=2, column=0, stickey="W")

entry2=Entry(win, font=("arial",12,"bold"))
entry2.grid(row=2, column=1)

button= Button(win, text="Check now !!", font=("arial",12,"bold"))
button.grid(row=3, columnspan=3)

win.mainloop()