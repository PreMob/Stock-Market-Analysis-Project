import matplotlib.pyplot as plt
import numpy as np

# Generate random data for multiple stock lines over a period of 30 days (1 month)
days = np.arange(1, 31)
stock1 = np.random.uniform(10, 50, size=30).cumsum() / 10
stock2 = np.random.uniform(15, 55, size=30).cumsum() / 10
stock3 = np.random.uniform(5, 40, size=30).cumsum() / 10

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(days, stock1, color="turquoise", marker="o", markersize=4, label="Stock 1")
plt.plot(days, stock2, color="violet", marker="o", markersize=4, label="Stock 2")
plt.plot(days, stock3, color="lightgreen", marker="o", markersize=4, label="Stock 3")

# Add labels and grid
plt.xlabel("Day")
plt.ylabel("Stock Price")
plt.title("Stock Market Simulation Over 1 Month")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()

# Set a dark background to resemble a trading platform style
plt.style.use("dark_background")

# Display the plot
plt.show()
