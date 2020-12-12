import random as rnd
from tkinter import *



def Encrypt(Text):
    step1=''
    for char in Text:
        ascii_val=str(ord(char))
        r=rnd.randint(100,800)
        ascii_val1=str(int(ascii_val)+r)+str(r)
        while ('0' in ascii_val1):
            r=rnd.randint(100,800)
            ascii_val1=str(int(ascii_val)+r)+str(r)
        step1+=ascii_val1
    step2=''
    lst=[step1[i:i+4] for i in range(0, len(step1), 4)]
    for char_ in lst:
        step2+=chr(int(char_))

    return step2

def Decrypt(Text):
    step1=''
    for char in Text:
        step1+=str(ord(char))
    lst=[step1[i:i+6] for i in range(0, len(step1), 6)]
    step2=""
    
    for j in lst:
        if len(j)==6:
            step2+=chr(abs(int(j[:3])-int(j[3:])))
        else:
            j=j+'0'*(6-len(j))
    return step2

def insert(t,s):
    t.delete('1.0',END)
    t.insert('1.0',Encrypt(s.get("1.0","end-1c")))
             
def insert1(t,s):
    t.delete('1.0',END)         
    t.insert('1.0',Decrypt(s.get("1.0","end-1c")))

def clear():
    e1.delete('1.0',END)
    e2.delete('1.0',END)
    
root = Tk()
root.title("Text Encryption")
l=Label(root,text="Text Encryption and Decryption",font="Calibri 14 bold")
lf1=LabelFrame(root, text="Enter Plain Text or Encrypted Text")
lf2=LabelFrame(root, text="Output")
f1=Frame(lf1)
f2=Frame(root)
f3=Frame(lf2)
s1=Scrollbar(f1)
s2=Scrollbar(f3)
e1=Text(f1,height=10,font="Calibri 12")
e2=Text(f3,height=10,font="Calibri 12")
b1=Button(f2,text="Encrypt",command= lambda s=e1,t=e2: insert(t,s))
b2=Button(f2,text="Decrypt",command= lambda s=e1,t=e2: insert1(t,s))
b3=Button(f2,text="Clear",command= lambda : clear())
l.pack(padx=10,pady=7)
s1.pack(side=RIGHT,fill=Y)
e1.pack(side=LEFT,fill=BOTH)
s1.config(command=e1.yview)
e1.config(yscrollcommand=s1.set)
b1.pack(padx=10,pady=5,side=LEFT)
b2.pack(padx=10,pady=5,side=LEFT)
b3.pack(padx=10,pady=5)
s2.pack(side=RIGHT,fill=Y)
e2.pack(side=LEFT,fill=BOTH)
s2.config(command=e2.yview)
e2.config(yscrollcommand=s2.set)
lf1.pack(padx=5,pady=5)
f1.pack(padx=5,pady=5)
f2.pack(padx=10,pady=5)
lf2.pack(padx=5,pady=5)
f3.pack(padx=5,pady=5)
root.mainloop()
        

   
