import pandas as pd

df = pd.read_csv("panda/data/pokemon.csv")

# filtering = keep the rows that match a condition
# speed_pokemon = df[df['Speed'] < 100]
legendary_pokemon = df[df['Legendary'] == True]
print(legendary_pokemon)
