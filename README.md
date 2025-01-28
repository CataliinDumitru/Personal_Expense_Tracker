# Personal_Expense_Tracker


def add_payment():

    Add a payment to the expense history and save it to a CSV file.

    This function interacts with the user to record a payment. It validates 
    the input for category and amount, saves the payment information to a 
    global history (`istoric`) and appends it to a CSV file. If the CSV file 
    doesn't exist, the function creates it and adds the appropriate headers.

    Steps:
    1. Check if the history CSV file exists. If not, create it with headers:
       ["Date", "Category", "Amount", "Description"].
    2. Prompt the user to input:
       - Category: Must contain only letters.
       - Amount: Must be a positive number.
       - Description: Optional.
    3. Append the payment details to the global `istoric` list and save 
       the record to the CSV file.
    4. Allow the user to add more payments in a loop or exit.

    Returns:
        None

    Raises:
        ValueError: If invalid data is entered for category or amount.
        Exception: For any unexpected errors during execution.

    Notes:
        - The CSV file path is currently hardcoded to 
          "/Users/catalindumitru/Personal_Expense_Tracker/history.csv".
        - The global variable `istoric` is used for storing the payments 
          in memory during runtime.


def show_payment():
    """
    Display all payments stored in the 'history.csv' file.

    This function reads data from 'history.csv' using a CSV DictReader and prints each payment's 
    details, including the date, category, amount spent, and description.
    """
    with open("history.csv", mode="r", newline="", encoding="utf-8") as f:
        data_reader = csv.DictReader(f)
        data = []
        for row in data_reader:
            data.append(row)
            print(f"{row['Date']} - {row['Category']} - {row['Amount']} - {row['Description']}")


def edit_payment():
    """
    Allow the user to edit a payment from the history.

    The function:
    1. Lists all current payments with an index.
    2. Prompts the user to select a payment to edit.
    3. Asks what aspect (category, amount, or description) they wish to change.
    4. Updates the selected value and ensures the changes are reflected in the global `istoric`.

    Raises:
        ValueError: If the user enters an invalid input during the process.
    """
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
                if istoric[0]["category"] != new_value:  # Validation block for debugging purposes
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
    """
    Delete a specific payment from the user's payment history.

    The function:
    1. Displays all payments for reference.
    2. Prompts the user to select a payment to delete by its index.
    3. Validates the input to ensure it is numeric and within range.
    4. Deletes the selected payment and updates the global `istoric`.
    """
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
    """
    Convert the user's payment history into a custom CSV file.

    This function:
    1. Prompts the user for a name to create a personalized CSV file.
    2. Checks if the global `istoric` contains data to export.
    3. Appends data to an existing file if it already exists or creates a new one.
    4. Writes payment data (date, category, amount, description) into the file.

    Raises:
        Exception: Handles unexpected errors during the process.
    """
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
            print("Your document has been updated.")
        elif len(istoric) >= 1:
            with open(file_path, mode='w', newline="", encoding='utf-8') as file:
                content = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount", "Description"])
                content.writeheader()
                content.writerows(istoric)
            print(f"The {username} file has been successfully created.")
    except Exception as e:
        print(f"An error occurred: {e}.")


def statistics():
    """
    Generate a statistical visualization of a user-selected report.

    The function:
    1. Lists all CSV files available in a specific directory.
    2. Prompts the user to select a file for visualization.
    3. Reads the selected file and extracts data for categories and amounts.
    4. Creates a pie chart to represent the distribution of spending across categories.

    Uses:
        - `matplotlib` for generating the pie chart.
        - `numpy` for numerical data processing.

    Raises:
        KeyError: If required columns ('Category', 'Amount') are missing in the CSV file.
    """
    # All the CSV files are listed for user selection
    file_path = f"/Users/catalindumitru/Personal_Expense_Tracker/"
    show_file = os.listdir(file_path)

    for index, file in enumerate(show_file, 1):
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

        # Here is where the graphic is created
    y = np.array(list(values_for_graph))
    labels = category_for_data

    fig, ax = plt.subplots()
    plt.pie(y, labels=labels)
    plt.legend()
    plt.show()