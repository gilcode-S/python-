import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Vegetables",
                      "Proteins", 'Diary', "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color="skyblue",)
#horizontal barh
plt.barh(categories, values, color="skyblue",
         )
plt.title("Daily Consumption")
plt.xlabel("food")
plt.ylabel("Quantity")
plt.show()
