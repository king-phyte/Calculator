from tkinter import *
from tkinter import ttk
from math import *

root = Tk()
root.title("Calculator")
root.option_add("*tearOff", False)


def clearall():
    clear()
    answerField.delete("1.0", "end")
    textField.focus()


def clear():
    textField.delete("1.0", "end")
    textField.focus()


def backspace():
    textField.delete("1.end - 1 chars")
    textField.focus()


def insert7():
    textField.insert("end", "7")


def insert8():
    textField.insert("end", "8")


def insert9():
    textField.insert("end", "9")


def insert4():
    textField.insert("end", "4")


def insert5():
    textField.insert("end", "5")


def insert6():
    textField.insert("end", "6")


def insert3():
    textField.insert("end", "3")


def insert2():
    textField.insert("end", "2")


def insert1():
    textField.insert("end", "1")


def insert0():
    textField.insert("end", "0")


def insertPlus():
    textField.insert("end", "+")


def insertMinus():
    textField.insert("end", "-")


def insertTimes():
    textField.insert("end", "*")


def insertDivide():
    textField.insert("end", "/")


def insertDot():
    textField.insert("end", ".")


def insertOpenBracket():
    textField.insert("end", "*(")


def insertClosedBracket():
    textField.insert("end", ")")


def insertLog():
    textField.insert("end", "log(")


def insertSin():
    textField.insert("end", "sin(")


def insertCos():
    textField.insert("end", "cos(")


def insertTan():
    textField.insert("end", "tan(")


def insertExponent():
    textField.insert("end", "**")


def insertRoot():
    textField.insert("end", "sqrt(")


def insertFactorial():
    textField.insert("end", "factorial(")


def symbolsbtn():
    textField.focus()

    num = ttk.Button(root, text="Num", command=numbtn)
    num.grid(row=3, column=2)

    openBracket = ttk.Button(root, text="(", command=insertOpenBracket)
    openBracket.grid(row=4, column=0)

    closeBracket = ttk.Button(root, text=")", command=insertClosedBracket)
    closeBracket.grid(row=4, column=1)

    log_ = ttk.Button(root, text="log", command=insertLog)
    log_.grid(row=4, column=2)

    sin_ = ttk.Button(root, text="sin", command=insertSin)
    sin_.grid(row=5, column=0)

    cos_ = ttk.Button(root, text="cos", command=insertCos)
    cos_.grid(row=5, column=1)

    tan_ = ttk.Button(root, text="tan", command=insertTan)
    tan_.grid(row=5, column=2)

    exp = ttk.Button(root, text="^", command=insertExponent)
    exp.grid(row=6, column=0)

    sqrt_ = ttk.Button(root, text="√", command=insertRoot)
    sqrt_.grid(row=6, column=1)

    factorial_ = ttk.Button(root, text="!", command=insertFactorial)
    factorial_.grid(row=6, column=2)


def equalbtn():
    ans = textField.get("1.0", "end")

    if ans == "\n":
        pass
    else:
        answerField.delete("1.0", "end")
        try:
            answerField.insert("end", eval(ans.strip()))
        except SyntaxError:
            answerField.insert("end", "Syntax Error")
        except ZeroDivisionError:
            answerField.insert("end", "Math Error")


menubar = Menu(root)
root.config(menu=menubar, width=640, height=480)

menu = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu=menu, label="Menu")
menubar.add_cascade(menu=help_, label="Help")


textField = Text(root, width=40, height=2)
textField.grid(row=1, columnspan=4)
textField.focus()

answerField = Text(root, width=40, height=1)
answerField.grid(row=2, columnspan=4)


clearAll = ttk.Button(root, text="CE", command=clearall)
clearAll.grid(row=3, column=0)

clearB = ttk.Button(root, text="C", command=clear)
clearB.grid(row=3, column=1)

mode = ttk.Button(root, text="Del", command=backspace)
mode.grid(row=3, column=3)


def numbtn():
    divide = ttk.Button(root, text="÷", command=insertDivide)
    divide.grid(row=4, column=3)

    seven = ttk.Button(root, text="7", command=insert7)
    seven.grid(row=4, column=0)

    eight = ttk.Button(root, text="8", command=insert8)
    eight.grid(row=4, column=1)

    nine = ttk.Button(root, text="9", command=insert9)
    nine.grid(row=4, column=2)

    times = ttk.Button(root, text="×", command=insertTimes)
    times.grid(row=5, column=3)

    four = ttk.Button(root, text="4", command=insert4)
    four.grid(row=5, column=0)

    five = ttk.Button(root, text="5", command=insert5)
    five.grid(row=5, column=1)

    six = ttk.Button(root, text="6", command=insert6)
    six.grid(row=5, column=2)

    minus = ttk.Button(root, text="-", command=insertMinus)
    minus.grid(row=6, column=3)

    three = ttk.Button(root, text="3", command=insert3)
    three.grid(row=6, column=0)

    two = ttk.Button(root, text="2", command=insert2)
    two.grid(row=6, column=1)

    one = ttk.Button(root, text="1", command=insert1)
    one.grid(row=6, column=2)

    plus = ttk.Button(root, text="+", command=insertPlus)
    plus.grid(row=7, column=3)

    symbols = ttk.Button(root, text="Sym", command=symbolsbtn)
    symbols.grid(row=3, column=2)

    zero = ttk.Button(root, text="0", command=insert0)
    zero.grid(row=7, column=1)

    dot = ttk.Button(root, text=".", command=insertDot)
    dot.grid(row=7, column=0)

    equal = ttk.Button(root, text="=", command=equalbtn)
    equal.grid(row=7, column=2)


numbtn()
root.mainloop()
