import pandas as pd


df = pd.read_csv('panda/data/pokemon.csv')

# drop
# df = df.drop(columns=['Legendary'])

# 2. handle missing data
# df = df.dropna(subset=['Type 2'])
# df = df.fillna({"Type 2": "None"})


# 3. fix incosistent value

# df['Type 1'] = df['Type 1'].replace({"Grass": "GRASS"})


# 4. standarize text
# df["Name"] = df["Name"].str.lower()

# 5. fix data type
# df["Legendary"] = df["Legendary"].astype(bool)


# 6 duplicated  
df = df.drop_duplicates()
print(df)
