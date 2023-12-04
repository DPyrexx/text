# This is the first page when using the application.

import sqlite3
from tkinter import *
from tkinter import messagebox
from sqlfunctions import *
import os

# below are global values for the module scope
current_user = None
email_textbox = None
password_textbox = None


def open_registerPG(): # This is a function created for opening the register page
    os.system("Register_Page.py")


def open_dashboardPG(customerId): # This is a function created to open the dashboard and also send through the customerId
    os.system("Dashboard.py " + str(customerId))


def login_click(): # This function executes on a button click
    # checking to see for current user - Message already logged in
    # global current_user
    print('login_click')
    user_email = str(email_textbox.get()) # These lines take the entry strings and save them
    user_password = str(password_textbox.get())

    try:
        print(user_email, user_password)
        # The line below takes the login variables and passes them into the sql functions page whilst executing the
        # login function from sqlfunctions.py
        user = login(user_email, user_password)
        print("the user", user)
        customerId = user[0]
        user_first_name = user[3]
        current_user = customerId
        open_dashboardPG(customerId) # This opens the dashboard and passes through the customerId
    except Exception as e:
        print(e)
        # Shows an error message box if the user is not found in the database
        messagebox.showerror('Oops!', 'Username or Password not recognized')


# This section creates the window
win = Tk()
win.title("Taxi Booking System - Login")
win.geometry("900x643")
# End of window section

# BACKGROUND SECTION

try:
    bgImage = PhotoImage(file=r'Taxi Booking System Register Background.png')
    Label(win, image=bgImage).place(relwidth=1, relheight=1)
except Exception as e:
    print(e)
    messagebox.showerror('Oops!', 'Background Failed to load')

# END OF BACKGROUND SECTION

page_title = Label(win, bg='white', width=5, text="Login", font=("Roboto", 50, "bold"))
page_title.pack()

# Frames - these are essentially sections within the window

f1 = Frame(win, width=600, height=200, bg='white', bd=10, )
f1.pack(pady=100)

f2 = Frame(win, width=800, height=400, bg='white', bd=10, )
f2.pack(pady=10)

# Labels next to the entries

Email_lbl = Label(f1, bg='white', text="Email: ", width=10, pady=20, font=("Roboto", 18, "bold"))
Email_lbl.grid(column=0, row=0)

Password_lbl = Label(f1, bg='white', text="Password: ", width=10, font=("Roboto", 18, "bold"))
Password_lbl.grid(column=0, row=1)

# Entry for users
email_textbox = Entry(f1, text="Email: ", width=20, font=("Roboto", 14, "bold"))
email_textbox.grid(column=1, row=0)

password_textbox = Entry(f1, show="*", text="Password: ", width=20, font=("Roboto", 14, "bold"))
password_textbox.grid(column=1, row=1)

# Buttons

btn_login = Button(f2, text="Login", font=("Roboto", 15, "bold"), width=18, relief=RAISED,
                   command=login_click)
btn_login.pack(side="left")

btn_register = Button(f2, text="Register", font=("Roboto", 15, "bold"), width=18, relief=RAISED,
                      command=open_registerPG)
btn_register.pack(side="right")

win.mainloop()



