from tkinter import *
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid length!")
            return

        choice = password_type.get()

        if choice == "Simple":
            chars = string.ascii_letters
        elif choice == "Medium":
            chars = string.ascii_letters + string.digits
        elif choice == "Strong":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            messagebox.showwarning("Warning", "Select a complexity level!")
            return

        password = ''.join(random.choice(chars) for _ in range(length))

        result_box.delete("1.0", END)
        result_box.insert(END, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def copy_password():
    password = result_box.get("1.0", END).strip()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied successfully!")

# Main Window
root = Tk()
root.title("Password Generator")
root.geometry("600x500")
root.resizable(True, True)

# Heading
Label(root,
      text="Password Generator",
      font=("Arial", 18, "bold")).pack(pady=10)

# Length Input
Label(root,
      text="Enter Password Length",
      font=("Arial", 12)).pack()

length_entry = Entry(root, width=20, font=("Arial", 12))
length_entry.pack(pady=5)

# Complexity Selection
Label(root,
      text="Select Password Complexity",
      font=("Arial", 12, "bold")).pack(pady=10)

password_type = StringVar()

Radiobutton(root,
            text="Simple (Letters Only)",
            variable=password_type,
            value="Simple").pack()

Radiobutton(root,
            text="Medium (Letters + Numbers)",
            variable=password_type,
            value="Medium").pack()

Radiobutton(root,
            text="Strong (Letters + Numbers + Symbols)",
            variable=password_type,
            value="Strong").pack()

# Generate Button
Button(root,
       text="Generate Password",
       width=20,
       font=("Arial", 12),
       command=generate_password).pack(pady=15)

# Result Label
Label(root,
      text="Generated Password",
      font=("Arial", 12, "bold")).pack()

# Large Result Box
result_box = Text(root,
                  width=50,
                  height=4,
                  font=("Arial", 12))
result_box.pack(pady=10)

# Copy Button
Button(root,
       text="Copy Password",
       width=20,
       font=("Arial", 12),
       command=copy_password).pack(pady=10)

# Exit Button
Button(root,
       text="Exit",
       width=20,
       font=("Arial", 12),
       command=root.destroy).pack(pady=10)

root.mainloop()