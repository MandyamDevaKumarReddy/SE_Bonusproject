
from tkinter import *
import numpy as np
import numexpr as ne


def initialize(master):
    '''
    DOCSTRING: Define what to do on initialization
    '''

    # Add a name to our application
    master.title("Python Calculator")

    # Create a line where we display the equation
    equation = Entry(master, bg="black", foreground="white", width=27, font=('Arial 50'), relief='raised', xscrollcommand='true')

    # Assign a position for the equation line in the grey application window
    equation.grid(row=0, column=0, columnspan=4)

    # Execute the .creteButton() method
    create_button(equation)


def create_button(equation):
    '''
    DOCSTRING: Method that creates the buttons
    INPUT: nothing
    OUTPUT: creates a button
    '''

    # We first create each button one by one with the value we want
    # Using addButton() method which is described below
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

    # Arrange the buttons into lists which represent calculator rows
    row1 = [b_7, b_8, b_9, b_add]
    row2 = [b_4, b_5, b_6, b_sub]
    row3 = [b_1, b_2, b_3, b_mult]
    row4 = [b_clear, b_0, b_equal, b_div]

    # Assign each button to a particular location on the GUI
    row_index = 1
    for row in [row1, row2, row3, row4]:
        col_index = 0
        for buttn in row:
            buttn.grid(row=row_index, column=col_index, columnspan=1)
            col_index += 1
        row_index += 1


def addButton(value, equation):
    '''
    DOCSTRING: Method to process the creation of a button and make it clickable
    INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
    OUTPUT: returns a designed button object
    '''
    return Button(master, activebackground="red", bg="orange", text=value, width=17, height=7, command=lambda: clickButton(str(value), equation), relief=RAISED)


def clickButton(value, equation):
    '''
    DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
    INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
    OUTPUT: what action will be performed when a particular button is clicked
    '''

    # Get the equation that's entered by the user
    current_equation = str(equation.get())

    # # If user clicked "c", then clear the screen
    if value == 'c':
        equation.delete(-1, END)

    # If user clicked "=", then compute the answer and display it
    elif value == '=':
        answer = str(eval(current_equation))
        equation.delete(-1, END)
        equation.insert(0, answer)

    # If user clicked any other button, then add it to the equation line
    else:
        equation.delete(0, END)
        equation.insert(0, current_equation+value)


# Execution
if __name__ == '__main__':

    # Create the main window of an application
    master = Tk()
    # Tell our calculator class to use this window
    initialize(master)

    # Executable loop on the application, waits for user input
    master.mainloop()
