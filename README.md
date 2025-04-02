# Tkinter_Calculator
A simple calculator application built with Python's Tkinter library. Provides a user-friendly interface for basic arithmetic operations. See README.md for detailed documentation.

![image](https://github.com/user-attachments/assets/14b07734-2b87-4772-872a-43ba6341599d)

**Features**

Basic arithmetic operations: addition, subtraction, multiplication, and division
Clear button functionality
Error handling for invalid inputs and division by zero
Clean, modern UI with responsive button layout

**How It Works**
**Main Window**

The application creates a fixed-size window (400x450 pixels) titled "Calculator" with a display area at the top and operation buttons below.

**Display Area**
A white frame contains an Entry widget that shows both input and calculation results. The text is right-aligned with a large font for better readability.

**Button Layout**
The calculator uses a 4x4 grid layout:
 - Number buttons (0-9)
 - Operation buttons (+, -, *, /)
 - Clear button (c)
 - Equals button (=)

**Calculation Logic**
When the equals button is pressed:

 1. The application retrieves the expression from the display
 2. Validates that it contains only valid characters
 3. Calculates the result using Python's eval() function
 4. Displays the result or an error message if applicable

**Code Structure**

**Window Setup:** Creates and configures the main application window
**Display Setup:** Creates the calculator's display field
**Button Creation:** Dynamically creates and positions all buttons
**Button Functions:** Defines what each button does when clicked
**Calculation Function:** Handles expression evaluation and error cases
**Grid Configuration:** Ensures buttons expand evenly to fill available space

**Requirements**

Python 3.x
Tkinter (included in standard Python installation)

**Usage**
Run the script with Python:

python calculator.py
