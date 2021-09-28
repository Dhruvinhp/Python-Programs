import tkinter as tk

cal= tk.Tk()
cal.title("Calculator")
variable=tk.StringVar()
display = tk.Entry(cal, font=("calibri",20,"bold"),bd=25, textvariable=variable,justify="right")
display.grid(columnspan=5)

def click(number):
    global operator
    operator=str(eval(operator))
    variable.set(operator)
def clear():
    global operator
    operator=" "
    variable.set(operator)
def sum():
    global operator
    operator=str(eval(operator))
    variable.set(operator)
operator=""

btn1 = tk.Button(cal,text="1",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(1))
btn1.grid(row=3,column=0)

btn2 = tk.Button(cal,text="2",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(2))
btn2.grid(row=3,column=1)

btn3 = tk.Button(cal,text="3",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(3))
btn3.grid(row=3,column=2)

btn4 = tk.Button(cal,text="4",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(4))
btn4.grid(row=2,column=0)

btn5 = tk.Button(cal,text="5",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(5))
btn5.grid(row=2,column=1)

btn6 = tk.Button(cal,text="6",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(6))
btn6.grid(row=2,column=2)

btn7 = tk.Button(cal,text="7",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(7))
btn7.grid(row=1,column=0)

btn8 = tk.Button(cal,text="8",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(8))
btn8.grid(row=1,column=1)

btn9 = tk.Button(cal,text="9",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(9))
btn9.grid(row=1,column=2)

btn0 = tk.Button(cal,text="0",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click(0))
btn0.grid(row=4,column=0)

btnpoint = tk.Button(cal,text=".",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click("."))
btnpoint.grid(row=4,column=1)

btnclear = tk.Button(cal,text="clr",font=("arial","18","bold"),bd=5,padx=10,command=clear)
btnclear.grid(row=1,column=4)

btnplus = tk.Button(cal,text="+",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click("+"))
btnplus.grid(row=2,column=4)

btnsub = tk.Button(cal,text="-",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click("-"))
btnsub.grid(row=3,column=4)

btnmul = tk.Button(cal,text="*",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click("*"))
btnmul.grid(row=4,column=4)

btndiv = tk.Button(cal,text="/",font=("arial","18","bold"),bd=5,padx=10,command=lambda:click("/"))
btndiv.grid(row=5,column=4)

btnequal = tk.Button(cal,text="ans",font=("arial","18","bold"),bd=5,padx=10,command=sum)
btnequal.grid(row=4,column=2)

cal.mainloop()