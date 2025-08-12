import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = length_var.get()
    if not str(length).isdigit() or int(length) < 4:
        messagebox.showerror("Invalid Input", "Please enter a valid length (4 or more).")
        return

    length = int(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

length_var = tk.IntVar(value=12)
password_var = tk.StringVar()

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=length_var, font=("Arial", 12), width=10, justify='center').pack()

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, justify='center').pack(pady=5)
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_password).pack(pady=5)

root.mainloop()