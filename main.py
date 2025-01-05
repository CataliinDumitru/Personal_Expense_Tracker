# Personal Expense Tracker

import sqlite3
from datetime import datetime


print("     Personal Expense Tracker    ")

meniu = ["Add payment", "Show all payments from DB", "Edit payment", "Delete payment"]


date_time = datetime.now()

istoric = []


def add_payment():
    global istoric
    category = input("Category (Food, Health, Lifestyle, Hobby, Other)\n")
    ammount = input("Ammount of money spend\n")
    description = input("Description (Optional)")
    any_options = input("Add another payment? Y/N\n")
    if any_options == "N".lower():
        istoric.append(print(f"{date_time}. A payment of {ammount}$ was registred in the {category} category. "))

    return

def show_payment():
    global istoric
    if istoric
    x = 0
    for element in istoric:
        print(f"{x}. {element}")
    return


while True:

    x = 0
    print()
    for element in meniu:
        x += 1
        print(f"{x}. {element}")

    start = input("What do you like to do?\n")


    if start == 1 or meniu[0]:
        add_payment()
    elif start == 2 or meniu[1]:
        show_payment()