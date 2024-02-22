from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Calc App")
root.geometry("300x400+1800+100")
# root.iconbitmap("icon/cal-logo.ico")
root.resizable(False,False)

def quit():
    confirm = askquestion("ยืนยัน", "คุณต้องการออกจากปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()

def clear():
    display.delete(0,END)
    enableOperator()

def negate():
    result = float(display.get()) * -1

    display.delete(0,END)
    display.insert(0,result)

def inverse():
    result = 1 / float(display.get())

    display.delete(0,END)
    display.insert(0,result)

def square():
    result = float(display.get()) ** 2

    display.delete(0,END)
    display.insert(0,result)

def equal():
    if operator == "add":
        result = float(firstNumber) + float(display.get())
    elif operator == "subtract":
        result = float(firstNumber) - float(display.get())
    elif operator == "divide":
        if display.get() == "0":
            result = "Error"
        else:
            result = float(firstNumber) / float(display.get())
    elif operator == "multiply":
        result = float(firstNumber) * float(display.get())
    elif operator == "exponent":
        result = float(firstNumber) ** float(display.get())

    display.delete(0,END)
    display.insert(0,result)
    enableOperator()

def showNumber(number):
    display.insert(END, number)

    if "." in display.get():
        btnDecimal.config(state=DISABLED)

def operation(value):
    global firstNumber
    global operator

    firstNumber = display.get()
    operator = value

    display.delete(0,END)

    # dissable operator
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnAdd.config(state=DISABLED)
    btnNegate.config(state=DISABLED)

    # print(firstNumber + " " + operator)

def enableOperator():
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnExponent.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnMultiply.config(state=NORMAL)
    btnSubtract.config(state=NORMAL)
    btnAdd.config(state=NORMAL)
    btnDecimal.config(state=NORMAL)
    btnNegate.config(state=NORMAL)

# setiing
fontDisplay = ("Arial", 30)
fontButton = ("Arial", 19)
color = "orange"

# Frame
displayFrame = LabelFrame(root)
btnFrame = LabelFrame(root)
displayFrame.pack(padx=2, pady=5)
btnFrame.pack(pady=2)

# display
display = Entry(displayFrame, border=5, font=fontDisplay, justify=RIGHT)
display.pack(padx=5, pady=5)

# btn
btnClear = Button(btnFrame, bg="white", font=fontButton, text="Clear", command=clear)
btnQuit = Button(btnFrame, bg="white", font=fontButton, text="Quit", command=quit)
btnClear.grid(row=0, column=0, columnspan=2, ipadx=35, pady=1, sticky="WE")
btnQuit.grid(row=0, column=2, columnspan=2, ipadx=35, pady=1, sticky="WE")

# operator
btnInverse = Button(btnFrame, text="1/x", font=fontButton, bg=color, command=inverse)
btnSquare = Button(btnFrame, text="x^", font=fontButton, bg=color, command=square)
btnExponent = Button(btnFrame, text="x^n", font=fontButton, bg=color, command=lambda:operation("exponent"))
btnDivide = Button(btnFrame, text="/", font=fontButton, bg=color, command=lambda:operation("divide"))
btnMultiply = Button(btnFrame, text="*", font=fontButton, bg=color, command=lambda:operation("multiply"))
btnSubtract = Button(btnFrame, text="-", font=fontButton, bg=color, command=lambda:operation("subtract"))
btnAdd = Button(btnFrame, text="+", font=fontButton, bg=color, command=lambda:operation("add"))
btnEqual = Button(btnFrame, text="=", font=fontButton, bg=color, command=equal)
btnDecimal = Button(btnFrame, text=".", font=fontButton, bg=color, command=lambda:showNumber("."))
btnNegate = Button(btnFrame, text="+/-", font=fontButton, bg=color, command=negate)

# number
btn1 = Button(btnFrame, text="1", font=fontButton, bg="black", fg="white", command=lambda:showNumber("1"))
btn2 = Button(btnFrame, text="2", font=fontButton, bg="black", fg="white", command=lambda:showNumber("2"))
btn3 = Button(btnFrame, text="3", font=fontButton, bg="black", fg="white", command=lambda:showNumber("3"))
btn4 = Button(btnFrame, text="4", font=fontButton, bg="black", fg="white", command=lambda:showNumber("4"))
btn5 = Button(btnFrame, text="5", font=fontButton, bg="black", fg="white", command=lambda:showNumber("5"))
btn6 = Button(btnFrame, text="6", font=fontButton, bg="black", fg="white", command=lambda:showNumber("6"))
btn7 = Button(btnFrame, text="7", font=fontButton, bg="black", fg="white", command=lambda:showNumber("7"))
btn8 = Button(btnFrame, text="8", font=fontButton, bg="black", fg="white", command=lambda:showNumber("8"))
btn9 = Button(btnFrame, text="9", font=fontButton, bg="black", fg="white", command=lambda:showNumber("9"))
btn0 = Button(btnFrame, text="0", font=fontButton, bg="black", fg="white", command=lambda:showNumber("0"))

# row 1
btnInverse.grid(row=1, column=0, ipadx=10, pady=1, sticky="WE")
btnSquare.grid(row=1, column=1, ipadx=10, pady=1, sticky="WE")
btnExponent.grid(row=1, column=2, ipadx=10, pady=1, sticky="WE")
btnDivide.grid(row=1, column=3, ipadx=10, pady=1, sticky="WE")

# row 2
btn7.grid(row=2, column=0, ipadx=10, pady=1, sticky="WE")
btn8.grid(row=2, column=1, ipadx=10, pady=1, sticky="WE")
btn9.grid(row=2, column=2, ipadx=10, pady=1, sticky="WE")
btnMultiply.grid(row=2, column=3, ipadx=10, pady=1, sticky="WE")

# row 3
btn4.grid(row=3, column=0, ipadx=10, pady=1, sticky="WE")
btn5.grid(row=3, column=1, ipadx=10, pady=1, sticky="WE")
btn6.grid(row=3, column=2, ipadx=10, pady=1, sticky="WE")
btnSubtract.grid(row=3, column=3, ipadx=10, pady=1, sticky="WE")

# row 4
btn1.grid(row=4, column=0, ipadx=10, pady=1, sticky="WE")
btn2.grid(row=4, column=1, ipadx=10, pady=1, sticky="WE")
btn3.grid(row=4, column=2, ipadx=10, pady=1, sticky="WE")
btnAdd.grid(row=4, column=3, ipadx=10, pady=1, sticky="WE")

# row 5
btnNegate.grid(row=5, column=0, ipadx=10, pady=1, sticky="WE")
btn0.grid(row=5, column=1, ipadx=10, pady=1, sticky="WE")
btnDecimal.grid(row=5, column=2, ipadx=10, pady=1, sticky="WE")
btnEqual.grid(row=5, column=3, ipadx=10, pady=1, sticky="WE")

root.mainloop()