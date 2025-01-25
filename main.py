# Personal Expense Tracker


from datetime import datetime
import csv


print("     Personal Expense Tracker    ")

meniu = ["Add payment", "Show all payments from DB", "Edit payment", "Delete payment", "Export to CSV", "Exit"]


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
        if len(istoric) == 0:
            print("There are no data to convert.")
            pass
        elif len(istoric) >= 1:
            with open(f"{username}.csv", mode='w', newline='', encoding='utf-8') as file:
                header = ["Date", "Category", "Amount", "Description"]
                content = csv.DictWriter(file, fieldnames = header)
                content.writeheader()
                content.writerows(istoric)
            print(f"The {username} file has been successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}.")



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
    else:
        print("You exit the program")
        break