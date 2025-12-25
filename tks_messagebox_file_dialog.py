from tkinter import *
from tkinter import messagebox,filedialog

def warn():
    if len(e1.get())>10 or len(e1.get())<1:
        messagebox.showerror("Error","Name should neither be empty nor exceed 10 characters")
    else:
        print("Submitted...")
        w.destroy()
    
def of():
    file=filedialog.askopenfile(mode="r",filetypes=[("python program","*.py"),("cpp programs","*.cpp"),("All Files","*.*")])
    if file:
        print(f"File name: {file.name}")
        content=file.read()
        print(f"Content: {content}")
        #w.withdraw()
        
        w2=Tk()
        w2.title("File uploaded")
        w2.geometry("700x300")

        l=Label(w2,
                text="Your file got uploaded Successfully...!",
                font=("ariel",25),
                fg="gold",
                bg="grey")

        def close():
            w2.destroy()
        bu=Button(w2,text="OK..",bg='pink',fg='blue',font=("times new roman",18),command=close)

        bu.place(x=300,y=200)

        l.pack(anchor='center',expand=True)
        w2.mainloop()
        file.close()

        
w=Tk()
w.title("Alert and File Navigation")
w.geometry("500x300")

l1=Label(w,
        text='Name',
        font=("times new roman",18))
e1=Entry(w,
        font=("times new roman",16),
        width=20)
l2=Label(w,
         text='Upload a file',
         font=("times new roman",18))

#e2=Entry(w,width=28)

l2.place(x=20,y=60)
#e2.place(x=100,y=60)
l1.place(x=20,y=20)
e1.place(x=100,y=20)

b1=Button(w,
         text="SUBMIT",
         fg="white",
         bg="green",
         font=("times new roman",16),
         command=warn)
b1.place(x=300,y=85)

b2=Button(w,text="upload",
          fg="blue",
          bg="yellow",
          font=("times new roman",15),
          command=of)

b2.place(x=230,y=63,width=60,height=25)

w.mainloop()


