from math import sqrt, log, log10, sin, cos, tan, exp, factorial
from tkinter import ttk
import tkinter as tk


class Calculator:
    """
    A GUI calculator made with tkinter.
    Supports both standard and scientific calculations.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.layout()
        self.standardButtons()
        self.root.mainloop()

    def layout(self):
        """
        Create different frames for fields and buttons
        """
        self.textFrame = ttk.Frame(self.root, width=400,
                                   height=200, relief=tk.RIDGE)
        self.textFrame.pack()

        self.textField = tk.Text(self.textFrame, height=3, width=50)
        self.textField.grid(row=1, columnspan=4)
        self.textField.focus()

        self.answerField = tk.Text(self.textFrame, height=2, width=50)
        self.answerField.grid(row=2, columnspan=4)
        self.answerField.config(state="disabled")

        self.buttonsFrame = tk.Frame(
            self.root, width=400, height=600, relief=tk.RIDGE)
        self.buttonsFrame.pack()

    def standardButtons(self):
        """
        Provides a standard calculator for basic mathematics operations
        """

        self.sciCalculator = ttk.Button(
            self.buttonsFrame, text="Scientific", command=self.scientificButtons)
        self.sciCalculator.grid(row=1, column=0, ipadx=10,
                                ipady=7)

        def answerFieldOn():
            self.answerField.config(state="normal")
            self.answerField.delete("1.0", "end")

        def answerFieldOff():
            self.answerField.config(state="disabled")
            self.textField.focus()

        def clearEverthingHandler():
            answerFieldOn()
            answerFieldOff()
            clearHandler()

        self.clearEverthing = ttk.Button(
            self.buttonsFrame, text="CE", command=clearEverthingHandler)
        self.clearEverthing.grid(row=1, column=1, ipadx=10, ipady=7)

        def clearHandler():
            self.textField.delete("1.0", "end")
            self.textField.focus()

        self.clear = ttk.Button(
            self.buttonsFrame, text="C", command=clearHandler)
        self.clear.grid(row=1, column=2, ipadx=10, ipady=7)

        def deleteHandler():
            self.textField.delete("1.end - 1 chars")
            self.textField.focus()

        self.delete = ttk.Button(
            self.buttonsFrame, text="⬅", command=deleteHandler)
        self.delete.grid(row=1, column=3, ipadx=10, ipady=7)

        self.seven = ttk.Button(
            self.buttonsFrame, text="7", command=lambda: self.textField.insert("end", "7"))
        self.seven.grid(row=2, column=0, ipadx=10, ipady=7)

        self.eight = ttk.Button(
            self.buttonsFrame, text="8", command=lambda: self.textField.insert("end", "8"))
        self.eight.grid(row=2, column=1, ipadx=10, ipady=7)

        self.nine = ttk.Button(self.buttonsFrame, text="9",
                               command=lambda: self.textField.insert("end", "9"))
        self.nine.grid(row=2, column=2, ipadx=10, ipady=7)

        self.division = ttk.Button(
            self.buttonsFrame, text="÷", command=lambda: self.textField.insert("end", "÷"))
        self.division.grid(row=2, column=3, ipadx=10, ipady=7)

        self.four = ttk.Button(self.buttonsFrame, text="4",
                               command=lambda: self.textField.insert("end", "4"))
        self.four.grid(row=3, column=0, ipadx=10, ipady=7)

        self.five = ttk.Button(self.buttonsFrame, text="5",
                               command=lambda: self.textField.insert("end", "5"))
        self.five.grid(row=3, column=1, ipadx=10, ipady=7)

        self.six = ttk.Button(self.buttonsFrame, text="6",
                              command=lambda: self.textField.insert("end", "6"))
        self.six.grid(row=3, column=2, ipadx=10, ipady=7)

        self.multiplication = ttk.Button(
            self.buttonsFrame, text="×", command=lambda: self.textField.insert("end", "×"))
        self.multiplication.grid(row=3, column=3, ipadx=10, ipady=7)

        self.one = ttk.Button(self.buttonsFrame, text="1",
                              command=lambda: self.textField.insert("end", "1"))
        self.one.grid(row=4, column=0, ipadx=10, ipady=7)

        self.two = ttk.Button(self.buttonsFrame, text="2",
                              command=lambda: self.textField.insert("end", "2"))
        self.two.grid(row=4, column=1, ipadx=10, ipady=7)

        self.three = ttk.Button(
            self.buttonsFrame, text="3", command=lambda: self.textField.insert("end", "3"))
        self.three.grid(row=4, column=2, ipadx=10, ipady=7)

        self.subtraction = ttk.Button(
            self.buttonsFrame, text="-", command=lambda: self.textField.insert("end", "-"))
        self.subtraction.grid(row=4, column=3, ipadx=10, ipady=7)

        self.point = ttk.Button(
            self.buttonsFrame, text=".", command=lambda: self.textField.insert("end", "."))
        self.point.grid(row=5, column=0, ipadx=10, ipady=7)

        self.zero = ttk.Button(self.buttonsFrame, text="0",
                               command=lambda: self.textField.insert("end", "0"))
        self.zero.grid(row=5, column=1, ipadx=10, ipady=7)

        self.squareroot = ttk.Button(
            self.buttonsFrame, text="√", command=lambda: self.textField.insert("end", "√("))
        self.squareroot.grid(row=5, column=2, ipadx=10, ipady=7)

        def equalToHandler():
            expression = self.textField.get("1.0", "end").strip()

            if expression == "\n":
                pass

            else:
                try:
                    expression = expression.replace("×", "*")
                    expression = expression.replace("÷", "/")
                    expression = expression.replace("^", "**")
                    expression = expression.replace("log(", "log10(")
                    expression = expression.replace("mod", "%")
                    expression = expression.replace("e(", "exp(")
                    expression = expression.replace("ln(", "log(")
                    expression = expression.replace("√", "sqrt(")

                    answer = eval(expression)

                    answerFieldOn()
                    self.answerField.insert("end", answer)
                    answerFieldOff()

                except ZeroDivisionError:
                    answerFieldOn()
                    self.answerField.insert("end", "Math Error")
                    answerFieldOff()

                except SyntaxError:
                    answerFieldOn()
                    self.answerField.insert("end", "Syntax Error")
                    answerFieldOff()

        self.equalTo = ttk.Button(
            self.buttonsFrame, text="=", command=equalToHandler)
        self.equalTo.grid(row=5, column=3, ipadx=10, ipady=7)

    def scientificButtons(self):
        """
        Provides basic scientific capabilities
        """
        self.staCalculator = ttk.Button(
            self.buttonsFrame, text="Standard", command=self.standardButtons)
        self.staCalculator.grid(
            row=1, column=0, ipadx=10, ipady=7)

        self.sin_ = ttk.Button(self.buttonsFrame, text="sin",
                               command=lambda: self.textField.insert("end", "sin("))
        self.sin_.grid(row=2, column=0, ipadx=10, ipady=7)

        self.cos_ = ttk.Button(self.buttonsFrame, text="cos",
                               command=lambda: self.textField.insert("end", "cos("))
        self.cos_.grid(row=2, column=1, ipadx=10, ipady=7)

        self.tan_ = ttk.Button(self.buttonsFrame, text="tan",
                               command=lambda: self.textField.insert("end", "tan("))
        self.tan_.grid(row=2, column=2, ipadx=10, ipady=7)

        self.log_ = ttk.Button(self.buttonsFrame, text="log",
                               command=lambda: self.textField.insert("end", "log("))
        self.log_.grid(row=2, column=3, ipadx=10, ipady=7)

        self.exponent = ttk.Button(
            self.buttonsFrame, text="^", command=lambda: self.textField.insert("end", "^"))
        self.exponent.grid(row=3, column=0, ipadx=10, ipady=7)

        self.cubicroot = ttk.Button(
            self.buttonsFrame, text="∛", command=lambda: self.textField.insert("end", "∛("))
        self.cubicroot.grid(row=3, column=1, ipadx=10, ipady=7)

        self.oneoverx = ttk.Button(
            self.buttonsFrame, text="1/x", command=lambda: self.textField.insert("end", "1/("))
        self.oneoverx.grid(row=3, column=2, ipadx=10, ipady=7)

        self.naturallog = ttk.Button(
            self.buttonsFrame, text="ln", command=lambda: self.textField.insert("end", "ln("))
        self.naturallog.grid(row=3, column=3, ipadx=10, ipady=7)

        self.modulo = ttk.Button(
            self.buttonsFrame, text="mod", command=lambda: self.textField.insert("end", "mod"))
        self.modulo.grid(row=4, column=0, ipadx=10, ipady=7)

        self.factorial_ = ttk.Button(self.buttonsFrame, text="factorial",
                                     command=lambda: self.textField.insert("end", "factorial("))
        self.factorial_.grid(row=4, column=1, ipadx=10, ipady=7)

        self.eulersnumber = ttk.Button(
            self.buttonsFrame, text="e", command=lambda: self.textField.insert("end", "exp("))
        self.eulersnumber.grid(row=4, column=2, ipadx=10, ipady=7)

        self.tenexponentx = ttk.Button(
            self.buttonsFrame, text="10^x", command=lambda: self.textField.insert("end", "10^("))
        self.tenexponentx.grid(row=4, column=3, ipadx=10, ipady=7)

        self.abosultevalue = ttk.Button(
            self.buttonsFrame, text="| x |", command=lambda: self.textField.insert("end", "abs("))
        self.abosultevalue.grid(row=5, column=0, ipadx=10, ipady=7)

        self.openbracket = ttk.Button(
            self.buttonsFrame, text="(", command=lambda: self.textField.insert("end", "("))
        self.openbracket.grid(row=5, column=1, ipadx=10, ipady=7)

        self.closebracket = ttk.Button(
            self.buttonsFrame, text=")", command=lambda: self.textField.insert("end", ")"))
        self.closebracket.grid(row=5, column=2, ipadx=10, ipady=7)


if __name__ == "__main__":
    app = Calculator()
