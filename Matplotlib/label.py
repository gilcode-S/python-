import matplotlib.pyplot as plt
import numpy as np


x = np.array([2003, 2004, 2005, 2006])
y = np.array([15, 25, 35, 45])
y1 = np.array([16, 24, 31, 42])
y2 = np.array([1, 4, 31, 2])


plt.title("Class size", fontsize=25,
          family="Arial",
          fontweight='bold',
          color="red",
          )

plt.xlabel("YEAR", fontsize=20,
           family="Arial",
           fontweight='bold',
           color="green")


plt.ylabel("students", fontsize=20,
           family="Arial",
           fontweight='bold',
           color="green")


plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.tick_params(axis="both", colors="yellow")
plt.xticks(x)
plt.show()
