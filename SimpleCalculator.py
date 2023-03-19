import tkinter as tk
def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    multiply = num1 * num2
    return multiply

def div(num1, num2):
    div = num1 / num2
    return div

def Calculate():
    number1 = int(number1_field.get())
    number2 = int(number2_field.get())
    print("Perform the operation")
    print("""1.Addition 2.Subtraction 3.Multiplication.Division""" )
    operation = operation_var.get()
    if operation == 1:
        result = add(number1, number2)
    elif operation == 2:
        result = sub(number1, number2)
    elif operation == 3:
        result = multiply(number1, number2)
    elif operation == 4:
        result = div(number1, number2)
    else:
        result = "INVALID NUMBER"
    print(result)
    result_label.config(text=result)

window = tk.Tk()
window.title("Calculator")

# Create the input fields for number 1 and number 2
number1_label = tk.Label(window, text="Number 1")
number1_label.pack()
number1_field = tk.Entry(window)
number1_field.pack()

number2_label = tk.Label(window, text="Number 2")
number2_label.pack()
number2_field = tk.Entry(window)
number2_field.pack()

# RADIO BUTTON FOR SELECTING OPERATION
operation_label = tk.Label(window, text="OPERATION")
operation_label.pack()
operation_var = tk.IntVar()

addition_radio = tk.Radiobutton(window, text="Addition", variable=operation_var, value=1)
addition_radio.pack()
subtraction_radio = tk.Radiobutton(window, text="Subtract", variable=operation_var, value=2)
subtraction_radio.pack()
multiply_radio = tk.Radiobutton(window, text="Multiply", variable=operation_var, value=3)
multiply_radio.pack()
division_radio = tk.Radiobutton(window, text="Division", variable=operation_var, value=4)
division_radio.pack()

# BUTTON FOR CALCULATING
calculate_button = tk.Button(window, text="Calculate", command=Calculate)
calculate_button.pack()

# DISPLAY_RESULT
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
