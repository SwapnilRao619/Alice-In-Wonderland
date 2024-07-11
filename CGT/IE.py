from tkinter import *
from tkinter import filedialog

start=Tk()
start.geometry("200x160")

def ei():
    f1=filedialog.askopenfile(mode='r', filetype=[('jpg file','*.jpg'),('png file','*.png')])
    if f1 is not None:
        key=e1.get(1.0,END)
        f1n=f1.name

        fp1=open(f1n,'rb')
        i=fp1.read()
        fp1.close()

        i=bytearray(i)
        for index,values in enumerate(i):
            i[index]=values^int(key) #interchangeable operator 

        fp2=open(f1n,'wb') 
        fp2.write(i)
        fp2.close()
    else:
        print("File not chosen.")

b1=Button(start,text="Encrypt/Decrypt",command=ei)
b1.place(x=50,y=10)

e1=Text(start,height=1,width=10)
e1.place(x=55,y=50)

start.mainloop()