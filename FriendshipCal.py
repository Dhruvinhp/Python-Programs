import random
import tkinter as tk
import datetime
import pandas as pd

def check():
    global result
    text_area=tk.Text(master=root, height=2, width=60, bg="#FFFF99")
    text_area.grid(column=0,row=5)
    result=("Friendship score is: ", result)
    text_area.insert(tk.END,result)

root=tk.Tk()
root.geometry("400x300")
root.title("Friendship calculator")
result=40+int(pd.datetime.now().second)
entryname1=tk.Entry(root, width=20, textVariable=Name1)
entryname1.grid(column=1, row=1)
entryname2=tk.Entry(root, width=20, textVariable=Name2)*
entryname2.grid(column=1, row=2)

button2=tk.Label(text="    CHECK LOVE      ",bg="pink", command=check)
button2.grid(column=1, row=3)
lbl1=tk.Label(root,text="Your Name: ",bg="red", font=('',15,'bold'))
lbl1.grid(row=1, column=0, padx=5, pady=5)
lbl2=tk.Label(root,text="Friends Name: ",bg="red", font=('',15,'bold'))
lbl2.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()




