# @Description: Handle CRUD Operations for the Expense Tracker Project
# @Author: Saloni Malhotra
# @Date: 05-07-2026

import uuid
from datetime import datetime
from data import transactions, income_Categories, expense_Categories


def add_transaction():
    """
    Collect transaction details from the user and add a new
    transaction to the expense tracker.
    """
    # transaction_id = str(uuid.uuid4()) # UUID Approach
    # max_id = max_generate_id()  # Using max()
    transaction_id = generate_id()  # Using Loop
    transaction_date = get_current_datetime()
    transaction_type = get_transaction_type()
    category = get_category(transaction_type)
    amount = get_amount()
    description = get_description()

    transactions.append(
        {
            "id": transaction_id,
            "type": transaction_type,
            "category": category,
            "description": description,
            "amount": amount,
            "date": transaction_date,
        }
    )
    print(f"\n✅ Transaction with ID {transaction_id} added successfully.\n")


def get_transaction_type():
    """
    Prompt the user to enter a valid transaction type.

    Returns:
        str: "Income" or "Expense".
    """
    while True:
        userInputType = input("Enter Type (Income/Expense): ")
        transaction_type = userInputType.strip().lower()

        if transaction_type in ("income", "expense"):
            return transaction_type.capitalize()

        print("❌ Invalid Type. Please enter either Income or Expense.")


def get_category(transaction_type):
    """
    Display categories based on the selected transaction type
    and return the selected category.

    Args:
        transaction_type (str): Income or Expense.

    Returns:
        str: Selected category.
    """

    categories = (
        income_Categories if transaction_type == "Income" else expense_Categories
    )
    while True:
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        try:
            choice = int(input(f"\nEnter your choice (1-{len(categories)}): "))

            if 1 <= choice <= len(categories):
                return categories[choice - 1]

            print("❌ Please select a valid category number.")

        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def get_amount():
    """
    Prompt the user to enter a valid transaction amount.

    Returns:
        float: A positive transaction amount.
    """
    while True:
        try:
            amount = float(input("Enter the amount "))

            if amount > 0:
                return amount

            print("❌ Please enter an amount greater than 0.")

        except ValueError:
            print("❌ Amount should be a number (e.g., 100 or 250.50).")


def get_description():
    """
    Prompt the user to enter a transaction description.

    Returns:
        str: Transaction description.
    """

    while True:
        description = input("Enter the Description ").strip()

        if description != "":
            return description

        print("❌ Description cannot be empty.")


def generate_id():
    """
    Generate the next available transaction ID
    by finding the highest existing ID.

    Returns:
        int: New transaction ID.
    """
    max_id = 0

    for transaction in transactions:
        if transaction["id"] > max_id:
            max_id = transaction["id"]

    return max_id + 1


def max_generate_id():
    """
    Generate the next transaction ID using Python's max() function.

    Returns:
        int: New transaction ID.
    """
    if not transactions:
        return 1

    max_id = max(transaction["id"] for transaction in transactions)
    return max_id + 1


def get_current_datetime():
    """
    Get the current system date.

    Returns:
        str: Current date in YYYY-MM-DD format.
    """
    return datetime.now().strftime("%Y-%m-%d")


def view_all_transactions():
    """
    Display all available transactions.
    """
    for transaction in transactions:
        print_transaction(transaction)


def get_valid_id(prompt="Enter Transaction ID: "):
    """
    Prompt the user until they enter a valid numeric transaction ID.

    Args:
        prompt (str): Message shown to the user.

    Returns:
        int: A validly-typed transaction ID (existence not yet checked).
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid numeric transaction ID.")


def view_transaction_by_id():
    """
    Display a transaction using its ID.

    Raises:
        ValueError: If the transaction ID does not exist.
    """
    view_id = get_valid_id()

    for transaction in transactions:
        if transaction["id"] == view_id:
            print_transaction(transaction)
            return

    raise ValueError(f"❌ Transaction with ID {view_id} not found.")


def delete_transaction_by_id():
    """
    Delete a transaction using its ID.

    Raises:
        ValueError: If the transaction ID does not exist.
    """
    delete_id = get_valid_id()

    for transaction in transactions:
        if transaction["id"] == delete_id:
            transactions.remove(transaction)
            print(f"✅ Transaction with ID {delete_id} deleted successfully.\n")
            view_all_transactions()
            return

    raise ValueError(f"❌ Transaction with ID {delete_id} not found.")


def calculate_total(transaction_type):
    """
    Calculate the total amount for a transaction type.

    Args:
        transaction_type (str): Income or Expense.

    Returns:
        float: Total amount.
    """
    total = 0
    for transaction in transactions:
        if transaction["type"] == transaction_type:
            total += transaction["amount"]

    return total


def show_balance():
    """
    Display total income, total expense,
    and remaining account balance.
    """
    total_income = calculate_total("Income")
    print(f"\nYour Total Income is: {format_money(total_income)}")
    
    total_expense = calculate_total("Expense")
    print(f"Your Total Expense is: {format_money(total_expense)}")
    
    remaining_balance = total_income - total_expense
    print(f"Your Remaining Balance is: {format_money(remaining_balance)}")


def format_money(amount):
    """
    Format a numeric amount into Indian currency format.

    Args:
        amount (float): Amount to format.

    Returns:
        str: Formatted currency string.
    """
    return f"₹ {amount:,}"


def print_transaction(transaction):
    """
    Display transaction details in a readable format.

    Args: transaction (dict): Transaction information.
    """
    print(f"""
    ID          : {transaction['id']}
    Type        : {transaction['type']}
    Category    : {transaction['category']}
    Description : {transaction['description']}
    Amount      : ₹{transaction['amount']}
    Date        : {transaction['date']}
    -----------------------------
    """)
