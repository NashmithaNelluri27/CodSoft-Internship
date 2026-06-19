from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        else:
            messagebox.showwarning("Warning", "Please select an operation!")
            return

        result_label.config(text=f"Result: {result}")
        messagebox.showinfo("Result", f"The Result is {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Main Window
root = Tk()
root.title("Simple Calculator")
root.geometry("500x400")
root.resizable(True, True)

# Heading
heading = Label(
    root,
    text="Simple Calculator",
    font=("Arial", 18, "bold")
)
heading.pack(pady=15)

# First Number
Label(
    root,
    text="Enter First Number",
    font=("Arial", 12)
).pack()

entry1 = Entry(root, width=30, font=("Arial", 12))
entry1.pack(pady=5)

# Second Number
Label(
    root,
    text="Enter Second Number",
    font=("Arial", 12)
).pack()

entry2 = Entry(root, width=30, font=("Arial", 12))
entry2.pack(pady=5)

# Operation Selection
Label(
    root,
    text="Select Operation",
    font=("Arial", 12, "bold")
).pack(pady=10)

operation = StringVar()

frame = Frame(root)
frame.pack()

Radiobutton(
    frame,
    text="Addition (+)",
    variable=operation,
    value="+"
).grid(row=0, column=0, padx=10)

Radiobutton(
    frame,
    text="Subtraction (-)",
    variable=operation,
    value="-"
).grid(row=0, column=1, padx=10)

Radiobutton(
    frame,
    text="Multiplication (*)",
    variable=operation,
    value="*"
).grid(row=1, column=0, padx=10)

Radiobutton(
    frame,
    text="Division (/)",
    variable=operation,
    value="/"
).grid(row=1, column=1, padx=10)

# Calculate Button
Button(
    root,
    text="Calculate",
    width=15,
    font=("Arial", 12),
    command=calculate
).pack(pady=20)

# Result Display
result_label = Label(
    root,
    text="Result:",
    font=("Arial", 16, "bold"),
    width=25,
    height=2,
    relief="solid"
)
result_label.pack(pady=20)

# Exit Button
Button(
    root,
    text="Exit",
    width=15,
    font=("Arial", 12),
    command=root.destroy
).pack(pady=10)

root.mainloop()