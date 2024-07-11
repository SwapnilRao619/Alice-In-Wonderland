import tkinter as tk
from tkinter import ttk
import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{}+-*%?#;:,.\\ "

def generate_password(upper, lower, nums, syms, length, amount, output_text):
    all_chars = ""
    if upper:
        all_chars += uppercase_letters
    if lower:
        all_chars += lowercase_letters
    if nums:
        all_chars += digits
    if syms:
        all_chars += symbols
    
    for _ in range(amount):
        password = "".join(random.sample(all_chars, length))
        output_text.insert(tk.END, f"{password}\n")

def clear_text(output_text):
    output_text.delete(1.0, tk.END)

def create_gui():
    window = tk.Tk()
    window.title("Random Password Generator")
    window.geometry("400x400")

    upper_var = tk.BooleanVar()
    lower_var = tk.BooleanVar()
    nums_var = tk.BooleanVar()
    syms_var = tk.BooleanVar()

    upper_check = tk.Checkbutton(window, text="Uppercase Letters", variable=upper_var)
    lower_check = tk.Checkbutton(window, text="Lowercase Letters", variable=lower_var)
    nums_check = tk.Checkbutton(window, text="Digits", variable=nums_var)
    syms_check = tk.Checkbutton(window, text="Symbols", variable=syms_var)

    upper_check.pack()
    lower_check.pack()
    nums_check.pack()
    syms_check.pack()

    length_label = tk.Label(window, text="Password Length:")
    length_label.pack()
    length_entry = tk.Entry(window)
    length_entry.pack()

    amount_label = tk.Label(window, text="Number of Passwords:")
    amount_label.pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()

    output_frame = ttk.Frame(window)
    output_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    output_text = tk.Text(output_frame, height=10, wrap=tk.NONE)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(output_frame, orient=tk.HORIZONTAL, command=output_text.xview)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
    output_text.config(xscrollcommand=scrollbar.set)

    generate_button = tk.Button(window, text="Generate Passwords", command=lambda: generate_password(
        upper_var.get(), lower_var.get(), nums_var.get(), syms_var.get(),
        int(length_entry.get()), int(amount_entry.get()), output_text))
    generate_button.pack()

    clear_button = tk.Button(window, text="Clear Text", command=lambda: clear_text(output_text))
    clear_button.pack()

    window.mainloop()

create_gui()

