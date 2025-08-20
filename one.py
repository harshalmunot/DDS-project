import json
from datetime import datetime
import os

# --------------------------
# Data Structures
# --------------------------
transactions = []

# Each transaction:
# {
#     "date": "2025-08-15",
#     "type": "income" or "expense",
#     "category": "Food",
#     "amount": 150.0,
#     "description": "Grocery shopping"
# }

# --------------------------
# Functions
# --------------------------

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    type_ = input("Enter type (income/expense): ").lower()
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    transaction = {
        "date": date,
        "type": type_,
        "category": category,
        "amount": amount,
        "description": description
    }

    transactions.append(transaction)
    print("Transaction added.\n")


def save_to_file(filename="transactions.json"):
    with open(filename, "w") as f:
        json.dump(transactions, f, indent=4)
    print("Data saved to file.\n")


def load_from_file(filename="transactions.json"):
    global transactions
    if os.path.exists(filename):
        with open(filename, "r") as f:
            transactions = json.load(f)
        print("Data loaded from file.\n")
    else:
        print("File not found. Starting with empty transaction list.\n")


def show_transactions():
    if not transactions:
        print("No transactions to show.\n")
        return
    for t in transactions:
        print(t)
    print()


def filter_expenses_over(amount=100):
    filtered = [t for t in transactions if t['type'] == 'expense' and t['amount'] > amount]
    if not filtered:
        print("No expenses over the specified amount.\n")
        return
    for t in filtered:
        print(t)
    print()


def search_by_category(keyword):
    found = [t for t in transactions if keyword.lower() in t['category'].lower()]
    if not found:
        print("No transactions found for that category.\n")
        return
    for t in found:
        print(t)
    print()


def sort_by_amount():
    if not transactions:
        print("No transactions to sort.\n")
        return
    sorted_txns = sorted(transactions, key=lambda x: x['amount'], reverse=True)
    for t in sorted_txns:
        print(t)
    print()


def display_ascii_bar_chart():
    monthly_spending = {}
    for t in transactions:
        if t['type'] == 'expense':
            month = t['date'][:7]  # YYYY-MM
            monthly_spending[month] = monthly_spending.get(month, 0) + t['amount']

    if not monthly_spending:
        print("No spending data to display.\n")
        return

    print("\nMonthly Spending Chart:")
    for month, total in sorted(monthly_spending.items()):
        bar = "#" * int(total / 10)
        print(f"{month}: {bar} ${total:.2f}")
    print()

# --------------------------
# Main Loop
# --------------------------

def main():
    load_from_file()

    while True:
        print("1. Add Transaction")
        print("2. Show All Transactions")
        print("3. Filter Expenses Over $100")
        print("4. Search by Category")
        print("5. Sort by Amount (Descending)")
        print("6. Display ASCII Bar Chart")
        print("7. Save to File")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            filter_expenses_over()
        elif choice == "4":
            keyword = input("Enter category to search: ")
            search_by_category(keyword)
        elif choice == "5":
            sort_by_amount()
        elif choice == "6":
            display_ascii_bar_chart()
        elif choice == "7":
            save_to_file()
        elif choice == "8":
            save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
