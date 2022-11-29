
from tkinter import *
import numpy as np
import numexpr as ne


def initialize(master):

    master.title("Python Calculator")

    equation = Entry(master, bg="black", foreground="white", width=27, font=('Arial 50'), relief='raised', xscrollcommand='true')

    equation.grid(row=0, column=0, columnspan=4)

    create_button(equation)


def create_button(equation):

    b_0 = addButton(0, equation)
    b_1 = addButton(1, equation)
    b_2 = addButton(2, equation)
    b_3 = addButton(3, equation)
    b_4 = addButton(4, equation)
    b_5 = addButton(5, equation)
    b_6 = addButton(6, equation)
    b_7 = addButton(7, equation)
    b_8 = addButton(8, equation)
    b_9 = addButton(9, equation)
    b_add = addButton('+', equation)
    b_sub = addButton('-', equation)
    b_mult = addButton('*', equation)
    b_div = addButton('/', equation)
    b_clear = addButton('c', equation)
    b_equal = addButton('=', equation)

    row1 = [b_7, b_8, b_9, b_add]
    row2 = [b_4, b_5, b_6, b_sub]
    row3 = [b_1, b_2, b_3, b_mult]
    row4 = [b_clear, b_equal, b_0, b_div]

    row_index = 1
    for row in [row1, row2, row3, row4]:
        col_index = 0
        for buttn in row:
            buttn.grid(row=row_index, column=col_index, columnspan=1)
            col_index += 1
        row_index += 1


def addButton(value, equation):

    return Button(master, text=value, width=17,  command=lambda: clickButton(str(value), equation),height=7)

def clickButton(value, equation):

    current_equation = str(equation.get())
    equation.delete(0, END)
    equation.insert(0, current_equation+value)

if __name__ == '__main__':

    master = Tk()

    initialize(master)

    master.mainloop()
