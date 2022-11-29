
from tkinter import *
import numpy as np
import numexpr as ne


def initialize(master):

    master.title("Python Calculator")

    equation = Entry(master, bg="black", foreground="white", width=27,font=('Arial 50'), relief='raised', xscrollcommand='true')

    equation.grid(row=0, column=0, columnspan=4)

    create_button(equation)

def create_button(equation):

    b_1 = addButton(1, equation)
    b_2 = addButton(2, equation)
    b_3 = addButton(3, equation)
    b_add = addButton('+', equation)

    row1 = [b_1, b_2, b_3, b_add]



    row_index = 1
    for row in [row1]:
        col_index = 0
        for buttn in row:
            buttn.grid(row=row_index, column=col_index, columnspan=1)
            col_index += 1
        row_index += 1


def addButton(value, equation):

    return Button(master, text=value, width=17, height=7,  relief=RAISED)

if __name__ == '__main__':

    master = Tk()

    initialize(master)

    master.mainloop()

    create_button(equation)
