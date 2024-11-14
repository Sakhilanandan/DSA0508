import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
date_range = pd.date_range(start='2024-01-01', end='2024-03-01', freq='D')
trading_volume = np.random.randint(1000000, 5000000, size=len(date_range))
stock_prices = np.random.uniform(100, 200, size=len(date_range))

df = pd.DataFrame({'Date': date_range, 'Volume': trading_volume, 'Close': stock_prices})


start_date = '2024-01-01'
end_date = '2024-03-01'
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Volume'], filtered_df['Close'], color='red')

plt.title('Trading Volume vs Stock Prices of Alphabet Inc. (Google)')
plt.xlabel('Volume')
plt.ylabel('Close Price')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
