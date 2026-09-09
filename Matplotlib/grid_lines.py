import matplotlib.pyplot as plt
import numpy as np

# grid () helps make plots easier to read by adding refernece lines

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 30]

# create grid lines
# single axis
plt.grid(axis='y', linewidth=3,
         color="lightgray",
         linestyle="dashed")

plt.plot(x, y)
plt.show()
