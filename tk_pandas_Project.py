'''Program to
    1.Build a mini project using tkinter and pandas 
    to collect and store data 
    in csv file from desktop application'''

from tkinter import *
from tkinter import messagebox
from pandas import *
from tkinter import filedialog
import os

file=None
def show():
    global file
    if Name.get()=="" or len(Name.get())>12:
        messagebox.showwarning("Warning","Name field should neither be empty nor exceed 12 characters")
        return
    if Regd.get()=="" or len(Regd.get())>10:
        messagebox.showwarning("Warning","Registered No field should neither be empty nor exceed 10 characters")
        return
    if Email.get()=="":
        messagebox.showwarning("Warning","Email field should not be empty")
        return
    if var.get()=="":
        messagebox.showwarning("Choose","Must choose an Elective")
        return
    if ack.get() is False:
        messagebox.showwarning("Check","Must acknowledge")
        return
    if file is None:
        messagebox.showwarning("upload","file must be uploaded")
    else:
        confirm()
        print('Submitted')
        r.destroy()

def select():
    print(f"You selected :{var.get()}")

def confirm():
    global file
    d=DataFrame([{"Name":Name.get(),
       "Redistered No":Regd.get(),
       "email":Email.get(),
       "Elective":var.get(),
       "file":file.name
       }])
    print(d)
    d.to_csv("Elective.csv",mode='a+',index=False,header=not os.path.exists("Elective.csv"))


def of():
    global file
    file=filedialog.askopenfile(mode="r",filetypes=[("text files","*.txt"),("All Files","*.*")])
    if file:
        b2.config(text="Done",state='disabled')
        print(f"File name: {file.name}")
        #w.withdraw()
        
        w2=Tk()
        w2.title("File uploaded")
        w2.geometry("700x300")

        l=Label(w2,
                text="Your file got uploaded Successfully...!",
                font=("timesnewroman",15),
                fg="gold",
                bg="grey")

        def close():
            w2.destroy()
        bu=Button(w2,text="OK..",bg='pink',fg='blue',font=("times new roman",18),command=close)

        bu.place(x=300,y=200)

        l.pack(anchor='center',expand=True)
        w2.mainloop()
        file.close()

    
r=Tk()
r.title("Elective Thread")
r.geometry("800x600")

l1=Label(r,
         text="Name",
         font=("times new roman",20),
         fg="black")
l2=Label(r,
         text="Registered No",
         font=("times new roman",20),
         fg="black")
l3=Label(r,
         text="Email",
         font=("times new roman",20),
         fg="black")
l4=Label(r,
         text="Choose an Elective Thread",
         font=("times new roman",20),
         fg="black")
l5=Label(r,text="upload text document with reason for choosing the elective in 100 words")

Name=Entry(r,
         font=("times new roman",18),
         fg="black")
Regd=Entry(r,
         font=("times new roman",18),
         fg="black")
Email=Entry(r,
         font=("times new roman",18),
         fg="black")

var=StringVar()

r1=Radiobutton(r,
               text="AIML",
               variable=var,
               value="AIML",
               command=select)
r2=Radiobutton(r,
               text="BI",
               variable=var,
               value="BI",
               command=select)
r3=Radiobutton(r,
               text="DS",
               variable=var,
               value="DS",
               command=select)
r4=Radiobutton(r,
               text="ES",
               variable=var,
               value="ES",
               command=select)
r5=Radiobutton(r,
               text="ICB",
               variable=var,
               value="ICB",
               command=select)
r6=Radiobutton(r,
               text="Networks",
               variable=var,
               value="Networks",
               command=select)

ack=BooleanVar()
c=Checkbutton(r,
              text="I acknowledge that all the provided information is true to the best of my knowledge",
              variable=ack,
              onvalue=1,
              offvalue=0)

b=Button(r,
         text="Submit",
         font=("times new roman",30),
         bg="green",
         fg="pink",
         width=10,
         height=1,
         command=show)

b2=Button(r,
          text="Upload",
          font=("timesnweroman",15),
          bg="grey",
          fg="gold",
          command=of)

l1.place(x=40,y=40)
l2.place(x=40,y=100)
l3.place(x=40,y=160)
l4.place(x=40,y=220)
l5.place(x=40,y=400)
b2.place(x=600,y=400)

Name.place(x=200,y=40,width=400)
Regd.place(x=200,y=100,width=400)
Email.place(x=200,y=160,width=400)

r1.place(x=40,y=260)
r2.place(x=40,y=280)
r3.place(x=40,y=300)
r4.place(x=40,y=320)
r5.place(x=40,y=340)
r6.place(x=40,y=360)

c.place(x=40,y=460)

b.place(x=280,y=500)

r.mainloop()
