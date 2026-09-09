import pandas as pd

df = pd.read_csv("solo_project_expense_tracker/data/expenses.csv")

# total_amount = df["amount"].sum()
# count_expense = df['amount'].count()
# avg_expense = df['amount'].mean()
# highest_expense = df['amount'].max()
# lowest_expense = df['amount'].min()

# print("======= Expense analysis ============= \n")
# print(f'Number of expenses : {count_expense}')
# print(f'Total spending :  ₱{total_amount}')
# print(f'Average expense :  ₱{avg_expense}')
# print(f'Highest expense :  ₱{highest_expense}')
# print(f'Lowest expense :  ₱{lowest_expense}')


# category_totals = df.groupby(
#     'category')['amount'].sum().sort_values(ascending=False)

# category_percentage = (category_totals / total_amount) * 100
# print('\n======== Spending by category =========\n')
# print(category_totals)
# print(category_percentage)


# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Calculate total spending per month
monthly_spending = df.groupby(
    df['date'].dt.to_period('M')
)['amount'].sum()
monthly_spending.index = monthly_spending.index.to_timestamp()

# highest_index = df['amount'].idxmax() # print the entire row base on index ID
# highest_expense = df.loc[highest_index]
print(monthly_spending)
