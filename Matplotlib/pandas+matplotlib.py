import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('panda/data/pokemon.csv')


type_count = df["Type 1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values,
         color='skyblue', edgecolor="black")
plt.title("Number of pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.show()
