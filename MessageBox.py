from tkinter import Tk
from tkinter import messagebox

win = Tk()
result1= messagebox.askokcancel("Title1","DO YOU REALLY?")
print(result1)
result2= messagebox.askyesno("Title2","DO YOU REALLY?")
print(result2)
result3= messagebox.askyesnocancel("Title3","DO YOU REALLY?")
print(result3)
result4= messagebox.askretrycancel("Warning","DO YOU REALLY?")
print(result4)
result5= messagebox.askquestion("Title5","DO YOU REALLY?")
print(result5)

#win.mainloop()