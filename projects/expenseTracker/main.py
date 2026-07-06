# @Description: Main File for Expense Tracker Project
# @Author: Saloni Malhotra
# @Date: 05-07-2026

from operations import (
    add_transaction,
    view_all_transactions,
    view_transaction_by_id,
    delete_transaction_by_id,
    show_balance,
)

while True:
    print("""
    ====== Personal Expense Tracker ======

    1. View All Transactions
    2. View Transaction By ID
    3. Add Transaction
    4. Delete Transaction By ID
    5. Show Balance
    6. Exit

    ======================================
    """)
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("===== Viewing all Transaction =====")
            view_all_transactions()

        elif choice == 2:
            print("===== View Transaction By Id =====")
            view_transaction_by_id()

        elif choice == 3:
            print("===== Add New Transaction =====")
            add_transaction()

        elif choice == 4:
            print("===== Delete Transaction =====")
            delete_transaction_by_id()

        elif choice == 5:
            print("===== Show Balance =====")
            show_balance()

        elif choice == 6:
            print("👋 Thank you for using Personal Expense Tracker!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.\n")

    except ValueError:
        print("❌ Please enter a valid number between 1 and 6.\n")
