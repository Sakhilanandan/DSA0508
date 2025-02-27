import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]


plt.plot(x, y1, label='Line 1', color='blue', linewidth=2)
plt.plot(x, y2, label='Line 2', color='red', linewidth=3)

plt.legend()

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines Plot')

plt.show()
