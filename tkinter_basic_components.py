'''Program to 
    1.import requirements from tkinter
    2.Demonstrate the functionlity of components in tkinter.'''

from tkinter import Tk,Entry,Label,Button

def show():
    print("Done..!")

W=Tk()

W.title("geometry")
W.geometry("800x300")

l=Label(W,text="Enter name",font=("times",20),fg="black")
l.place(x=20,y=50)

e=Entry(W,font=("times",18),fg="black")
e.place(x=160,y=50)

b=Button(W,text="Submit",font=("times",20),fg="white",bg="pink",command=show,width=5,height=1)
b.grid(row=6,column=3,columnspan=4,padx=300,pady=100,sticky='nsew')

W.mainloop()

