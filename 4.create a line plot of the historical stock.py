import yfinance as yf
import matplotlib.pyplot as plt

ticker_symbol = 'GOOGL'

start_date = '2024-01-01'
end_date = '2024-03-01'

data = yf.download(ticker_symbol, start=start_date, end=end_date)

plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], marker='o', linestyle='-')

plt.title('Historical Stock Prices of Alphabet Inc. (Google)')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
