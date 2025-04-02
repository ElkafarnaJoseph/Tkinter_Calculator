
from tkinter import *
import tkinter as tk


# Calculation function 
def print_calc():
    try:
        inserted_values = output_field.get()

        if not inserted_values.replace('.', '').replace('+', '').replace('-', '').replace('*', '').replace('/', '').isdigit():
            raise ValueError("Invalid characters in expression")
        
        result = eval(inserted_values)

        output_field.delete(0, tk.END)
        output_field.insert(tk.END, result)
    except ZeroDivisionError:
            output_field.delete(0, tk.END)
            output_field.insert(tk.END, "Error: Division by zero")


def clear_entry():
    # Clears any existing text
    output_field.delete(0, tk.END)
    

# Functions
def print_one():
    output_field.insert(tk.END, 1)  # Inserts text into the text field


def print_two():
    output_field.insert(tk.END, 2)



def print_three():
    output_field.insert(tk.END, 3)


def print_four():
    output_field.insert(tk.END, 4)


def print_five():
    output_field.insert(tk.END, 5)


def print_six():
    output_field.insert(tk.END, 6)


def print_seven():
    output_field.insert(tk.END, 7)


def print_eight():
    output_field.insert(tk.END, 8)


def print_nine():
    output_field.insert(tk.END, 9)


def print_division():
    output_field.insert(tk.END, "/")


def print_multiplier():
    output_field.insert(tk.END, "*")


def print_substraction():
    output_field.insert(tk.END, "-")


def print_addition():
    output_field.insert(tk.END, "+")




def print_zero():
    output_field.insert(tk.END, 0)


# Main app window and title
root = tk.Tk()
root.title("Calculator")

# Size of the window
root.geometry('400x450')

# Disable the resize of the window
root.resizable(False, False)

# Creating frame for the output field
frame = tk.Frame(root, bg='white', height=100)
frame.pack(fill="x")

# Add a text field (Entry widget) in the frame
output_field = tk.Entry(frame, font=("Arial", 24), bd=0, justify="right") # justify the text field to the right of the frame
output_field.pack(fill='x', padx=0, pady=(40, 20)) # pad thing the top and bottom of the with y(top , bottom)
# Buttons/operations frame
operations_frame = tk.Frame(root, bg='lightgray')
operations_frame.pack(fill="both", expand=True) # need to know what this does

# Button styling (shortened so we don't have to copy it many times).
button_style = {
    "font": ("Arial", 18),
    "bg": "#f0f0f0",
    "bd": 0,
    "relief": "flat",
    "activebackground": "#d1d1d1"
}

# Create buttons and arrange them in a grid
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2),("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),("-", 2, 3),
    ("c", 3, 0), ("0", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

# buttons commands
for (text, row, col) in buttons:
    button = tk.Button(operations_frame, text=text, **button_style) # putting the button in the op frame , text btm and we accessing the style from the styling dict using **button_style
    if text == "0":
        button.grid(row=row, column=col, columnspan=1, sticky="nsew")  # Make "0" span two columns 
    else:
        button.grid(row=row, column=col, sticky="nsew")
    # Assign commands dynamically
    if text == "1":
        button.config(command=print_one)
    elif text == "2":
        button.config(command=print_two)
    elif text == "3":
        button.config(command=print_three)
    elif text == "4":
        button.config(command=print_four)
    elif text == "5":
        button.config(command=print_five)
    elif text == "6":
        button.config(command=print_six)
    elif text == "7":
        button.config(command=print_seven)
    elif text == "8":
        button.config(command=print_eight)
    elif text == "9":
        button.config(command=print_nine)
    elif text == "/":
        button.config(command=print_division)
    elif text == "*":
        button.config(command=print_multiplier)
    elif text == "-":
        button.config(command=print_substraction)
    elif text == "+":
        button.config(command=print_addition)
    elif text == "=":
        button.config(command=print_calc)
    elif text == "c":
        button.config(command=clear_entry)
    elif text == "0":
        button.config(command=print_zero)

# Configure grid weights to make buttons expand and fill space evenly
for i in range(4):  # Rows
    operations_frame.rowconfigure(i, weight=1)
for j in range(4):  # Columns
    operations_frame.columnconfigure(j, weight=1)

# Running the simulation
root.mainloop()


