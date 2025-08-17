import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            label_password.config(text="Enter a valid length")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        label_password.config(text=password)
    except ValueError:
        label_password.config(text="Enter a number")

def copy_password():
    password = label_password.cget("text")
    if password and "Enter" not in password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        label_password.config(text="Copied!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg="#1e1e2f")

tk.Label(root, text="Password Length", fg="white", bg="#1e1e2f", font=("Arial", 12)).pack(pady=10)
entry_length = tk.Entry(root, font=("Arial", 12), justify="center")
entry_length.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#ff9800", fg="white", command=generate_password).pack(pady=10)

label_password = tk.Label(root, text="", fg="#00ffcc", bg="#1e1e2f", font=("Arial", 14, "bold"))
label_password.pack(pady=10)

tk.Button(root, text="Copy", font=("Arial", 12), bg="#4caf50", fg="white", command=copy_password).pack(pady=5)

root.mainloop()
