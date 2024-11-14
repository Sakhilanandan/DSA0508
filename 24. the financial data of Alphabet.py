import matplotlib.pyplot as plt


dates = ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16']
opens = [774.25, 776.030029, 779.309998, 779.0, 779.659973]
highs = [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
lows = [769.5, 772.890015, 775.650024, 775.539978, 770.75]
closes = [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]

plt.plot(dates, opens, label='Open')
plt.plot(dates, highs, label='High')
plt.plot(dates, lows, label='Low')
plt.plot(dates, closes, label='Close')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Data of Alphabet Inc. (Oct 3 - Oct 7, 2016)')
plt.xticks(rotation=45) 
plt.legend() 

# Displaying the plot
plt.tight_layout() 
plt.show()
