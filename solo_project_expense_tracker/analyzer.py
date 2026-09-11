import pandas as pd
import matplotlib.pyplot as plt




def analyze_expenses(expenses):
    df = pd.DataFrame(expenses)

    basic_analysis(df)
    category_analysis(df)
    daily_analysis(df)
    create_charts(df)


def basic_stats(df):

    if df.empty:
        return

    total_amount = df["amount"].sum()
    count_expense = df['amount'].count()
    avg_expense = df['amount'].mean()
    highest_expense = df['amount'].max()
    lowest_expense = df['amount'].min()

    return {
        "total_amount": total_amount,
        "count_expense": count_expense,
        'avg_expense': avg_expense,
        'highest_expense': highest_expense,
        'lowest_expense': lowest_expense
    }


def basic_analysis(df):

    stats = basic_stats(df)

    if stats is None:
        return

    total_amount = stats['total_amount']
    count_expense = stats['count_expense']
    avg_expense = stats['avg_expense']
    highest_expense = stats['highest_expense']
    lowest_expense = stats['lowest_expense']

    print("======= Expense analysis ============= \n")
    print(f'Number of expenses : {count_expense}')
    print(f'Total spending: ₱{total_amount:.2f}')
    print(f'Average expense: ₱{avg_expense:.2f}')
    print(f'Highest expense: ₱{highest_expense:.2f}')
    print(f'Lowest expense: ₱{lowest_expense:.2f}')


def category_stats(df):

    if df.empty:
        return None

    category_count = df["category"].value_counts()
    category_spending = df.groupby("category")["amount"].sum()
    highest_category = category_spending.idxmax()
    highest_amount = category_spending.loc[highest_category]
    total_amount = df["amount"].sum()
    category_percentage = (category_spending / total_amount) * 100
    highest_percentage = category_percentage.loc[highest_category]

    return {
        "category_count": category_count,
        "category_spending": category_spending,
        "highest_category": highest_category,
        "highest_amount": highest_amount,
        'category_percentage': category_percentage,
        'highest_percentage': highest_percentage,
    }


def category_analysis(df):
    print("\n====== Category Count =====\n")
    stats = category_stats(df)

    if stats is None:
        print("No expense to analyze")
        return

    category_count = stats["category_count"]
    category_spending = stats["category_spending"]
    for category, count in category_count.items():
        if count > 1:
            print(f'{category} : {count} transactions')
        else:
            print(f"{category} : {count} transaction")

    print("\n====== Category Amount =====\n")
    for category, amount in category_spending.items():
        print(f"{category}: P{amount:.2f}")

    highest_category = stats['highest_category']
    highest_amount = stats['highest_amount']

    print("\n====== Spending Insights ======")
    print(f'highest spending category : {highest_category}')
    print(f"Amount spent: P{highest_amount:.2f}")

    print("\n====== Spending Percentage ======\n")

    category_percentage = stats['category_percentage']
    highest_percentage = stats['highest_percentage']
    for category, percentage in category_percentage.items():
        print(f'{category} : {percentage:.2f}%')

    print("\n====== Spending Insights ======\n")
    print(f'Your highest spending category is {highest_category}.')
    print(f"You spent P{highest_amount:.2f} on {highest_category}.")
    print(
        f'That represents {highest_percentage:.2f}% of your total spending.\n')


def daily_stats(df):

    if df.empty:
        return None
    df['date'] = pd.to_datetime(df['date'])
    daily_spending = df.groupby(
        df['date'].dt.to_period('D')
    )['amount'].sum()

    return {
        'daily_spending': daily_spending
    }


def daily_analysis(df):
    stats = daily_stats(df)
    if stats is None:
        print('No expense to analyze')
        return
    daily_spending = stats['daily_spending']

    print('\n====== Daily Spending =====\n')
    for date, amount in daily_spending.items():
        print(f"{date}: ₱{amount:.2f}")


def chart_stats(df):
    if df.empty:
        return None
    category_totals = df.groupby("category")['amount'].sum()

    return {
        'category_totals': category_totals
    }


def create_charts(df):

    stats = chart_stats(df)
    if stats is None:
        print("No expense to analyze")
        return
    category_totals = stats['category_totals']
    plt.barh(category_totals.index, category_totals.values)
    plt.title("Spending by Category")
    plt.ylabel("Category")
    plt.xlabel("Spending (₱)")
    plt.tight_layout()
    plt.show()
