'''Program to demonstrate menu buttons for desktop applications using tkinter'''
from tkinter import *
def Manager():
    print("Manager logged in...")
def Team_Leader():
    print("Team Leader logged in...")
def Employee():
    print("Employee logged in...")
    
k=Tk()
k.title("Login page")
k.geometry("400x250")

Mb=Menubutton(k,text="Logins",fg='white',bg='Blue',relief=RAISED)
Mb.menu=Menu(Mb,tearoff=0)

Mb.menu.add_command(label="Manager",command=Manager)
Mb.menu.add_command(label="Team Leader",command=Team_Leader)
Mb.menu.add_command(label="Employee",command=Employee)
Mb.menu.add_separator()
Mb.menu.add_command(label="Exit")

Mb['menu']=Mb.menu

Mb.menu.config(fg='gold',activebackground='green',bg='gray')

Mb.pack(pady=40)

k.mainloop()
