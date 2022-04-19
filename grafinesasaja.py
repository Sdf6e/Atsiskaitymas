from variklis import Mainwallet, Savingswallet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from tkinter import *
from tkinter import messagebox

engine = create_engine('sqlite:///C:/Users/laimi/Desktop/atsiskaitymas/duomenys.db')
session = sessionmaker(bind=engine)()

def savings_wallet():
    root = Toplevel()
    root.title("Savings Wallet")
    root.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
    aprasasl = Label(root, text="Budget")
    aprasasl.grid(row=0, column=1)

    idl = Label(root, text="Id")
    ide = Entry(root)
    idl.grid(row=1, column=0)
    ide.grid(row=1, column=1)

    usel = Label(root, text="Use")
    usee = Entry(root)
    usel.grid(row=2, column=0)
    usee.grid(row=2, column=1)

    amountl = Label(root, text="Amount")
    amounte = Entry(root)
    amountl.grid(row=3, column=0)
    amounte.grid(row=3, column=1)

    from_tol = Label(root, text="from / to")
    from_toe = Entry(root)
    from_tol.grid(row=4, column=0)
    from_toe.grid(row=4, column=1)

    datel = Label(root, text="date")
    datee = Entry(root)
    datel.grid(row=5, column=0)
    datee.grid(row=5, column=1)

    buttonnew = Button(root, text="new", padx=32, pady=25)
    buttonnew.grid(row=8, column=0)

    buttonupdate = Button(root, text="update", padx=25, pady=25)
    buttonupdate.grid(row=9, column=0)

    buttondel = Button(root, text="del", padx=50, pady=25)
    buttondel.grid(row=8, column=1)

    buttonlist = Button(root, text="list", padx=50, pady=25)
    buttonlist.grid(row=9, column=1)

    buttonexit = Button(root, text="exit", padx=100, pady=25)
    buttonexit.grid(row=10, column=0, columnspan=2)

    listl = Label(root, text="list")
    listl.grid(row=0, column=2)
    listwindow = Listbox(root, height=20, width=110)
    listwindow.grid(row=1,rowspan=9, column=2)

def main_wallet():
    root = Toplevel()
    root.title("Main Wallet")
    root.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
    aprasasl = Label(root, text="Budget")
    aprasasl.grid(row=0, column=1)

    idl = Label(root, text="Id")
    ide = Entry(root)
    idl.grid(row=1, column=0)
    ide.grid(row=1, column=1)

    usel = Label(root, text="Use")
    usee = Entry(root)
    usel.grid(row=2, column=0)
    usee.grid(row=2, column=1)

    amountl = Label(root, text="Amount")
    amounte = Entry(root)
    amountl.grid(row=3, column=0)
    amounte.grid(row=3, column=1)

    from_tol = Label(root, text="from / to")
    from_toe = Entry(root)
    from_tol.grid(row=4, column=0)
    from_toe.grid(row=4, column=1)

    datel = Label(root, text="date")
    datee = Entry(root)
    datel.grid(row=5, column=0)
    datee.grid(row=5, column=1)

    buttonnew = Button(root, text="new", padx=32, pady=25)
    buttonnew.grid(row=8, column=0)

    buttonupdate = Button(root, text="update", padx=25, pady=25)
    buttonupdate.grid(row=9, column=0)

    buttondel = Button(root, text="del", padx=50, pady=25)
    buttondel.grid(row=8, column=1)

    buttonlist = Button(root, text="list", padx=50, pady=25)
    buttonlist.grid(row=9, column=1)

    buttonexit = Button(root, text="exit", padx=100, pady=25)
    buttonexit.grid(row=10, column=0, columnspan=2)

    listl = Label(root, text="List")
    listl.grid(row=0, column=2)
    listwindow = Listbox(root, height=20, width=110)
    listwindow.grid(row=1,rowspan=9, column=2)

def sw_click():
    savings_wallet()

def mw_click():
    main_wallet()



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
        mwb = Button(root, text="Main wallet", padx=40, pady=40, command=mw_click).grid(column=0, row=1)
        swb = Button(root, text="Savings wallet", padx=40, pady=40, command=sw_click).grid(column=4, row=1)
        



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
