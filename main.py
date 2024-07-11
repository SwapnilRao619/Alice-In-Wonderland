import tkinter as tk
from tkinter import ttk
import subprocess
import os

names = ["Vulnerability Tools", "Cracking Tools", "Password Tools", "Cryptography Tools"]
vt = ["Location Tracker", "Vulnerability Checker", "Ransomware", "Key Logger"]
ct = ["Email Bomber", "Hashed Password Cracker", "", ""]
pw = ["Password Manager", "Password Generator", "Password Strength Checker", ""]
ctg = ["Image Encr./Decr.", "File Encr./Decr.", "AES Cr.", "Caeser Cipher Cr."]

def run_file(file_path):
    try:
        folder_path = os.path.dirname(file_path)
        os.chdir(folder_path)
        subprocess.run(["python", os.path.basename(file_path)])
    except Exception as e:
        print(f"Error running the file: {e}")

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def create_styled_button(parent, text, command):
    button = HoverButton(
        parent,
        text=text,
        command=command,
        font=("Courier", 12, "bold"),
        fg="#00FF00",
        bg="#000000",
        activeforeground="#FF0000",
        activebackground="#1A1A1A",
        bd=0,
        padx=20,
        pady=10,
        relief=tk.FLAT,
        width=25
    )
    button.pack(pady=10)
    return button

def create_sub_window(main_button_number):
    sub_window = tk.Toplevel(root)
    sub_window.title(f"{names[main_button_number-1]}")
    sub_window.geometry("400x500")
    sub_window.configure(bg='#000000')

    label = tk.Label(sub_window, text=names[main_button_number-1], font=("Courier", 16, "bold"), fg="#00FF00", bg="#000000")
    label.pack(pady=20)

    button_texts = {1: vt, 2: ct, 3: pw, 4: ctg}
    texts = button_texts[main_button_number]

    for i, text in enumerate(texts):
        if text:
            file_index = (main_button_number - 1) * 4 + i
            file_path = file_paths[file_index]
            create_styled_button(sub_window, text, lambda fp=file_path: run_file(fp))

root = tk.Tk()
root.title("Alice In Wonderland")
root.geometry("600x700")
root.configure(bg='#000000')

title_font = ("Courier", 36, "bold")
title_label = tk.Label(root, text="Alice In Wonderland", font=title_font, bg='#000000', fg='#00FF00')
title_label.pack(pady=30)

subtitle_font = ("Courier", 14)
subtitle_label = tk.Label(root, text="Enter at your own risk...", font=subtitle_font, bg='#000000', fg='#FF0000')
subtitle_label.pack(pady=10)

for name in names:
    create_styled_button(root, name, lambda n=name: create_sub_window(names.index(n) + 1))

file_paths = [
    r"C:\Users\swapn\Downloads\AIW\VT\LT.py",
    r"C:\Users\swapn\Downloads\AIW\VT\VC.py",
    r"C:\Users\swapn\Downloads\AIW\VT\RW.py",
    r"C:\Users\swapn\Downloads\AIW\VT\KL.py",
    r"C:\Users\swapn\Downloads\AIW\CT\EB.py",
    r"C:\Users\swapn\Downloads\AIW\CT\PHC.py",
    r"placeholder",
    r"placeholder",
    r"C:\Users\swapn\Downloads\AIW\PT\PM.py",
    r"C:\Users\swapn\Downloads\AIW\PT\PG.py",
    r"C:\Users\swapn\Downloads\AIW\PT\PSC.py",
    r"placeholder",
    r"C:\Users\swapn\Downloads\AIW\CGT\IE.py",
    r"C:\Users\swapn\Downloads\AIW\CGT\FE.py",
    r"C:\Users\swapn\Downloads\AIW\CGT\DEAES.py",
    r"C:\Users\swapn\Downloads\AIW\CGT\DECS.py",
    r"placeholder",
]

root.mainloop()