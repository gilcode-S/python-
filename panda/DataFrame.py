
import pandas as pd
# dataframe = tabular data table , row , index

data = {"name": ["spongebob", 'patrick', 'squidward'],
        'age': [30, 35, 40]}


df = pd.DataFrame(data, index=['Employee 1', "Employee 2", "Employee 3"])

# add a new column
df["Job"] = ["cook", 'janitor', 'cashier']

# add new rows
new_rows = pd.DataFrame(
    [{"name": "Sandy", "age": 22, "Job": 'Engineer'},
     {"name": "Crabs", "age": 52, "Job": 'Manager'}],
    index=['Employee 4', 'Employee 5'],
)

df = pd.concat([df, new_rows])
print(df)
