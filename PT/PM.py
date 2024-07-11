import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.passwords = {}

        self.site_label = tk.Label(master, text="Site:")
        self.site_label.grid(row=0, column=0, padx=5, pady=5)
        self.site_entry = tk.Entry(master)
        self.site_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Password", command=self.add_password)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.get_button = tk.Button(master, text="Get Password", command=self.get_password)
        self.get_button.grid(row=2, column=1, padx=5, pady=5)

    def add_password(self):
        site = self.site_entry.get()
        password = self.password_entry.get()
        if site and password:
            self.passwords[site] = password
            messagebox.showinfo("Success", "Password added successfully")
            self.site_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both site and password")

    def get_password(self):
        site = self.site_entry.get()
        if site in self.passwords:
            messagebox.showinfo("Password", f"Password for {site}: {self.passwords[site]}")
        else:
            messagebox.showerror("Error", "Site not found")

def main():
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()