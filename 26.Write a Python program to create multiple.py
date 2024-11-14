import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

fig, axs = plt.subplots(2)

axs[0].plot(x, y1, color='blue')
axs[1].plot(x, y2, color='red')

axs[0].set_title('Subplot 1')
axs[1].set_title('Subplot 2')

plt.show()
