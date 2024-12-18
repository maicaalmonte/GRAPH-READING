import ccxt
import pandas as pd

# Set up Binance exchange with ccxt
binance = ccxt.binance()

# Fetch historical data (e.g., 1-day candlesticks for BTC/USDT)
symbol = 'BTC/USDT'
timeframe = '1d'
limit = 100

data = binance.fetch_ohlcv(symbol, timeframe, limit=limit)

# Convert data into a pandas DataFrame for easier analysis
df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Convert timestamp to human-readable date
df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

# Display the data
print(df.head())
