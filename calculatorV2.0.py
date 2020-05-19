from tkinter import *
from tkinter import ttk
from math import sqrt


class StandardCalculator:

    def __init__(self, master):
        def clearCommand():
            self.answerField.delete("1.0", "end")
            self.textField.focus()

        def clearEverthingCommand():
            self.textField.delete("1.0", "end")
            clearCommand()

        def backspace():
            self.textField.delete("1.end - 1 chars")
            self.textField.focus()

        self.menubar = Menu(master)
        self.tools = Menu(self.menubar)
        self.help_ = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.tools, label="Tools")
        self.menubar.add_cascade(menu=self.help_, label="Help")

        self.textField = Text(master, width=40, height=2)
        self.textField.grid(row=1, columnspan=4)
        self.textField.focus()

        self.answerField = Text(master, width=40, height=1)
        self.answerField.grid(row=2, columnspan=4)

        self.someButton = ttk.Button(master, text="Soon")
        self.someButton.grid(row=3, column=0)

        self.clearEverthing = ttk.Button(
            master, text="CE", command=clearEverthingCommand)
        self.clearEverthing.grid(row=3, column=1)

        self.clear = ttk.Button(master, text="C", command=clearCommand)
        self.clear.grid(row=3, column=2)

        self.delete = ttk.Button(master, text="◀", command=backspace)
        self.delete.grid(row=3, column=3)

    def standardButtons(self, master):
        def clear():
            return self.answerField.delete("1.0", "end")

        def overXCommand():
            ans = self.textField.get("1.0", "end")
            if ans == "\\n":
                pass
            else:
                try:
                    self.answerField.insert("end", (1/eval(ans.strip())))
                except SyntaxError:
                    clear()
                    self.answerField.insert("end", "Syntax Error")
                except ZeroDivisionError:
                    clear()
                    self.answerField.insert("end", "Math Error")

        def xSquaredCommand():
            ans = self.textField.get("1.0", "end")
            if ans == "\n":
                pass
            else:
                try:
                    self.answerField.insert("end", pow(eval(ans.strip()), 2))
                except SyntaxError:
                    clear()
                    self.answerField.insert("end", "Syntax Error")

        def sqrtXCommand():
            ans = self.textField.get("1.0", "end")
            if ans == "\\n":
                pass
            else:
                try:
                    self.answerField.insert("end", sqrt(eval(ans.strip())))
                except SyntaxError:
                    clear()
                    self.answerField.insert("end", "Syntax Error")

        self.overX = ttk.Button(master, text="⅟x", command=overXCommand)
        self.overX.grid(row=4, column=0)

        self.xSquared = ttk.Button(master, text="x²", command=xSquaredCommand)
        self.xSquared.grid(row=4, column=1)

        self.sqrtX = ttk.Button(master, text="√x", command=sqrtXCommand)
        self.sqrtX.grid(row=4, column=2)

    def defaultButtons(self, master):
        def equalsCommand():
            ans = self.textField.get("1.0", "end")

            if ans == "\n":
                pass
            else:
                self.answerField.delete("1.0", "end")
                try:
                    self.answerField.insert("end", eval(ans.strip()))
                except SyntaxError:
                    self.answerField.insert("end", "Syntax Error")
                except ZeroDivisionError:
                    self.answerField.insert("end", "Math Error")

        def genColumns():
            for x in range(3):
                for i in range(2, -1, -1):
                    yield i
            yield 1

        def genRows():
            for i in range(5, 9):
                for x in range(3):
                    yield i

        row_ = genRows()
        column_ = genColumns()
        self.divide = ttk.Button(
            master, text="÷", command=lambda: self.textField.insert("end", "/"))
        self.divide.grid(row=4, column=3)

        self.multiply = ttk.Button(
            master, text="×", command=lambda: self.textField.insert("end", "*"))
        self.multiply.grid(row=5, column=3)

        self.subtract = ttk.Button(
            master, text="-", command=lambda: self.textField.insert("end", "-"))
        self.subtract.grid(row=6, column=3)

        self.add = ttk.Button(
            master, text="+", command=lambda: self.textField.insert("end", "+"))
        self.add.grid(row=7, column=3)

        self.equals = ttk.Button(master, text="=", command=equalsCommand)
        self.equals.grid(row=8, column=3)

        self.nine = ttk.Button(
            master, text="9", command=lambda: self.textField.insert("end", "9"))
        self.nine.grid(row=next(row_), column=next(column_))

        self.eight = ttk.Button(
            master, text="8", command=lambda: self.textField.insert("end", "8"))
        self.eight.grid(row=next(row_), column=next(column_))

        self.seven = ttk.Button(
            master, text="7", command=lambda: self.textField.insert("end", "7"))
        self.seven.grid(row=next(row_), column=next(column_))

        self.six = ttk.Button(
            master, text="6", command=lambda: self.textField.insert("end", "6"))
        self.six.grid(row=next(row_), column=next(column_))

        self.five = ttk.Button(
            master, text="5", command=lambda: self.textField.insert("end", "5"))
        self.five.grid(row=next(row_), column=next(column_))

        self.four = ttk.Button(
            master, text="4", command=lambda: self.textField.insert("end", "4"))
        self.four.grid(row=next(row_), column=next(column_))

        self.three = ttk.Button(
            master, text="3", command=lambda: self.textField.insert("end", "3"))
        self.three.grid(row=next(row_), column=next(column_))

        self.two = ttk.Button(
            master, text="2", command=lambda: self.textField.insert("end", "2"))
        self.two.grid(row=next(row_), column=next(column_))

        self.one = ttk.Button(
            master, text="1", command=lambda: self.textField.insert("end", "1"))
        self.one.grid(row=next(row_), column=next(column_))

        self.zero = ttk.Button(
            master, text="0", command=lambda: self.textField.insert("end", "0"))
        self.zero.grid(row=next(row_), column=next(column_))


def main():
    root = Tk()
    app = StandardCalculator(root)
    app.standardButtons(root)
    app.defaultButtons(root)
    root.title("Calculator")
    root.option_add("*tearOff", False)
    root.mainloop()


if __name__ == "__main__":
    main()
