from pandas import *
from pandas import DataFrame as df
from tkinter import *
from tkinter import messagebox,filedialog

def Auth():
    d=read_csv("Stored.csv",header=0)
    if mail_entry.get() in d['email']:
        if passwd_entry.get() in d['password']:
            pass
        else:
            messagebox.showerror("Invalid","Password is Invalid")
    else:
        messagebox.showwarning("Try Again","mail Id doesn't exist")

def register():
    t=Tk()
    t.title("Registration")
    t.geometry("500x300")

    Name_label(t,
               text="Name",
               font=("timesnewroman",15))
    Name_label.place(x=120,y=90)

w=Tk()
w.geometry("500x300")

wish_label=Label(w,
                 text="WELCOME",
                 font=("timesnewroman",30),
                 fg="violet",
                 bg="light blue")
wish_label.place(x=140,y=20)

mail_label=Label(w,
                text="Email",
                font=("timesnewroman",15))
mail_label.place(x=30,y=90)
mail_entry=Entry(w,
                 font=("timesnewroman",15),width=30)
mail_entry.place(x=120,y=90)

passwd_label=Label(w,
             text="Password",
             font=("timesnewroman",15))
passwd_label.place(x=30,y=130)
passwd_entry=Entry(w,
                   font=("timesnewroman",15),width=30)
passwd_entry.place(x=120,y=130)

login_button=Button(w,
                    text="Login",
                    font=("timesnewroman",20),
                    bg="green",command=Auth)
login_button.place(x=210,y=180)
Register_label=Label(w,
                     text="Don't have an account",
                     font=("timesnewroman",10))
Register_label.place(x=154,y=234)
Register_button=Button(w,
                       text="Register Now",
                       font=("timesnewroman",10),
                       fg="blue",width=8,height=1)
Register_button.place(x=280,y=230)


w.mainloop()
