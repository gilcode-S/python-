import matplotlib.pyplot as plt
import numpy as np

test_scores = np.random.normal(loc=80, scale=10, size=100)
test_scores = np.clip(test_scores, 0, 100)
plt.hist(test_scores, bins=10,
         color="lightgreen",
         edgecolor='black')
plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("no of students")
plt.show()
