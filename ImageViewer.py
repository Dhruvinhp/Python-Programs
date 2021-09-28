import tkinter as tk
from tkinter.messagebox import showerror, showinfo, showwarning
root = tk.Tk()


def errorbox():
    showerror("what are you doing man! Error here!")


def infobox():
    showinfo("INFO")


def warningbox():
    showwarning("WARNING!!")


erbutton = tk.Button(root, text="File not found", command=errorbox())
erbutton.grid(row=0, column=0)
infbutton = tk.Button(root, text="python can be used in ML", command=infobox())
infbutton.grid(row=1, column=0)
warbtn = tk.Button(
    root, text="this variable not used anywhere", command=warningbox())
warbtn.grid(row=2, column=0)

# root=mainloop()
