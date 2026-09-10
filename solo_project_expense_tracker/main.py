import csv 


expenses = []

is_expense = True
next_id = 1


def add_expense():
    global next_id
    print("\n ===== ADD EXPENSE =====")

    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")
    date = input("Date (YYYY-MM-DD): ")

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
                    'description' : row['description'],
                    'amount' : float(row['amount'])
                }

                expenses.append(expense)

                if expense['id'] >= next_id: 
                     next_id = expense['id'] + 1
    except FileNotFoundError: 
        print("No expense file found. Starting with empty expenses.")


def save_expense(): 
    with open('solo_project_expense_tracker/data/expenses.csv', 'w', newline="") as file:
        fieldnames = ['id', 'date', 'category', 'description', 'amount']

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)



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
            f'{expense['date']:<15}'
            f'{expense['category']:<15}'
            f'{expense['description']:<20}'
            f'P{expense['amount']:>9.2f}'
        )

    print('-' * 75)


def show_total():
    print('\n ====== YOUR TOTAL EXPENSES =======')

    total = 0

    for expense in expenses:
        total += expense['amount']

    print(f'Total: P{total:.2f}')


def spending_total():
    print('\n ====== SPENDING BY CATEGORY =======')

    if not expenses:
        print("No expense recorded yet")
        return

    category_totals = {}

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    total = 0

    for category, amount in category_totals.items():
        print(f'{category:<12} P{amount:.2f}')
        total += amount

    print('=' * 31)
    print(f"{'Total':<12} P{total:.2f}")


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


def show_menu():
    print('\n ======================')
    print("    EXPENSE TRACKER")
    print('======================')
    print('1. add expense')
    print('2. view expense')
    print('3. show total spending category')
    print('4. Delete expense')
    print('5. Exit')
    print('======================')


load_expense()

while is_expense:
    show_menu()

    choice = input("Choose: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        spending_total()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        print('\nThank you for using Expense Tracker!')
        is_expense = False
    else:
        print("\nInvalid Choice. Please try again")
