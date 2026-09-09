import matplotlib.pyplot as plt
import numpy as np


x = np.array([2003, 2004, 2005, 2006])
y = np.array([15, 25, 35, 45])
y1 = np.array([16, 24, 31, 42])
y2 = np.array([1, 4, 31, 2])
line_style = dict(marker="o",
                  ms=10,
                  markerfacecolor='red',
                  markeredgecolor='red',
                  linestyle='solid',
                  linewidth=2,
                  color="blue")
plt.plot(x, y, **line_style)
plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)


plt.show()
