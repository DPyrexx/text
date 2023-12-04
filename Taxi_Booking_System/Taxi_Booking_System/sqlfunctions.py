# This is a file filled with all sql functions that should be needed for the entire booking system

import sqlite3
from tkinter import messagebox
import os
from sqlite3 import Error


def create_connection():
    connection = None

    try:
        connection = sqlite3.connect('taxi.db')
    except Exception as e:
        print("Connection to Database has failed!", e)

    return connection


# The above function is used to create a connection to the database which is in the root directory


def get_customer_by_id(customerId):
    # This function grabs the customers name to display on their dashboard
    conn = create_connection()
    sql = """SELECT customerId, firstname FROM Customer WHERE customerId=?"""
    cursor = conn.cursor()
    cursor.execute(sql, (customerId,))
    customer = cursor.fetchone()
    print("customer_name()", customer[1])
    conn.close()
    return customer


# Used when creating a user for the first time
def register_customer(customer):
    try:
        print(customer)
        conn = create_connection()
        cursor = conn.cursor()
        sql = '''INSERT INTO Customer(firstname, lastname, email, phoneNo, password, address, town, county, postcode,     
        cardholdername, cardnumber, EXP, CVV) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        cursor.execute(sql, customer)
        conn.commit()
        messagebox.showinfo("Account Status", "Account Created!")
        return cursor.lastrowid
    except Exception as e:
        print(e)


# Used when logging in a user for the startup page
def login(email, password):
    conn = create_connection()
    sql = """ SELECT * FROM Customer WHERE email=? AND password=? """
    cursor = conn.cursor()
    cursor.execute(sql, (email, password))
    first = cursor.fetchone()
    print("test", first[0], first[3])  # This line prints the users ID and their email
    conn.close()
    return first


# Used when making a booking
def make_booking(data):
    print(data)
    try:
        conn = create_connection()
        cur = conn.cursor()
        sql = '''INSERT INTO Booking(customerId, pickup_location, dropoff_location, date, time, status) VALUES (?,?,
        ?,?,?, "waiting dispatch") '''  # This places the values into their correct places
        cur.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Booking Status", "Booking Successful!")  # This gives confirmation of the booking
        return cur.lastrowid
    except Exception as e:
        messagebox.showerror("Booking Status", "Booking Unsuccessful!")
        print("func: make_bookings (sql)", e)


def get_booking(customerId):
    try:
        print("func: get_booking_iD")
        conn = create_connection()
        cur = conn.cursor()
        sql = '''SELECT bookingId, pickup_location, dropoff_location, date, time FROM Booking WHERE customerId=?'''
        cur.execute(sql, (customerId,))
        customer_booking = cur.fetchall()
        conn.commit()
        conn.close()
        print("bookingId = ", customer_booking)
        return customer_booking
    except Exception as e:
        print("func: get_booking_iD", e)
# The above function is used to fetch the needed information from a customers booking


def cancel_booking(data):
    try:
        conn = create_connection()
        cur = conn.cursor()
        sql = '''UPDATE customer SET status = "cancelled" WHERE bookingId = ?'''
        cur.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Cancellation Status", "Cancellation Successful")
        print("func: cancel_booking (sql)")
    except Exception as e:
        print(e)
        messagebox.showinfo("Cancellation Status", "Cancellation Unsuccessful, Please call our office 01582 123456")
# The above function is used to cancel a booking for a customer.
