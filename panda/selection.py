import pandas as pd


df = pd.read_csv("panda/data/pokemon.csv", index_col="Name")

# selection by column
# print(df["Name"])


# selectio by row
# print(df.loc["Charizard":"Blastoise", ["Attack", "HP"]])
# integer base row

# print(df.iloc[0:11:2, 0:3])


#simple exercise 
# where the user input a pokemon to search

pokemon = input("Enter a pokemon name: ")

try: 
    print(df.loc[pokemon])
except KeyError:
    print(f'{pokemon} not found')