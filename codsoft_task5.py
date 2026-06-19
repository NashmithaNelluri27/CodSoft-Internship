from tkinter import *
from tkinter import messagebox

contacts = []

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append([name, phone, email, address])
    display_contacts()

    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# Display Contacts
def display_contacts():
    listbox.delete(0, END)

    for contact in contacts:
        listbox.insert(END, f"{contact[0]} - {contact[1]}")

# Search Contact
def search_contact():
    search = search_entry.get().lower()

    listbox.delete(0, END)

    for contact in contacts:
        if search in contact[0].lower() or search in contact[1]:
            listbox.insert(END, f"{contact[0]} - {contact[1]}")

# Select Contact
def select_contact(event):
    try:
        index = listbox.curselection()[0]
        selected_text = listbox.get(index)

        phone = selected_text.split(" - ")[1]

        for contact in contacts:
            if contact[1] == phone:
                name_entry.delete(0, END)
                phone_entry.delete(0, END)
                email_entry.delete(0, END)
                address_entry.delete(0, END)

                name_entry.insert(0, contact[0])
                phone_entry.insert(0, contact[1])
                email_entry.insert(0, contact[2])
                address_entry.insert(0, contact[3])
                break

    except:
        pass

# Update Contact
def update_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact!")
        return

    old_text = listbox.get(selected[0])
    old_phone = old_text.split(" - ")[1]

    for contact in contacts:
        if contact[1] == old_phone:
            contact[0] = name_entry.get()
            contact[1] = phone_entry.get()
            contact[2] = email_entry.get()
            contact[3] = address_entry.get()

    display_contacts()

# Delete Contact
def delete_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a contact!")
        return

    text = listbox.get(selected[0])
    phone = text.split(" - ")[1]

    for contact in contacts:
        if contact[1] == phone:
            contacts.remove(contact)
            break

    display_contacts()

# Main Window
root = Tk()
root.title("Contact Management System")
root.geometry("800x600")
root.resizable(True, True)

# Heading
Label(root,
      text="Contact Management System",
      font=("Arial", 18, "bold")).pack(pady=10)

# Input Frame
frame = Frame(root)
frame.pack()

Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1)

Label(frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

Label(frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
email_entry = Entry(frame, width=30)
email_entry.grid(row=2, column=1)

Label(frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
address_entry = Entry(frame, width=30)
address_entry.grid(row=3, column=1)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

Button(button_frame,
       text="Add Contact",
       width=15,
       command=add_contact).grid(row=0, column=0, padx=5)

Button(button_frame,
       text="Update Contact",
       width=15,
       command=update_contact).grid(row=0, column=1, padx=5)

Button(button_frame,
       text="Delete Contact",
       width=15,
       command=delete_contact).grid(row=0, column=2, padx=5)

# Search
search_frame = Frame(root)
search_frame.pack(pady=10)

Label(search_frame,
      text="Search").grid(row=0, column=0)

search_entry = Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=5)

Button(search_frame,
       text="Search",
       command=search_contact).grid(row=0, column=2)

Button(search_frame,
       text="Show All",
       command=display_contacts).grid(row=0, column=3, padx=5)

# Contact List
listbox = Listbox(root,
                  width=70,
                  height=15,
                  font=("Arial", 11))

listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", select_contact)

# Exit Button
Button(root,
       text="Exit",
       width=20,
       command=root.destroy).pack(pady=10)

root.mainloop()
