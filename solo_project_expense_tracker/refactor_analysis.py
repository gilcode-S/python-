
import analyzer
import manager_expense

manager_expense.load_expense()


def show_menu():
    print('\n ======================')
    print("    EXPENSE TRACKER")
    print('======================')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Edit Expenses')
    print('4. Delete Expenses')
    print('5. Analyze Expenses')
    print('6. Exit')


while True:
    show_menu()
    choice = input("Choose: ")

    if choice == '1':
        manager_expense.add_expense()

    elif choice == '2':
        
        manager_expense.view_expenses()
    elif choice == '3':
        manager_expense.edit_expense()
    elif choice == '4':
        manager_expense.delete_expense()
    elif choice == '5':
        analyzer.analyze_expenses(manager_expense.expenses)

    elif choice == '6':
        print('\nThank you for using Expense Tracker!')
        break

    else:
        print("\nInvalid Choice. Please try again")
