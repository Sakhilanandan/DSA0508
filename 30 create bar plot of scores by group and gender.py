import matplotlib.pyplot as plt
import numpy as np

# Sample data
men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']

bar_width = 0.35

x = np.arange(len(labels))

plt.bar(x - bar_width/2, men_means, bar_width, label='Men')
plt.bar(x + bar_width/2, women_means, bar_width, label='Women')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, labels)  
plt.legend()

plt.tight_layout()
plt.show()
