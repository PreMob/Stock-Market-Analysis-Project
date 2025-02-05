import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock ticker and the time period for analysis
ticker = 'AAPL'  # For Apple
start_date = '2020-01-01'  # Start date
end_date = '2025-01-01'    # End date

# Fetch stock data using yfinance
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Plot the stock's closing price
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label=f'{ticker} Close Price')

# Add labels and title
plt.title(f'{ticker} Stock Price Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend(loc='upper left')

# Show the plot
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
