from tkinter import *

root = Tk()
root.title("Calculator App")
root.iconbitmap("icon/cal-logo.ico")
root.geometry("300x400")
root.resizable(0,0)

def negate():
    result = float(display.get()) * -1
    display.delete(0,END)
    display.insert(0,result)

def square():
    result = float(display.get()) ** 2
    display.delete(0,END)
    display.insert(0,result)

def inverse():
    # 1 / x
    if display.get() == "0":
        result = "Error"
    else:
        result = 1 / float(display.get())
    display.delete(0,END)
    display.insert(0,result)

def clearDisplay():
    display.delete(0,END)
    enableOperator()

def showNumber(number):
    display.insert(END, number)
    if "." in display.get():
        btnDecimal.config(state=DISABLED)

def equal():
    if operator == "add":
        result = float(firstNumber) + float(display.get())
    elif operator == "subtract":
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
    display.insert(0,result)

    enableOperator()

def operation(value):
    global firstNumber
    global operator
    operator = value
    firstNumber = display.get()

    # print(operator)

    # reset state
    btnDecimal.config(state=NORMAL)
    display.delete(0,END)

    # disable operator button
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnAdd.config(state=DISABLED)

def enableOperator():
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnExponent.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnMultiply.config(state=NORMAL)
    btnSubtract.config(state=NORMAL)
    btnAdd.config(state=NORMAL)
    btnDecimal.config(state=NORMAL)
    
# setting
color = "orange"
displayFont = ("Arial", 35)
btnFont = ("Arail", 19)

# design frame
displayFrame = LabelFrame(root)
ButtonFrame = LabelFrame(root)
displayFrame.pack(padx=2, pady=5)
ButtonFrame.pack(pady=2)

# display frame
display = Entry(displayFrame, width=30, font=displayFont, bg="white", border=5, justify=RIGHT)
display.pack(padx=5, pady=5)

# Button frame
clear_btn = Button(ButtonFrame, font=btnFont, text="Clear", command=clearDisplay)
quit_btn = Button(ButtonFrame, font=btnFont, text="Quit", command=root.destroy)
clear_btn.grid(row=0, column=0, columnspan=2,ipadx=35, sticky="WE")
quit_btn.grid(row=0, column=2, columnspan=2,ipadx=35, sticky="WE")

# operator button
btnInverse = Button(ButtonFrame, text="1/x", font=btnFont, bg=color, command=inverse)
btnSquare = Button(ButtonFrame, text="x^2", font=btnFont, bg=color, command=square)
btnExponent = Button(ButtonFrame, text="x^n", font=btnFont, bg=color, command=lambda:operation("exponent"))
btnDivide = Button(ButtonFrame, text="/", font=btnFont, bg=color, command=lambda:operation("divide"))
btnMultiply = Button(ButtonFrame, text="*", font=btnFont, bg=color, command=lambda:operation("multiply"))
btnSubtract = Button(ButtonFrame, text="-", font=btnFont, bg=color, command=lambda:operation("subtract"))
btnAdd = Button(ButtonFrame, text="+", font=btnFont, bg=color, command=lambda:operation("add"))
btnEqual = Button(ButtonFrame, text="=", font=btnFont, bg=color, command=equal)
btnDecimal = Button(ButtonFrame, text=".", font=btnFont, bg=color, command=lambda:showNumber("."))
btnNegate = Button(ButtonFrame, text="+/-", font=btnFont, bg=color, command=negate)

# number button
btn9 = Button(ButtonFrame, text="9", font=btnFont, bg="black", fg="white", command=lambda:showNumber(9))
btn8 = Button(ButtonFrame, text="8", font=btnFont, bg="black", fg="white", command=lambda:showNumber(8))
btn7 = Button(ButtonFrame, text="7", font=btnFont, bg="black", fg="white", command=lambda:showNumber(7))
btn6 = Button(ButtonFrame, text="6", font=btnFont, bg="black", fg="white", command=lambda:showNumber(6))
btn5 = Button(ButtonFrame, text="5", font=btnFont, bg="black", fg="white", command=lambda:showNumber(5))
btn4 = Button(ButtonFrame, text="4", font=btnFont, bg="black", fg="white", command=lambda:showNumber(4))
btn3 = Button(ButtonFrame, text="3", font=btnFont, bg="black", fg="white", command=lambda:showNumber(3))
btn2 = Button(ButtonFrame, text="2", font=btnFont, bg="black", fg="white", command=lambda:showNumber(2))
btn1 = Button(ButtonFrame, text="1", font=btnFont, bg="black", fg="white", command=lambda:showNumber(1))
btn0 = Button(ButtonFrame, text="0", font=btnFont, bg="black", fg="white", command=lambda:showNumber(0))

# row 1
btnInverse.grid(row=1, column=0, pady=1, ipadx=10, sticky="WE")
btnSquare.grid(row=1, column=1, padx=1, ipadx=10, sticky="WE")
btnExponent.grid(row=1, column=2, padx=1, ipadx=10, sticky="WE")
btnDivide.grid(row=1, column=3, padx=1, ipadx=10, sticky="WE")

# row 2
btn7.grid(row=2, column=0, padx=1, ipadx=10, sticky="WE")
btn8.grid(row=2, column=1, padx=1, ipadx=10, sticky="WE")
btn9.grid(row=2, column=2, padx=1, ipadx=10, sticky="WE")
btnMultiply.grid(row=2, column=3, padx=1, ipadx=10, sticky="WE")

# row 3
btn4.grid(row=3, column=0, padx=1, ipadx=10, sticky="WE")
btn5.grid(row=3, column=1, padx=1, ipadx=10, sticky="WE")
btn6.grid(row=3, column=2, padx=1, ipadx=10, sticky="WE")
btnSubtract.grid(row=3, column=3, padx=1, ipadx=10, sticky="WE")

# row 4
btn1.grid(row=4, column=0, padx=1, ipadx=10, sticky="WE")
btn2.grid(row=4, column=1, padx=1, ipadx=10, sticky="WE")
btn3.grid(row=4, column=2, padx=1, ipadx=10, sticky="WE")
btnAdd.grid(row=4, column=3, padx=1, ipadx=10, sticky="WE")

# row 5
btnNegate.grid(row=5, column=0, padx=1, ipadx=10, sticky="WE")
btn0.grid(row=5, column=1, padx=1, ipadx=10, sticky="WE")
btnDecimal.grid(row=5, column=2, padx=1, ipadx=10, sticky="WE")
btnEqual.grid(row=5, column=3, padx=1, ipadx=10, sticky="WE")

root.mainloop()