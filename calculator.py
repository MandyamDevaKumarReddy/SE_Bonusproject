
from tkinter import *
import numpy as np
import numexpr as ne


def initialize(master):

    master.title("Python Calculator")

    equation = Entry(master, bg="black", foreground="white", width=27, relief='raised', xscrollcommand='true')

    equation.grid(row=0, column=0, columnspan=4)



if __name__ == '__main__':

    master = Tk()

    initialize(master)

    master.mainloop()

    create_button(equation)
