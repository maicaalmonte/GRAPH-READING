import requests
import pandas as pd

# Fetch data from CoinGecko API for Bitcoin (BTC) in USD over the past 10 days
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {'vs_currency': 'usd', 'days': '10'}
response = requests.get(url, params=params)
data = response.json()

# Get the prices over the past 10 days
prices = data['prices']

# Convert to DataFrame
df = pd.DataFrame(prices, columns=['timestamp', 'price'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Display the data
print(df)
