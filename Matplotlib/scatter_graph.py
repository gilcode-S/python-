import matplotlib.pyplot as plt
import numpy as np


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([55, 12, 79, 87, 76, 5, 66, 55, 77, 88, 90])
x1 = np.array([0, 1, 2, 2, 4, 4, 6, 5, 7, 8, 1])
y2 = np.array([51, 11, 76, 83, 77, 57, 63, 55, 74, 81, 95])

plt.scatter(x, y, color="skyblue",
            alpha=0.5,
            s=200,
            label="Class A")

plt.scatter(x1, y2, color="red",
            alpha=0.5,
            s=200,
            label="Class B")
plt.title("TEST Scores")
plt.xlabel("Hours Studies")
plt.ylabel("Grade")

plt.legend()
plt.show()
