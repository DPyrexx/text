# This is the home page when using the application.

from tkinter import *
from tkinter import messagebox
import sys
from sqlfunctions import *

win_dash = Tk()
win_dash.title("Taxi Booking System - Homepage")
win_dash.geometry("900x643")

print(sys.argv)  # This is all data passed into this file
customerId = int(
    sys.argv[1])  # This takes the customerId from the Startup_page.py and then changes it value back to an int

booking_frame = None
make_booking_frame = None


def dashboard_welcome():  # There are no parameters since the variable exists in the parent (module).

    try:
        print("func: dashboard_welcome", customerId)
        customer = get_customer_by_id(customerId)  # This passes through the customerId and then executes the function
        # get_customer_by_id
        print(customer)
        set_welcome_message(customer[1])  # This executes the function whilst using the firstname of the customer (index 1)
    except Exception as e:
        print("ARRRRGH ERROR in Dashboard_welcome()", e)


def set_welcome_message(customerName):
    welcome_message = "Welcome, " + customerName
    page_title.config(text=welcome_message)
    # The above function places the customers name into a label to place a greeting specific to the customer


def set_booking_view_message(customerBooking):
    view_booking_message = "Booking Details" + customerBooking
    messagebox.INFO(view_booking_message)


def make_a_booking_click(data):
    try:
        print("func: make_a_booking_click")
        make_booking(data)  # this sends the information to the sqlfunctions
        print("func: make_a_booking", customerId)
        view_a_booking_click()
    except Exception as e:
        print("ERROR make_a_booking", e)


def render_make_booking():  # This function was created to render the form on a button click

    make_booking_frame = Frame(win_dash, width=800, height=400, bd=10, )
    make_booking_frame.pack(pady=10)

    # This is used when showing the booking information
    Pickup_Location_lbl = Label(make_booking_frame, bg='white', text="Pickup Location: ", anchor="e", width=20,
                                font=("Roboto", 12, "bold"))
    Pickup_Location_lbl.grid(column=0, row=0)

    Dropoff_location_lbl = Label(make_booking_frame, bg='white', text="Dropoff Location: ", anchor="e", width=20,
                                 font=("Roboto", 12, "bold"))
    Dropoff_location_lbl.grid(column=0, row=1)

    Date_lbl = Label(make_booking_frame, bg='white', text="Date: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
    Date_lbl.grid(column=0, row=2)

    Time_lbl = Label(make_booking_frame, bg='white', text="Time: ", anchor="e", width=20, font=("Roboto", 12, "bold"))
    Time_lbl.grid(column=0, row=3)

    # Entry for users
    Pickup_location_entry = Entry(make_booking_frame, text="Pickup Location: ", width=20, font=("Roboto", 14, "bold"))
    Pickup_location_entry.grid(column=1, row=0)

    Dropoff_location_entry = Entry(make_booking_frame, text="Dropoff Location: ", width=20, font=("Roboto", 14, "bold"))
    Dropoff_location_entry.grid(column=1, row=1)

    Date_entry = Entry(make_booking_frame, text="Date: ", width=20, font=("Roboto", 14, "bold"))
    Date_entry.grid(column=1, row=2)

    Time_entry = Entry(make_booking_frame, text="Time: ", width=20, font=("Roboto", 14, "bold"))
    Time_entry.grid(column=1, row=3)

    # button
    btn_book = Button(make_booking_frame, text="Book", font=("Roboto", 15, "bold"), width=18, relief=RAISED,
                      command=lambda: make_a_booking_click((customerId,
                                                            (str(Pickup_location_entry.get())),
                                                            str((Dropoff_location_entry.get())), str(Date_entry.get()),
                                                            str(Time_entry.get())
                                                            # This is grabbing all of the information from the entry boxes
                                                            )))
    btn_book.grid(column=0, row=4)

    # make_booking_frame.hidden = 1


def show_make_bookings(): # This function changes the global values to allow for the form to render when the button
    # is clicked
    make_booking_frame.hidden = 0
    bookings_frame.hidden = 1


def view_a_booking_click():
    try:
        get_booking(customerId)
        print("func: make_a_booking_click", customerId)
        get_booking(customerId)
        bookings = get_booking(customerId)  # This puts the data from get_booking func into a variable
        print_bookings(bookings)
        # messagebox.showinfo('Title', display_booking_message) # This displays the variable above as a pop up message
    except Exception as e:
        print("ERROR view_a_booking_click", e)


bookings_frame = None


def print_bookings(bookings):
    bookings_frame = None
    bookings_frame = Frame(win_dash, width=800, height=400, bd=10, )
    bookings_frame.pack(pady=40)
    for row, booking in enumerate(bookings, start=0):
        print(row, booking)
        bookingId = booking[0]
        bookingTitle = booking[1]
        bookingPickup = booking[4]
        label = Label(bookings_frame, bg='white', text=bookingTitle + " " + bookingPickup, anchor="e", width=20,
                      font=("Roboto", 12, "bold"))
        label.grid(column=0, row=row)
        btn = Button(bookings_frame, text="Cancel", font=("Roboto", 15, "bold"), width=18, relief=RAISED,
                     command=lambda: cancel_booking((bookingId,)))
        btn.grid(column=1, row=row)
        pass
    # The above function is used to display the correct booking information and to render the form properly
    # It does this by changing the global frame value to 1 to make it render and then it uses sql to find the customer
    # details and display them in order using 'enumerate'


def dashboard_booking(customerId):
    try:
        print("func: dashboard_booking", customerId)
        make_booking()
    except Exception as e:
        print("ERROR in dashboard_booking()", e)
# the above function runs the make_booking function from sqlfunctions.py and places some information in the console for
# context


def cancel_booking_click(customerId):
    try:
        print("func: cancel_booking_click", customerId)
        cancel_booking()
    except Exception as e:
        print("error", e)
# the above function executes the cancel_booking function from sqlfunctions.py and places some key information in the
# console for context


current_user = None

# BACKGROUND SECTION
try:
    bgImage = PhotoImage(file=r'Taxi Booking System Register Background.png')
    Label(win_dash, image=bgImage).place(relwidth=1, relheight=1)
except Exception as e:
    print(e)
    messagebox.showerror('Oops!', 'Background Failed to load')
# END OF BACKGROUND SECTION

# This is the main title of the page
page_title = Label(win_dash, bg='white', width=20, text="Welcome,", font=("Roboto", 30, "bold"))
page_title.pack()

# Frames - these are essentially sections within the window

f1 = Frame(win_dash, width=600, height=200, bg='white', bd=10, )
f1.pack(pady=40)

# Buttons

btn_book = Button(f1, text="Book", font=("Roboto", 15, "bold"), width=18, relief=RAISED,
                  command=show_make_bookings)
btn_book.pack(side="left")

btn_view = Button(f1, text="View", font=("Roboto", 15, "bold"), width=18, relief=RAISED,
                  command=view_a_booking_click)

btn_view.pack(side="right")

render_make_booking()
dashboard_welcome()

# This creates the mainloop to allow for the window to run
win_dash.mainloop()
