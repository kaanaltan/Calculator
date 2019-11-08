from tkinter import *

def add():
    a = int(first_number_entry.get())
    b = int(second_number_entry.get())
    output.delete(0.0, END)
    output.insert(END, '{}'.format(a + b))

def subtract():
    a = int(first_number_entry.get())
    b = int(second_number_entry.get())
    output.delete(0.0, END)
    output.insert(END, '{}'.format(a - b))

def multiply():
    a = int(first_number_entry.get())
    b = int(second_number_entry.get())
    output.delete(0.0, END)
    output.insert(END, '{}'.format(a * b))

def divide():
    a = int(first_number_entry.get())
    b = int(second_number_entry.get())
    output.delete(0.0, END)
    output.insert(END, '{}'.format(a / b))

def tk_init():
    
    global window
    window = Tk()
    window.title("Calculator")
    window.configure(background = "black")

    add_button = Button(window, text = 'Add', width = 8, command = add) 
    add_button.grid(row = 0, column = 0, sticky = W)

    subtract_button = Button(window, text = 'Subtract', width = 8, command = subtract) 
    subtract_button.grid(row = 0, column = 1, sticky = W)

    multiply_button = Button(window, text = 'Multiply', width = 8, command = multiply) 
    multiply_button.grid(row = 1, column = 0, sticky = W)

    divide_button = Button(window, text = 'Divide', width = 8, command = divide) 
    divide_button.grid(row = 1, column = 1, sticky = W)

    global first_number_entry
    first_number_entry = Entry(window, width = 4, bg = "white")
    first_number_entry.grid(row = 2, column = 0, sticky = W)

    global second_number_entry
    second_number_entry = Entry(window, width = 4, bg = "white")
    second_number_entry.grid(row = 2, column = 1, sticky = W)

    global output
    output = Text(window, width = 16, height = 3, wrap=WORD, background = 'white')
    output.grid(row = 3, column = 0, rowspan = 1, columnspan = 2, sticky = W)

    window.mainloop()

if __name__ == '__main__':
    tk_init()