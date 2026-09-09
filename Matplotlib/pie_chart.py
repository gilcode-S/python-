import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Freshmen", 'Sophomores', "Juniors", "Senior"])
values = np.array([300, 250, 270, 225])

colors = ['red', 'blue', 'yellow', 'green']

plt.pie(values, labels=categories,
        autopct="%1.1f%%",
        colors=colors,
        explode=[0, 0, 0, 0.2],
        shadow=True,
        startangle=90)


plt.title("Bro code college")
plt.show()
