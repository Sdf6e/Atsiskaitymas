from variklis import Mainwallet, Savingswallet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from tkinter import *
from tkinter import messagebox

engine = create_engine('sqlite:///C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/duomenys.db')
session = sessionmaker(bind=engine)()

def savings_wallet():
    global listwindow
    loginroot.withdraw()
    root = Toplevel()
    root.title("Savings Wallet")
    root.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
    aprasasl = Label(root, text="Budget")
    aprasasl.grid(row=0, column=1)

    global usee1
    global susevar
    global amounte1
    global samountvar
    global datee1
    global sdatevar

    idl = Label(root, text="Id")
    ide = Entry(root)
    idl.grid(row=1, column=0)
    ide.grid(row=1, column=1)

    usel = Label(root, text="Use")
    susevar = StringVar()
    usee1 = Entry(root, textvariable=susevar)
    usel.grid(row=2, column=0)
    usee1.grid(row=2, column=1)

    amountl = Label(root, text="Amount")
    samountvar = IntVar()
    amounte1 = Entry(root, textvariable=samountvar)
    amountl.grid(row=3, column=0)
    amounte1.grid(row=3, column=1)

    datel = Label(root, text="date")
    sdatevar = StringVar()
    datee1 = Entry(root, textvariable=sdatevar)
    datel.grid(row=4, column=0)
    datee1.grid(row=4, column=1)

    buttonnew = Button(root, text="new", command=new_swallet, padx=32, pady=25)
    buttonnew.grid(row=8, column=0)

    buttonbalance = Button(root, text="balance", command=swallet_balance, padx=25, pady=25)
    buttonbalance.grid(row=9, column=0)

    buttondel = Button(root, text="del",command=swallet_del, padx=50, pady=25)
    buttondel.grid(row=8, column=1)

    buttonlist = Button(root, text="list",command=swallet_list, padx=50, pady=25)
    buttonlist.grid(row=9, column=1)

    buttonexit = Button(root, text="exit",command=root.destroy, padx=100, pady=25)
    buttonexit.grid(row=10, column=0, columnspan=2)
    listl = Label(root, text="list")
    listl.grid(row=0, column=2)
    listwindow = Listbox(root, height=20, width=110)
    listwindow.grid(row=1,rowspan=9, column=2)
    
    
    

def main_wallet():
    global listwindow
    loginroot.withdraw()
    root = Toplevel()
    root.title("Main Wallet")
    root.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
    aprasasl = Label(root, text="Budget")
    aprasasl.grid(row=0, column=1)

    global usevar
    global usee1
    global amountvar
    global amounte1
    global datee1
    global datevar


    idl = Label(root, text="Id")
    ide = Entry(root)
    idl.grid(row=1, column=0)
    ide.grid(row=1, column=1)
    

    usel = Label(root, text="Use")
    usevar = StringVar()
    usee1 = Entry(root, textvariable=usevar)

    usel.grid(row=2, column=0)
    usee1.grid(row=2, column=1)
    

    amountl = Label(root, text="Amount")
    amountvar = IntVar()
    amounte1 = Entry(root, textvariable=amountvar)

    amountl.grid(row=3, column=0)
    amounte1.grid(row=3, column=1)

    datel = Label(root, text="date")
    datevar = StringVar()
    datee1 = Entry(root, textvariable=datevar)
    
    datel.grid(row=5, column=0)
    datee1.grid(row=5, column=1)

    buttonnew = Button(root, text="new",command=new_mwallet, padx=32, pady=25)
    buttonnew.grid(row=8, column=0)

    buttonbalance = Button(root, text="balance", command=mwallet_balance, padx=25, pady=25)
    buttonbalance.grid(row=9, column=0)

    buttondel = Button(root, text="del",command=mwallet_del, padx=50, pady=25)
    buttondel.grid(row=8, column=1)

    buttonlist = Button(root, text="list",command=mwallet_list, padx=50, pady=25)
    buttonlist.grid(row=9, column=1)

    buttonexit = Button(root, text="exit",command=root.destroy, padx=100, pady=25)
    buttonexit.grid(row=10, column=0, columnspan=2)

    listl = Label(root, text="List")
    listl.grid(row=0, column=2)
    listwindow = Listbox(root, height=20, width=110)
    listwindow.grid(row=1,rowspan=9, column=2)


def mwallet_list():
    global filter_all
    listwindow.delete(0, END)
    filter_all = session.query(Mainwallet).all()
    for info in filter_all:
        listwindow.insert(END, info)
    
def swallet_list():
    listwindow.delete(0, END)
    filter_all = session.query(Savingswallet).all()
    for info in filter_all:
        listwindow.insert(END, info)
    
def mwallet_del():
    select = listwindow.curselection()[0]
    session.delete(filter_all[select])
    session.commit()
    mwallet_list()

def swallet_del():
    select = listwindow.curselection()[0]
    filter_alls = session.query(Savingswallet).all()
    session.delete(filter_alls[select])
    session.commit()
    swallet_list()

def mwallet_balance():
    filter_all = session.query(Mainwallet).all()
    suma = 0
    msg = "Main Wallet Balance : "
    for wallet_entry in filter_all:
        suma += wallet_entry.amount
    listwindow.delete(0, END)
    listwindow.insert(END, msg)
    listwindow.insert(END, suma)

def swallet_balance():
    filter_all = session.query(Savingswallet).all()
    suma = 0
    msg = "Main Wallet Balance : "
    for wallet_entry in filter_all:
        suma += wallet_entry.amount
    listwindow.delete(0, END)
    listwindow.insert(END, msg)
    listwindow.insert(END, suma)
        

def new_mwallet():
    newuse = usevar.get()
    newamount = amountvar.get()
    newdate = datevar.get()
    mwallet = Mainwallet(newuse, newamount, newdate)
    session.add(mwallet)
    session.commit()
    listwindow.delete(0, END)
    msg = "new info has been created in main wallet"
    listwindow.insert(END, msg)

def new_swallet():
    newuse = susevar.get()
    newamount = samountvar.get()
    newdate = sdatevar.get()
    swallet = Savingswallet(newuse, newamount, newdate)
    session.add(swallet)
    session.commit()
    listwindow.delete(0, END)
    msg = "new info has been created in savings wallet"
    listwindow.insert(END, msg)

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
        signinroot = Tk()
        signinroot.title("menu")
        signinroot.iconbitmap("C:/Users/laimi/Desktop/atsiskaitymas/Atsiskaitymas/scales.ico")
        signinroot.geometry("400x200")
        mwbl = Label(signinroot, text="Select your wallet").grid(column=2, row=0)
        mwb = Button(signinroot, text="Main wallet", padx=40, pady=40, command=mw_click).grid(column=0, row=1)
        swb = Button(signinroot, text="Savings wallet", padx=40, pady=40, command=sw_click).grid(column=4, row=1)
        
        



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
