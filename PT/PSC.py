import string
import tkinter as tk
from tkinter import messagebox

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    if show_password:
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

def check_password():
    password = entry_password.get()

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    characters = [upper_case, lower_case, special, digits]
    length = len(password)
    score = 0

    with open('common.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        messagebox.showwarning("Common Password", "Password was found in common list, Score:0/7")
        return

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1
    result_label.config(text=f"Password length is {length}, adding {score} points!")

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1
    result_label.config(text=result_label.cget("text") + f"\nPassword has {sum(characters)} different character types, adding {sum(characters)-1} points!")

    if score < 4:
        messagebox.showinfo("Password Strength", f"The password is quite weak! Score: {score}/7")
    elif score == 4:
        messagebox.showinfo("Password Strength", f"The password is ok! Score: {score}/7")
    elif 4 < score < 6:
        messagebox.showinfo("Password Strength", f"The password is pretty good! Score: {score}/7")
    elif score >= 6:
        messagebox.showinfo("Password Strength", f"The password is strong! Score: {score}/7")

root = tk.Tk()
root.title("Password Checker")
root.geometry("400x200")

label_password = tk.Label(root, text="Enter the password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

show_password = False
show_password_button = tk.Button(root, text="Show Password", command=toggle_password_visibility)
show_password_button.pack()

check_button = tk.Button(root, text="Check Password", command=check_password)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
