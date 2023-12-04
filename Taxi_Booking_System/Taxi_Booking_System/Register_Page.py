# This is the first page when using the application.

from idlelib import window
from sqlfunctions import *
from tkinter import *
from tkinter import messagebox
import os

# This section renders the window
win_Reg = Tk()
win_Reg.title("Taxi Booking System - Register")
win_Reg.geometry("900x643")

current_user = None


def register_click():
    try:
        customer = (
            str(First_name_entry.get()), str(Last_name_entry.get()), str(Email_entry.get()), int(Phone_entry.get()), str(Password_entry.get()), str(Address_entry.get()), str(Town_entry.get()), str(County_entry.get()), str(Postcode_entry.get()),
            str(CrdHolderName_entry.get()), int(CrdNumber_entry.get()),
            str(EXP_entry.get()), int(CVV_entry.get()))
        register_customer(customer)
        print(customer)
    except Exception as e:
        print(e)
# The above function places all of the customer information into a single variable which is then passed into the
# sqlfunctions.py


def login_page_click():
    os.system("Startup_Page.py")
    try:  # This should close then window when the customer clicks on the login button - It crashes in the background
        win_Reg.destroy()
    except Exception as e:
        print(e)


def customer_create(customer):
    register_customer(customer)
    print("func: customer_create")


# BACKGROUND SECTION
try:
    bgImage = PhotoImage(file=r'Taxi Booking System Register Background.png')
    Label(win_Reg, image=bgImage).place(relwidth=1, relheight=1)
except Exception as e:
    print(e)
    messagebox.showerror('Oops!', 'Background Failed to load')

# END OF BACKGROUND SECTION

page_title = Label(win_Reg, bg='white', width=10, text="Register", font=("Roboto", 25, "bold"))
page_title.pack()

# Frames - these are essentially sections within the window

f1 = Frame(win_Reg, width=850, height=100, bg='white', bd=10, )
f1.pack(pady=5)

f2 = Frame(win_Reg, width=850, height=200, bg='white', bd=10, )
f2.pack(pady=10)

f3 = Frame(win_Reg, width=850, height=200, bg='#FFCF97', bd=10, )
f3.pack(pady=10)

# Labels next to the entries
# Frame 1 - Labels
First_name_lbl = Label(f1, bg='white', text="First name: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
First_name_lbl.grid(column=0, row=0)

Last_name_lbl = Label(f1, bg='white', text="Last name: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Last_name_lbl.grid(column=0, row=1)

Email_lbl = Label(f1, bg='white', text="Email: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Email_lbl.grid(column=0, row=2)

Phone_lbl = Label(f1, bg='white', text="Phone: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Phone_lbl.grid(column=0, row=3)

Password_lbl = Label(f1, bg='white', text="Password: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Password_lbl.grid(column=0, row=4)

Address_lbl = Label(f1, bg='white', text="Address: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Address_lbl.grid(column=0, row=5)

Town_lbl = Label(f1, bg='white', text="Town: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Town_lbl.grid(column=0, row=6)

County_lbl = Label(f1, bg='white', text="County: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
County_lbl.grid(column=0, row=7)

Postcode_lbl = Label(f1, bg='white', text="Postcode: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
Postcode_lbl.grid(column=0, row=8)

# frame 2 - Labels

CrdHolderName_lbl = Label(f2, bg='white', text="Card Holders Name: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
CrdHolderName_lbl.grid(column=0, row=4)

CrdNumber_lbl = Label(f2, bg='white', text="Card Number: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
CrdNumber_lbl.grid(column=0, row=5)

EXP_lbl = Label(f2, bg='white', text="EXP Date: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
EXP_lbl.grid(column=0, row=6)

CVV_lbl = Label(f2, bg='white', text="CVV: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
CVV_lbl.grid(column=0, row=7)

# Entry for users - frame 1
First_name_entry = Entry(f1, text="First Name: ", width=20, font=("Roboto", 14, "bold"))
First_name_entry.grid(column=1, row=0)

Last_name_entry = Entry(f1, text="Last Name: ", width=20, font=("Roboto", 14, "bold"))
Last_name_entry.grid(column=1, row=1)

Email_entry = Entry(f1, text="Email: ", width=20, font=("Roboto", 14, "bold"))
Email_entry.grid(column=1, row=2)

Phone_entry = Entry(f1, text="Phone: ", width=20, font=("Roboto", 14, "bold"))
Phone_entry.grid(column=1, row=3)

Password_entry = Entry(f1, show="*", text="Password: ", width=20, font=("Roboto", 14, "bold"))
Password_entry.grid(column=1, row=4)

Address_entry = Entry(f1, text="Address: ", width=20, font=("Roboto", 14, "bold"))
Address_entry.grid(column=1, row=5)

Town_entry = Entry(f1, text="Town: ", width=20, font=("Roboto", 14, "bold"))
Town_entry.grid(column=1, row=6)

County_entry = Entry(f1, text="County: ", width=20, font=("Roboto", 14, "bold"))
County_entry.grid(column=1, row=7)

Postcode_entry = Entry(f1, text="Postcode: ", width=20, font=("Roboto", 14, "bold"))
Postcode_entry.grid(column=1, row=8)

# Frame 2 starts for entries

CrdHolderName_entry = Entry(f2, text="Card Holder Name: ", width=20, font=("Roboto", 14, "bold"))
CrdHolderName_entry.grid(column=1, row=4)

CrdNumber_entry = Entry(f2, text="Card Number: ", width=20, font=("Roboto", 14, "bold"))
CrdNumber_entry.grid(column=1, row=5)

EXP_entry = Entry(f2, text="Exp: ", width=20, font=("Roboto", 14, "bold"))
EXP_entry.grid(column=1, row=6)

CVV_entry = Entry(f2, text="CVV: ", width=20, font=("Roboto", 14, "bold"))
CVV_entry.grid(column=1, row=7)

# Buttons

btn_login = Button(f3, text="Login", font=("Roboto", 15, "bold"), width=9,
                   relief=RAISED,
                   command=login_page_click)  # This is the button for logging into the system. Opens the other page.
btn_login.grid(column=0, row=0)

btn_register = Button(f3, text="Register", font=("Roboto", 15, "bold"), width=9, relief=RAISED,
                      command=register_click)  # This invokes the register_click function which then places the
# information into the database.
btn_register.grid(column=1, row=0)


win_Reg.mainloop() # This required to run the window created at the top of the page
