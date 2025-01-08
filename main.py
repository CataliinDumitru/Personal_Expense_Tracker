# Personal Expense Tracker

import sqlite3
from datetime import datetime
from logging import ERROR

print("     Personal Expense Tracker    ")

meniu = ["Add payment", "Show all payments from DB", "Edit payment", "Delete payment", "Exit"]


date_time = datetime.now().strftime("%Y-%m-%d %H:%M")

istoric = []


def add_payment():
    """Add a payment and return the info of the payment"""
    global istoric

    while True:
        try:
            # Validare pentru categorie
            while True:
                category = input("Category (Food, Health, Lifestyle, Hobby, Other)\n")
                if not category.isalpha():  # Verificare dacă inputul conține doar litere
                    print("This section takes only letters. Please try again.")
                else:
                    break

            # Validare pentru sumă
            while True:
                ammount = input("Amount of money spent\n")
                try:
                    ammount = float(ammount)  # Conversie în float pentru valori zecimale
                    if ammount <= 0:
                        print("The amount must be greater than 0. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid numeric value. E.g., 10.50, 20, 3.50")

            # Descrierea este opțională
            description = input("Description (Optional)\n")

            # Crearea informației despre plată
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            payment_info = {
                "date": date_time,
                "category": category,
                "amount": ammount,
                "description": description
            }

            # Adăugarea în istoric
            istoric.append(payment_info)

            # Afișarea plății salvate
            payment_info_str = f"<<< {date_time} - {category} - {ammount} - {description} >>>"
            print(f"Payment saved: {payment_info_str}")

            # Întreabă utilizatorul dacă dorește să adauge o altă plată
            any_options = input("Add another payment? Y/N\n").lower()
            if any_options == "n":
                break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return

def show_payment():
    global istoric

    x = 0
    for element in istoric:
        x += 1
        print(f"{x}. {element}")
    return



def edit_payment():
    """This function select the payment that the user want to edit and modify the category, ammount of money spent and the description."""
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
                print(istoric)
                new_value = input("Enter the new value:\n")
                istoric[0]["category"] = new_value
                if istoric[0]["category"] != new_value:  # Here is a caution code block to test the code functionality
                    print("There was a problem during the process.")
                else:
                    print("New value saved")
            elif what_to_edit == "money spend":
                new_value1 = input("Enter the new value:\n")
                istoric[0]["amount"] = new_value1
            else:
                new_value2 = input("Enter the new value:\n")
                istoric[0]["description"] = new_value2
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
    else:
        print("You exit the program")
        break