import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("solo_project_expense_tracker/data/expenses.csv")\

category_count = df["category"].value_counts()
category_spending = df.groupby("category")["amount"].sum()

df['date'] = pd.to_datetime(df['date'])
daily_spending = df.groupby(
    df['date'].dt.to_period('D')
)['amount'].sum()


print('\n====== Daily Spending =====\n')
for date, amount in daily_spending.items():
    print(f"{date}: {amount:.2f}")


print("\n====== Category Count =====\n")
for category, count in category_count.items():
    if count > 1:
        print(f'{category} : {count} transactions')
    else:
        print(f"{category} : {count} transaction")

print("\n====== Category Amount =====\n")
for category, amount in category_spending.items():
    print(f"{category}: P{amount:.2f}")


# print("====== Category Analysis ======")
# print("\nNumber of Transactions")
# print(category_count)

# print("\nTotal spending:")
# print(category_spending)


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
# df['date'] = pd.to_datetime(df['date'])

# Calculate total spending per month
# day_spending = df.groupby(
#     df['date'].dt.to_period('D')
# )['amount'].sum()
# day_spending.index = day_spending.index.to_timestamp()

# highest_index = df['amount'].idxmax() # print the entire row base on index ID
# highest_expense = df.loc[highest_index]

# matplot
# category_totals = df.groupby("category")['amount'].sum()
# plt.barh(category_totals.index, category_totals.values)
# plt.title("Spending by Category")
# plt.ylabel("Category")
# plt.xlabel("Spending (₱)")
# plt.tight_layout()
# plt.show()
