import tkinter as tk
from tkinter import messagebox

letters = "abcdefghijklmnopqrstuvwxyz"
no_of_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ""
    key %= no_of_letters  
    if mode == "d":
        key = -key
        
    for letter in text:
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            index = letters.find(letter)
            if index != -1:
                new_index = (index + key) % no_of_letters
                if is_upper:
                    result += letters[new_index].upper()
                else:
                    result += letters[new_index]
            else:
                result += letter
        else:
            result += letter
    
    return result

def process_input():
    choice = choice_var.get()
    key = key_entry.get()
    text = text_entry.get("1.0", "end-1c")  # Get text from Text widget

    if choice == "1":
        ciphertext = encrypt_decrypt(text, "e", int(key))
        result_text.delete("1.0", "end")
        result_text.insert("1.0", ciphertext)
    elif choice == "2":
        original_text = encrypt_decrypt(text, "d", int(key))
        result_text.delete("1.0", "end")
        result_text.insert("1.0", original_text)
    else:
        root.quit()

root = tk.Tk()
root.title("Caesar Cipher")

choice_var = tk.StringVar()
choice_var.set("1")  # Default choice

choice_label = tk.Label(root, text="Choose Action:")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=choice_var, value="1")
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=choice_var, value="2")
key_label = tk.Label(root, text="Enter Key (1-26):")
key_entry = tk.Entry(root)
text_label = tk.Label(root, text="Enter Text:")
text_entry = tk.Text(root, height=5, width=30)
process_button = tk.Button(root, text="Process", command=process_input)
result_label = tk.Label(root, text="Result:")
result_text = tk.Text(root, height=5, width=30)

choice_label.grid(row=0, column=0, sticky="w")
encrypt_radio.grid(row=0, column=1, sticky="w")
decrypt_radio.grid(row=0, column=2, sticky="w")
key_label.grid(row=1, column=0, sticky="w")
key_entry.grid(row=1, column=1, columnspan=2, sticky="we")
text_label.grid(row=2, column=0, sticky="w")
text_entry.grid(row=2, column=1, columnspan=2, sticky="we")
process_button.grid(row=3, column=1, columnspan=2)
result_label.grid(row=4, column=0, sticky="w")
result_text.grid(row=4, column=1, columnspan=2, sticky="we")

root.mainloop()
