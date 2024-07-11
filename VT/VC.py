import tkinter as tk
from tkinter import messagebox
import requests

def check_vulnerability():
    site = site_entry.get()
    try:
        header = requests.get(site).headers
        if "X-Frame-options" in header:
            messagebox.showinfo("Result", f"{site} is NOT VULNERABLE")
        else:
            messagebox.showinfo("Result", f"{site} is VULNERABLE")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Website Vulnerability Checker")

site_label = tk.Label(root, text="Enter the website URL:")
site_label.pack()
site_entry = tk.Entry(root, width=50)
site_entry.pack()

check_button = tk.Button(root, text="Check Vulnerability", command=check_vulnerability)
check_button.pack()

root.mainloop()