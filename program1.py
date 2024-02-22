from tkinter import *

root = Tk()
root.title("Calc Appli")
root.geometry("300x400+2000+100")
root.iconbitmap("icon/cal-logo.ico")
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
    # 1 /x
    if display.get() == "0":
        "ERROR"
    else:
        result = 1 / float(display.get())
        
    display.delete(0,END)
    display.insert(0,result)


def clear():
    display.delete(0,END)
    enableOperator()

def equal():
    if operator == "add":
        result = float(firstNumber) + float(display.get())
    elif operator == "subtract":
        result = float(firstNumber) - float(display.get())
    elif operator == "multiply":
        result = float(firstNumber) * float(display.get())
    elif operator == "divide":
        if display.get() == "0":
            "ERROR"
        else:
            result = float(firstNumber) / float(display.get())
    elif operator == "exponents":
        result = float(firstNumber) ** float(display.get())

    display.delete(0,END)
    display.insert(0,result)

    enableOperator()

def operation(value):
    global firstNumber
    global operator

    operator = value
    firstNumber = display.get()
    # print(firstNumber)
    # print(operator)

    # reset state
    btnDecimal.config(state=NORMAL)
    display.delete(0,END)
    
    # disable btn
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)
    btnExponents.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnAdd.config(state=DISABLED)

def enableOperator():
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnExponents.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnMultiply.config(state=NORMAL)
    btnSubtract.config(state=NORMAL)
    btnAdd.config(state=NORMAL)


def showNumber(number):
    display.insert(END,number)
    # print(number)

    if "." in display.get():
        btnDecimal.config(state=DISABLED)

# setting
displayFont = ("Arial", 35)
btnFont = ("Arial", 19)
color = "orange"

# frame
displayFrame = LabelFrame(root)
buttonFrame = LabelFrame(root)
displayFrame.pack(padx=2, pady=5)
buttonFrame.pack(pady=2)

# display
display = Entry(displayFrame, font=displayFont, border=5, width=30, justify=RIGHT, bg="white")
display.pack(padx=5, pady=5)

# btn
clear_btn = Button(buttonFrame, font=btnFont, text="Clear", command=clear)
clear_btn.grid(row=0, column=0,columnspan=2, ipadx=35, sticky="WE")

clear_quit = Button(buttonFrame, font=btnFont, text="Quit", command=root.destroy)
clear_quit.grid(row=0, column=2, columnspan=2, ipadx=35, sticky="WE")

# operator
btnInverse = Button(buttonFrame, font=btnFont, text="1/x", bg=color, command=inverse)
btnSquare = Button(buttonFrame, font=btnFont, text="x^2", bg=color, command=square)
btnExponents = Button(buttonFrame, font=btnFont, text="x^n", bg=color, command=lambda:operation("exponents"))
btnDivide = Button(buttonFrame, font=btnFont, text="/", bg=color, command=lambda:operation("divide"))
btnMultiply = Button(buttonFrame, font=btnFont, text="x", bg=color, command=lambda:operation("multiply"))
btnSubtract = Button(buttonFrame, font=btnFont, text="-", bg=color, command=lambda:operation("subtract"))
btnAdd = Button(buttonFrame, font=btnFont, text="+", bg=color, command=lambda:operation("add"))
btnEqual = Button(buttonFrame, font=btnFont, text="=", bg=color, command=equal)
btnDecimal = Button(buttonFrame, font=btnFont, text=".", bg=color, command=lambda:showNumber("."))
btnNegate = Button(buttonFrame, font=btnFont, text="+/-", bg=color, command=negate)

# number
btn1 = Button(buttonFrame, font=btnFont, text="1", bg="black", fg="white", command=lambda:showNumber("1"))
btn2 = Button(buttonFrame, font=btnFont, text="2", bg="black", fg="white", command=lambda:showNumber("2"))
btn3 = Button(buttonFrame, font=btnFont, text="3", bg="black", fg="white", command=lambda:showNumber("3"))
btn4 = Button(buttonFrame, font=btnFont, text="4", bg="black", fg="white", command=lambda:showNumber("4"))
btn5 = Button(buttonFrame, font=btnFont, text="5", bg="black", fg="white", command=lambda:showNumber("5"))
btn6 = Button(buttonFrame, font=btnFont, text="6", bg="black", fg="white", command=lambda:showNumber("6"))
btn7 = Button(buttonFrame, font=btnFont, text="7", bg="black", fg="white", command=lambda:showNumber("7"))
btn8 = Button(buttonFrame, font=btnFont, text="8", bg="black", fg="white", command=lambda:showNumber("8"))
btn9 = Button(buttonFrame, font=btnFont, text="9", bg="black", fg="white", command=lambda:showNumber("9"))
btn0 = Button(buttonFrame, font=btnFont, text="0", bg="black", fg="white", command=lambda:showNumber("0"))

# row 1
btnInverse.grid(row=1, column=0, pady=1, ipadx=10, sticky="WE")
btnSquare.grid(row=1, column=1, pady=1, ipadx=10, sticky="WE")
btnExponents.grid(row=1, column=2, pady=1, ipadx=10, sticky="WE")
btnDivide.grid(row=1, column=3, pady=1, ipadx=10, sticky="WE")

# row 2
btn7.grid(row=2, column=0, pady=1, ipadx=10, sticky="WE")
btn8.grid(row=2, column=1, pady=1, ipadx=10, sticky="WE")
btn9.grid(row=2, column=2, pady=1, ipadx=10, sticky="WE")
btnMultiply.grid(row=2, column=3, pady=1, ipadx=10, sticky="WE")

# row 3
btn4.grid(row=3, column=0, pady=1, ipadx=10, sticky="WE")
btn5.grid(row=3, column=1, pady=1, ipadx=10, sticky="WE")
btn6.grid(row=3, column=2, pady=1, ipadx=10, sticky="WE")
btnSubtract.grid(row=3, column=3, pady=1, ipadx=10, sticky="WE")

# row 4
btn1.grid(row=4, column=0, pady=1, ipadx=10, sticky="WE")
btn2.grid(row=4, column=1, pady=1, ipadx=10, sticky="WE")
btn3.grid(row=4, column=2, pady=1, ipadx=10, sticky="WE")
btnAdd.grid(row=4, column=3, pady=1, ipadx=10, sticky="WE")

# row 5
btnNegate.grid(row=5, column=0, pady=1, ipadx=10, sticky="WE")
btn0.grid(row=5, column=1, pady=1, ipadx=10, sticky="WE")
btnDecimal.grid(row=5, column=2, pady=1, ipadx=10, sticky="WE")
btnEqual.grid(row=5, column=3, pady=1, ipadx=10, sticky="WE")

root.mainloop()