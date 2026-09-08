import pandas as pd

df = pd.read_csv("panda/data/pokemon.csv")


print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())


# single column

print(df["Attack"].mean())
print(df['Attack'].sum())
print(df["Attack"].min())
print(df["Attack"].max())
print(df["Attack"].count())


# group by
group = df.groupby("Type 1")
print(group["Attack"].mean())
print(group["Speed"].sum())
print(group["Attack"].min())
