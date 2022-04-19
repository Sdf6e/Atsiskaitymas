from variklis import Mainwallet, Savingswallet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from tkinter import *
from tkinter import messagebox

engine = create_engine('sqlite:///C:/Users/laimi/Desktop/atsiskaitymas/duomenys.db')
session = sessionmaker(bind=engine)()

def sign_in():
    user = username.get()
    code = password.get()

    if (user=="" and code==""):
        messagebox.showinfo("","Blank not Allowed")

    elif (user=="admin" and code=="1234"):
        messagebox.showinfo("","Signed in Sucessfully")
        root = Tk()
        root.title("menu")
        root.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
        root.geometry("400x200")
        mwbl = Label(root, text="Select your wallet").grid(column=2, row=0)
        mwb = Button(root, text="Main wallet", padx=40, pady=40).grid(column=0, row=1)
        swb = Button(root, text="Savings wallet", padx=40, pady=40).grid(column=4, row=1)
        



    else:
        messagebox.showinfo("","incorrect username or password")

def login_screen():

    global loginroot
    global username
    global password
    loginroot = Tk()
    loginroot.title("Biudzetas")
    loginroot.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
    loginroot.geometry("200x80")

    global usernamentry
    global passwordentry
    loginlabel = Label(loginroot, text="Username").grid(column=0, row=0)
    loginlabel2 = Label(loginroot, text="Password").grid(column=0, row=1)
    username=StringVar()
    password=StringVar()
    usernamentry = Entry(loginroot, textvariable=username).grid(column=1, row=0)
    passwordentry = Entry(loginroot, textvariable=password, show="*").grid(column=1, row=1)
    loginbutton = Button(loginroot, text="Sign in", command=sign_in).grid(column=1, row=3, padx=5, pady=5)

    loginroot.mainloop()

login_screen()
