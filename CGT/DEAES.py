from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from tkinter import *
from tkinter import filedialog
import os

start=Tk()
start.geometry("200x160")

def encr():
    salt=b'\xa5\xa3\x15\x9c\xee,-\xeb\xeb$qo\xcb\xcb\xaeF\xcesm\xd9\x02\xb7Q\xda\xd8\xe8\xa8\x1e\xfb+]\xb8'
    password=ta1.get(1.0,END)
    key=PBKDF2(password,salt,dkLen=32)
    message=ta2.get(1.0,END).encode()
    cipher=AES.new(key,AES.MODE_CBC)

    ciphered_message=cipher.encrypt(pad(message, AES.block_size))
    fp1=open("Encrypted.txt",'wb')
    fp1.write(cipher.iv)
    fp1.write(ciphered_message)
    fp1.close()

def decr():
    salt=b'\xa5\xa3\x15\x9c\xee,-\xeb\xeb$qo\xcb\xcb\xaeF\xcesm\xd9\x02\xb7Q\xda\xd8\xe8\xa8\x1e\xfb+]\xb8'
    password=ta1.get(1.0,END)
    key=PBKDF2(password,salt,dkLen=32)

    fp1=open("Encrypted.txt",'rb')
    iv=fp1.read(16)
    dd=fp1.read()
    cipher=AES.new(key,AES.MODE_CBC,iv=iv)
    decrypted_message=unpad(cipher.decrypt(dd),AES.block_size)

    fp2=open("Decrypted.txt",'wb')
    fp2.write(decrypted_message)
    fp2.close()
    fp1.close()

l1=Label(start,text="Password")
l1.pack()
ta1=Text(start,height="1",width=52)
ta1.pack()
l2=Label(start,text="Message")
l2.pack()
ta2=Text(start,height="1",width=52)
ta2.pack()
b1=Button(start,height="1",width="20",text="Encrypt Message",command=encr)
b1.pack()
b2=Button(start,height="1",width="20",text="Decrypt Message",command=decr)
b2.pack()

start.mainloop()