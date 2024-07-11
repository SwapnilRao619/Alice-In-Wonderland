from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet as f
import os

start=Tk()
start.geometry("200x160")

def gk():
    size=os.stat("key.key").st_size

    if size==0:
        key=f.generate_key()

        fp1=open('key.key','wb')
        fp1.write(key)
        fp1.close()

def ed():
    fp2=open('key.key','rb')
    key=fp2.read()
    boss=f(key)
    fp2.close()

    fp3=open("Data.txt",'rb')
    og=fp3.read()
    encrypted=boss.encrypt(og)
    fp3.close()

    fp4=open("Data_Encr.txt",'wb')
    fp4.write(encrypted)
    os.remove("Data.txt")
    fp4.close()

def dd():
    fp2=open('key.key','rb')
    key=fp2.read()
    boss=f(key)
    fp2.close()

    fp3=open("Data_Encr.txt",'rb')
    de=fp3.read()
    decrypted=boss.decrypt(de)
    fp3.close()

    fp4=open("Data.txt","wb")
    fp4.write(decrypted)
    os.remove("Data_Encr.txt")
    fp4.close()

b1=Button(start,text="Generate Key",command=gk)
b1.place(x=60,y=10)

b2=Button(start,text="Encrypt",command=ed)
b2.place(x=70,y=50)

b3=Button(start,text="Decrypt",command=dd)
b3.place(x=70,y=80)

start.mainloop()