# Personal Expense Tracker

import sqlite3
from datetime import datetime
from os import execle
from types import new_class
from unicodedata import category

print("     Personal Expense Tracker    ")

meniu = ["Add payment", "Show all payments from DB", "Edit payment", "Delete payment"]


date_time = datetime.now().strftime("%Y-%m-%d %H:%M")

istoric = []


def add_payment():
    """Add a payment and return the info of the payment"""
    global istoric
    while True:
        category = input("Category (Food, Health, Lifestyle, Hobby, Other)\n")
        ammount = input("Ammount of money spend\n")
        description = input("Description (Optional)\n")

        payment_info = payment_info = {
            "date": date_time,
            "category": category,
            "amount": ammount,
            "description": description
        }

        print(f"Payment saved: {payment_info}")
        any_options = input("Add another payment? Y/N\n").lower()
        istoric.append(payment_info)
        if any_options == "n":
            break
        else:
            continue

    return

def show_payment():
    global istoric

    x = 0
    for element in istoric:
        x += 1
        print(f"{x}. {element}")
    return



def edit_payment():
    global istoric
    x = 0
    for element in istoric:
        x += 1
        print(f"{x}. {element}")

    edit_payment = int(input("What payment do you wanna edit?\n"))
    try:
        if istoric[edit_payment - 1]:
            print(f"<<< {istoric[edit_payment -1]} >>> was selected")
            what_to_edit = input("What do you wanna change? (Category, money spend or description)\n").lower()
            if what_to_edit == "category":
                new_value = input("Enter the new value:\n")
                istoric[1]["category"] = new_value
            elif what_to_edit == "money spend":
                new_value1 = input("Enter the new value:\n")
                istoric[2]["amount"] = new_value1
            else:
                new_value2 = input("Enter the new value:\n")
                istoric[3]["description"] = new_value2
    except ValueError:
        print("Thats not a valid value!")



while True:

    x = 0
    print()
    for element in meniu:
        x += 1
        print(f"{x}. {element}")

    start = input("What do you like to do?\n")


    if start == "1":
        add_payment()
    elif start == "2":
        show_payment()
    elif start == "3":
        edit_payment()
