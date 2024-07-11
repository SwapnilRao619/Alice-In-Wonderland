import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def crack_hash():
    hash_type = hash_type_entry.get().upper()
    wordlist_location = wordlist_location_entry.get()
    hash_input = hash_input_entry.get()

    try:
        with open(wordlist_location, 'rb') as word_list_file:
            word_list = word_list_file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "Wordlist file not found.")
        return

    for word_bytes in word_list:
        word = word_bytes.decode('latin-1').strip()
        if hash_type == "MD5":
            hashed = hashlib.md5(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA1":
            hashed = hashlib.sha1(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA224":
            hashed = hashlib.sha224(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA256":
            hashed = hashlib.sha256(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA384":
            hashed = hashlib.sha384(word.encode('utf-8')).hexdigest()
        elif hash_type == "SHA512":
            hashed = hashlib.sha512(word.encode('utf-8')).hexdigest()
        else:
            messagebox.showerror("Error", "Please choose from the available hash options!")
            return

        if hash_input == hashed:
            messagebox.showinfo("Success", f"HASH FOUND: {word}")
            return

    messagebox.showinfo("Result", "Hash not found in the wordlist.")

def browse_wordlist():
    filename = filedialog.askopenfilename()
    wordlist_location_entry.delete(0, tk.END)
    wordlist_location_entry.insert(0, filename)

root = tk.Tk()
root.title("Hash Cracker")


algorithms_frame = tk.Frame(root)
algorithms_frame.pack(pady=10)

algorithm_label = tk.Label(algorithms_frame, text="Algorithms available: MD5/SHA1/SHA224/SHA256/SHA384/SHA512")
algorithm_label.pack()

hash_frame = tk.Frame(root)
hash_frame.pack(pady=10)

hash_label = tk.Label(hash_frame, text="Hash Type:")
hash_label.grid(row=0, column=0, padx=10)

hash_type_entry = tk.Entry(hash_frame)
hash_type_entry.grid(row=0, column=1, padx=10)

wordlist_frame = tk.Frame(root)
wordlist_frame.pack(pady=10)

wordlist_label = tk.Label(wordlist_frame, text="Wordlist Location:")
wordlist_label.grid(row=0, column=0, padx=10)

wordlist_location_entry = tk.Entry(wordlist_frame, width=40)
wordlist_location_entry.grid(row=0, column=1, padx=10)

browse_button = tk.Button(wordlist_frame, text="Browse", command=browse_wordlist)
browse_button.grid(row=0, column=2, padx=10)

hash_input_frame = tk.Frame(root)
hash_input_frame.pack(pady=10)

hash_input_label = tk.Label(hash_input_frame, text="Hash:")
hash_input_label.grid(row=0, column=0, padx=10)

hash_input_entry = tk.Entry(hash_input_frame)
hash_input_entry.grid(row=0, column=1, padx=10)

crack_button = tk.Button(root, text="Crack Hash", command=crack_hash)
crack_button.pack(pady=10)

root.mainloop()
