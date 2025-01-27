# Personal Expense Tracker
import os.path
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import numpy as np


print("     Personal Expense Tracker    ")

meniu = ["Add payment", "Show all payments", "Edit payment", "Delete payment", "Export to CSV", "Statistics", "Exit"]

date_time = datetime.now().strftime("%Y-%m-%d %H:%M")

istoric = []

def add_payment():
    """Add a payment and return the info of the payment"""
    global istoric

    file_path_history = "/Users/catalindumitru/Personal_Expense_Tracker/history.csv"
    if os.path.exists(file_path_history):
        pass
    else:
        with open("history.csv", mode="w", newline="", encoding="utf-8") as data:
            history_data = csv.DictWriter(data, fieldnames=["Date", "Category", "Amount", "Description"])
            history_data.writeheader()


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
                amount = input("Amount of money spent\n")
                try:
                    amount = float(amount)  # Conversie în float pentru valori zecimale
                    if amount <= 0:
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
                "Date": date_time,
                "Category": category,
                "Amount": amount,
                "Description": description
            }

            # Adăugarea în istoric
            istoric.append(payment_info)

            # Afișarea plății salvate
            payment_info_str = f"<<< {date_time} - {category} - {amount} - {description} >>>"
            print(f"Payment saved: {payment_info_str}")

            with open(file_path_history, mode="a", newline="", encoding="utf-8") as data:
                data_to_append = csv.DictWriter(data, fieldnames=["Date", "Category", "Amount", "Description"])
                data_to_append.writerows(istoric)


            # Întreabă utilizatorul dacă dorește să adauge o altă plată
            any_options = input("Add another payment? Y/N\n").lower()
            if any_options == "n":
                break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return

def show_payment():
    with open("history.csv", mode="r", newline="", encoding="utf-8") as f:
        data_reader = csv.DictReader(f)
        data = []
        for row in data_reader:
            data.append(row)
            print(f"{row['Date']} - {row['Category']} - {row['Amount']} - {row['Description']}")


def edit_payment():
    """This function select the payment that the user want to edit and modify the category, amount of money spent and the description."""
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
        print("That's not a valid value!")



def delete():
    global istoric

    for payment in istoric:
        print(payment)

    while True:
        delete_payment = input("What payment do you want to delete?\n")
        if not delete_payment.isdigit():
            print("You need to enter only numbers.")
        elif int(delete_payment) > len(istoric):
            print("This number is out of range.")
        else:
            break

    if istoric[int(delete_payment) - 1]:
        print(f"<<< {istoric[int(delete_payment) -1]} >>> was selected and successfully deleted!")
        del istoric[int(delete_payment) - 1]




def to_CSV():
    '''This function convert into a custom CSV file the history of the user payments.'''
    global istoric
    try:
        username = input("Enter your name:\n")
        file_path = f"/Users/catalindumitru/Personal_Expense_Tracker/{username}.csv"
        if len(istoric) == 0:
            print("There are no data to convert.")
            pass
        elif os.path.exists(file_path):
            with open(file_path, mode="a", newline="", encoding='utf-8') as existing_file:
                existing_data = csv.DictWriter(existing_file, fieldnames=["Date", "Category", "Amount", "Description"])
                existing_data.writerows(istoric)
            print("You document has been updated.")
        elif len(istoric) >= 1:
            with open(file_path, mode='w', newline="", encoding='utf-8') as file:
                content = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount", "Description"])
                content.writeheader()
                content.writerows(istoric)
            print(f"The {username} file has been successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}.")


def statistics():  #TODO Maine trebuie sa termin toata functia
    '''This function generates a statistical visualisation of a report that the user choose'''

    #All the CSV file are list in the GUI and the user pick from one of them
    file_path = f"/Users/catalindumitru/Personal_Expense_Tracker/"
    show_file = os.listdir(file_path)

    for file in show_file:
        index = 0
        index += 1
        if file.endswith(".csv"):
            print(f"{index}. {file}")

    graph_rep = input("For which report do you need a graphic representation?\n").lower()

    with open(f"{graph_rep}.csv", mode="r", newline="", encoding="utf-8") as data:
        csv_reader = csv.DictReader(data)
        stored_data = []
        for row in csv_reader:
            stored_data.append(row)

        category_for_data = []
        values_for_graph = []
        for value in stored_data:
            values_for_graph.append(value["Amount"])
            category_for_data.append(value["Category"])

        #Here is where the graphic it's created
    y = np.array(list(values_for_graph))
    labels = category_for_data

    fig, ax = plt.subplots()
    plt.pie(y, labels=labels)
    plt.legend()
    plt.show()


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
    elif start == "4":
        delete()
    elif start == "5":
        to_CSV()
    elif start == "6":
        statistics()
    else:
        print("You exit the program")
        break

