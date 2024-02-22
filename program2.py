from tkinter import *

root = Tk()
root.title("Calcu App")
root.iconbitmap("icon/cal-logo.ico")
root.resizable(0,0)
root.geometry("300x400+1800+100")

def negate():
    result = float(display.get()) * -1
    display.delete(0,END)
    display.insert(0, result)

def clear():
    display.delete(0, END)
    enableOperator()

def square():
    result = float(display.get()) ** 2
    display.delete(0,END)
    display.insert(0, result)

def inverse():
    result = 1 / float(display.get())
    display.delete(0,END)
    display.insert(0, result)

def equal():
    if operator == "add":
        result = float(firstNumber) + float(display.get())
    elif operator == "subtrack":
        result = float(firstNumber) - float(display.get())
    elif operator == "multiply":
        result = float(firstNumber) * float(display.get())
    elif operator == "divide":
        if display.get() == "0":
            result = "Error"
        else:
            result = float(firstNumber) / float(display.get())
    elif operator == "exponent":
        result = float(firstNumber) ** float(display.get())

    display.delete(0,END)
    display.insert(0, result)
    enableOperator()
    # print(result)

def operation(value):
    global firstNumber
    global operator

    operator = value
    firstNumber = float(display.get())

    # print(firstNumber)
    # print(operator)

    # reset
    btnDecimal.config(state=NORMAL)
    display.delete(0, END)

    # disable operator
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnAdd.config(state=DISABLED)
    btnNegate.config(state=DISABLED)

def enableOperator():
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnExponent.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnMultiply.config(state=NORMAL)
    btnSubtract.config(state=NORMAL)
    btnAdd.config(state=NORMAL)
    btnNegate.config(state=NORMAL)

def showNumber(number):
    # print(number)
    display.insert(END, number)

    if "." in display.get():
        btnDecimal.config(state=DISABLED)

# setting
color = "orange"
displayFont = ("Arial", 30, NORMAL)
btnFont = ("Arial", 19, NORMAL)

displayFrame = LabelFrame(root)
btnframe = LabelFrame(root)
displayFrame.pack(padx=2, pady=5)
btnframe.pack(pady=2)

# display Frame 1
display = Entry(displayFrame, font=displayFont, width=30, border=5, justify=RIGHT)
display.pack(padx=5, pady=5)

# row 0
btnClear = Button(btnframe, text="Clear", font=btnFont, bg="white", command=clear)
btnQuit = Button(btnframe, text="Quit", font=btnFont, bg="white", command=root.destroy)
btnClear.grid(row=0, column=0, columnspan=2, ipadx=35, pady=1, sticky="WE")
btnQuit.grid(row=0, column=2, columnspan=2, ipadx=35, pady=1, sticky="WE")

# btn Operator
btnInverse = Button(btnframe, text="1/x", font=btnFont, bg=color, command=inverse)
btnSquare = Button(btnframe, text="x^2", font=btnFont, bg=color, command=square)
btnExponent = Button(btnframe, text="x^n", font=btnFont, bg=color, command=lambda:operation("exponent"))
btnDivide = Button(btnframe, text="/", font=btnFont, bg=color, command=lambda:operation("divide"))
btnMultiply = Button(btnframe, text="*", font=btnFont, bg=color, command=lambda:operation("multiply"))
btnSubtract = Button(btnframe, text="-", font=btnFont, bg=color, command=lambda:operation("subtrack"))
btnAdd = Button(btnframe, text="+", font=btnFont, bg=color, command=lambda:operation("add"))
btnEqual = Button(btnframe, text="=", font=btnFont, bg=color, command=equal)
btnDecimal = Button(btnframe, text=".", font=btnFont, bg=color, command=lambda:showNumber("."))
btnNegate = Button(btnframe, text="+/-", font=btnFont, bg=color, command=negate)

# btn Number
btn1 = Button(btnframe, text="1", font=btnFont, bg="black", fg="white", command=lambda:showNumber("1"))
btn2 = Button(btnframe, text="2", font=btnFont, bg="black", fg="white", command=lambda:showNumber("2"))
btn3 = Button(btnframe, text="3", font=btnFont, bg="black", fg="white", command=lambda:showNumber("3"))
btn4 = Button(btnframe, text="4", font=btnFont, bg="black", fg="white", command=lambda:showNumber("4"))
btn5 = Button(btnframe, text="5", font=btnFont, bg="black", fg="white", command=lambda:showNumber("5"))
btn6 = Button(btnframe, text="6", font=btnFont, bg="black", fg="white", command=lambda:showNumber("6"))
btn7 = Button(btnframe, text="7", font=btnFont, bg="black", fg="white", command=lambda:showNumber("7"))
btn8 = Button(btnframe, text="8", font=btnFont, bg="black", fg="white", command=lambda:showNumber("8"))
btn9 = Button(btnframe, text="9", font=btnFont, bg="black", fg="white", command=lambda:showNumber("9"))
btn0 = Button(btnframe, text="0", font=btnFont, bg="black", fg="white", command=lambda:showNumber("0"))

# row 1
btnInverse.grid(row=1, column=0, ipadx=10, pady=1, sticky="WE")
btnSquare.grid(row=1, column=1, ipadx=10, pady=1, sticky="WE")
btnExponent.grid(row=1, column=2, ipadx=10, pady=1, sticky="WE")
btnDivide.grid(row=1, column=3, ipadx=10, pady=1, sticky="WE")

# row 2
btn7.grid(row=2, column=0, ipadx=10, pady=0, sticky="WE")
btn8.grid(row=2, column=1, ipadx=10, pady=0, sticky="WE")
btn9.grid(row=2, column=2, ipadx=10, pady=0, sticky="WE")
btnMultiply.grid(row=2, column=3, ipadx=10, pady=0, sticky="WE")

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