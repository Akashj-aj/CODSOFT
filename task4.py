import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.config(bg="#1e3d59")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#1e3d59", fg="white")
title_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e3d59")
result_label.pack(pady=10)

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\nIt's a Tie!", fg="blue")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\nYou Win!", fg="green")
    else:
        result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\nYou Lose!", fg="red")

button_frame = tk.Frame(root, bg="#1e3d59")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

root.mainloop()
