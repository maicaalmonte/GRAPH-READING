import requests
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Fetch data from CoinGecko API for Bitcoin (BTC) in USD over the past 10 days
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {'vs_currency': 'usd', 'days': '10'}
response = requests.get(url, params=params)

# Check for errors in response
if response.status_code != 200:
    raise Exception(f"Error fetching data: {response.status_code}")

data = response.json()

# Get the prices over the past 10 days
prices = data['prices']

# Convert to DataFrame
df = pd.DataFrame(prices, columns=['timestamp', 'price'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Calculate the 10-period SMA
df['10_period_sma'] = df['price'].rolling(window=10).mean()

# Display only the last 10 rows for clarity
table_df = df.tail(10)

# Create a figure for the table
fig, ax = plt.subplots(figsize=(10, 4))  # Customize the size as needed
ax.axis('off')  # Hide the axes

# Plot the table
table_data = table(ax, table_df, loc='center', colWidths=[0.3, 0.3, 0.3])  # Adjust column widths if necessary
table_data.auto_set_font_size(False)
table_data.set_fontsize(10)
table_data.scale(1.2, 1.2)  # Scale the table for better readability

# Save the table as an image
plt.savefig("crypto_sma_table.png", bbox_inches="tight", dpi=300)

# Display the table
plt.show()
