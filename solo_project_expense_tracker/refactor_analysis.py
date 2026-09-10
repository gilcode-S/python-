import pandas as pd
import analyzer
import manager_expense

manager_expense.load_expense()


def show_menu():
    print('\n ======================')
    print("    EXPENSE TRACKER")
    print('======================')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Delete Expenses')
    print('4. Analyze Expenses')
    print('5. Exit')


while True:
    show_menu()
    choice = input("Choose: ")

    if choice == '1':
        manager_expense.add_expense()

    elif choice == '2':
        manager_expense.view_expenses()
    elif choice == '3':
        manager_expense.delete_expense()
    elif choice == '4':
        df = pd.DataFrame(manager_expense.expenses)

        analyzer.basic_analysis(df)
        analyzer.category_analysis(df)
        analyzer.daily_analysis(df)
        analyzer.create_charts(df)

    elif choice == '5':
        print('\nThank you for using Expense Tracker!')
        break

    else:
        print("\nInvalid Choice. Please try again")
