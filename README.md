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

