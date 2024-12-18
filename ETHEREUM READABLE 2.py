import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import ccxt
import time

# Define the function to fetch data with retries
def fetch_data_with_retry(exchange, symbol, timeframe, limit=100):
    retries = 5
    for attempt in range(retries):
        try:
            data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            return data
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                print("Max retries reached for fetching data.")
                return None

# Function to update the plot
def update_plot(i, df, ax, exchange, symbol, timeframe):
    data = fetch_data_with_retry(exchange, symbol, timeframe, limit=100)
    if data:
        new_df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        new_df['date'] = pd.to_datetime(new_df['timestamp'], unit='ms')

        # Update the plot
        df = new_df
        ax.clear()

        # Plot the close price
        ax.plot(df['date'], df['close'], label='Close Price', color='blue')

        # Plot the moving average (10-period)
        df['SMA'] = df['close'].rolling(window=10).mean()
        ax.plot(df['date'], df['SMA'], label='10-period SMA', color='orange', linestyle='--')

        # Highlight the last closing price
        last_close = df['close'].iloc[-1]
        ax.annotate(f"Last Close: {last_close:.2f} USDT",
                    xy=(df['date'].iloc[-1], last_close),
                    xytext=(df['date'].iloc[-5], last_close + 50),
                    arrowprops=dict(facecolor='green', shrink=0.05))

        # Add titles and labels
        ax.set_title(f'{symbol} Price (Real-time updates)', fontsize=14)
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Price (USDT)', fontsize=12)

        # Display high and low prices as annotations
        high_price = df['high'].max()
        low_price = df['low'].min()
        ax.annotate(f"High: {high_price:.2f} USDT",
                    xy=(df['date'][df['high'].idxmax()], high_price),
                    xytext=(df['date'][df['high'].idxmax() - 5], high_price + 50),
                    arrowprops=dict(facecolor='red', shrink=0.05))
        ax.annotate(f"Low: {low_price:.2f} USDT",
                    xy=(df['date'][df['low'].idxmin()], low_price),
                    xytext=(df['date'][df['low'].idxmin() - 5], low_price - 50),
                    arrowprops=dict(facecolor='purple', shrink=0.05))

        # Add a grid for better readability
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

        # Rotate x-axis labels for better readability
        ax.tick_params(axis='x', rotation=45)

        # Display a legend
        ax.legend()

# Plot real-time data
def plot_realtime_data(exchange_name, symbol, timeframe):
    # Initialize the exchange object using ccxt
    exchange = getattr(ccxt, exchange_name)()  # Dynamically load the exchange class
    fig, ax = plt.subplots(figsize=(10, 6))
    ani = animation.FuncAnimation(fig, update_plot, fargs=(pd.DataFrame(), ax, exchange, symbol, timeframe),
                                  interval=60000)  # Update every 60 seconds (1 minute)
    plt.tight_layout()
    plt.show()

# Example usage for Ethereum
plot_realtime_data('kraken', 'ETH/USDT', '1m')  # Use 'ETH/USD' if preferred
