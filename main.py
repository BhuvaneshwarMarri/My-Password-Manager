from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip
win=Tk()
win.title("MyPass")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
p=Password()
def generater():
    pw=p.generate()
    e3.insert(0,pw)
    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    web=e1.get()
    mail=e2.get()
    pw=e3.get()
    if len(web)==0 or len(mail)==0 or len(pw)==0:
        messagebox.showinfo(title="Errror!",message="Don't leave any of the fields empty") 
        return
    x=messagebox.askokcancel(title=web,message=f"Details are ok to save\nEmail: {mail}\nPassword: {pw}\nIs it ok to save?")
    if x:
        with open("file.txt",mode="a") as f:
            f.write(f"Website: {web}\n")
            f.write(f"Mail: {mail}\n")
            f.write(f"Password: {pw}\n")
            f.write("----------------------------------\n")
        e1.delete(0,END)
        e3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
win.config(padx=50,pady=50)

#Elements
l1=Label(text="Website",padx=20,pady=5)
l2=Label(text="Email/Username",padx=20,pady=5)
l3=Label(text="Password",padx=20,pady=5)
b1=Button(text="Generate Password")
b2=Button(text="Add")
e1=Entry()
e1.focus()
e2=Entry()
e2.insert(0,"dummy@gmail.com")
e3=Entry()


#Configurations
e1.config(width=60)
e2.config(width=60)
e3.config(width=35)
b1.config(width=20,height=1,command=generater)
b2.config(width=50,command=add_data)


#Positioning
l1.grid(column=0, row=1, sticky='nsew')
l2.grid(column=0, row=2, sticky='nsew')
l3.grid(column=0, row=3, sticky='nsew')
e1.grid(column=1, row=1, columnspan=2)
e2.grid(column=1, row=2, columnspan=2)
e3.grid(column=1, row=3)
b1.grid(column=2, row=3)
b2.grid(column=1, row=4, columnspan=2,sticky="nsew")


win.mainloop()