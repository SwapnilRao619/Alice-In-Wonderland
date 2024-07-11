import smtplib
import tkinter as tk
from tkinter import messagebox

class EmailSender:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Sender")

        self.from_label = tk.Label(master, text="From:")
        self.from_label.grid(row=0, column=0, padx=5, pady=5)
        self.from_entry = tk.Entry(master, width=40)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)
        self.from_entry.insert(0, 's69346089@gmail.com')

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(master, show="*", width=40)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_entry.insert(0, 'hyhl lhet sjaw snbn')

        self.to_label = tk.Label(master, text="To:")
        self.to_label.grid(row=2, column=0, padx=5, pady=5)
        self.to_entry = tk.Entry(master, width=40)
        self.to_entry.grid(row=2, column=1, padx=5, pady=5)
        self.to_entry.insert(0, 'hoyis89915@furnato.com')

        self.message_label = tk.Label(master, text="Message:")
        self.message_label.grid(row=3, column=0, padx=5, pady=5)
        self.message_text = tk.Text(master, height=5, width=40)
        self.message_text.grid(row=3, column=1, padx=5, pady=5)
        self.message_text.insert(tk.END, 'Testing')

        self.count_label = tk.Label(master, text="Count:")
        self.count_label.grid(row=4, column=0, padx=5, pady=5)
        self.count_entry = tk.Entry(master, width=10)
        self.count_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        self.count_entry.insert(0, '5')

        self.send_button = tk.Button(master, text="Send Emails", command=self.send_emails)
        self.send_button.grid(row=5, column=0, columnspan=2, pady=10)

    def send_emails(self):
        fromaddr = self.from_entry.get()
        password = self.password_entry.get()
        toaddr = self.to_entry.get()
        message = self.message_text.get("1.0", tk.END)
        count = int(self.count_entry.get())

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtpserver:
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo()
                smtpserver.login(fromaddr, password)
                
                for _ in range(count):
                    smtpserver.sendmail(fromaddr, toaddr, message)
                
            messagebox.showinfo("Success", f"{count} emails sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = EmailSender(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# import smtplib

# toaddrs = 'hoyis89915@furnato.com'
# fromaddrs = 's69346089@gmail.com'
# password = 'hyhl lhet sjaw snbn' 
# message = 'Testing'

# # Establish a connection to Gmail's SMTP server
# # Port 587 is the default port for SMTP submission. It is often used for secure SMTP (SMTPS) submission by email clients to email servers. This port is preferred  for sending emails securely.
# with smtplib.SMTP('smtp.gmail.com', 587) as smtpserver:
#     # We need to greet the SMTP server, initiate a TLS connection for security, and greet the server again.
#     smtpserver.ehlo()
#     smtpserver.starttls()
#     smtpserver.ehlo()
    
#     # Logging in to Gmail account
#     smtpserver.login(fromaddrs, password)
    
#     for i in range(5):
#         smtpserver.sendmail(fromaddrs, toaddrs, message)