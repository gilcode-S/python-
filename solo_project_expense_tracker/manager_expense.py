import csv
from datetime import datetime

expenses = []
next_id = 1


def get_valid_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_valid_text(prompt):
    while True:
        text = input(prompt)
        if not text.strip():
            print("This field cannot be empty")
            continue
        return text


def get_valid_date():
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def add_expense():
    global next_id
    print("\n ===== ADD EXPENSE =====")

    amount = get_valid_amount()
    category = get_valid_text("Category: ")
    description = get_valid_text("Description: ")
    date = get_valid_date()
    expense = {
        "id": next_id,
        'amount': amount,
        'category': category,
        'description': description,
        'date': date
    }

    expenses.append(expense)
    next_id += 1
    save_expense()
    print("\n Expense added Successfully")


def save_expense():
    with open('solo_project_expense_tracker/data/expenses.csv', 'w', newline="") as file:
        fieldnames = ['id', 'date', 'category', 'description', 'amount']

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)


def load_expense():
    global next_id

    try:
        with open('solo_project_expense_tracker/data/expenses.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = {
                    'id': int(row['id']),
                    'date': row['date'],
                    'category': row['category'],
                    'description': row['description'],
                    'amount': float(row['amount'])
                }

                expenses.append(expense)

                if expense['id'] >= next_id:
                    next_id = expense['id'] + 1
    except FileNotFoundError:
        print("No expense file found. Starting with empty expenses.")


def view_expenses():
    print('\n ====== YOUR EXPENSE =======')

    if not expenses:
        print("No expense recorded yet. ")
        return

    print("-" * 75)
    print(f'{'ID':<5}{'DATE':<15}{'CATEGORY':<15}{'DESCRIPTION':<20} P{'AMOUNT':>}')
    print('-' * 75)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<20}"
            f"P{expense['amount']:>9.2f}"
        )

    print('-' * 75)


def delete_expense():
    print('\n ====== DELETE EXPENSE =======')

    if not expenses:
        print("No expense recorded yet.")
        return

    try:
        expense_id = int(input("\nEnter the ID of the expense to delete: "))

        for expense in expenses:
            if expense['id'] == expense_id:
                expenses.remove(expense)
                save_expense()
                print("\nExpense deleted successfully")
                return

        print(
            "\nInvalid ID not found"
        )
    except ValueError:
        print('\nInvalid ID. Please enter a number.')
