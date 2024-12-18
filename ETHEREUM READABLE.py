import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import ccxt
import time


class RealTimePlot:
    def __init__(self, exchange_name, symbol, timeframe):
        self.exchange = getattr(ccxt, exchange_name)()
        self.symbol = symbol
        self.timeframe = timeframe
        self.df = pd.DataFrame()

    def fetch_data_with_retry(self, limit=100):
        retries = 5
        for attempt in range(retries):
            try:
                data = self.exchange.fetch_ohlcv(self.symbol, timeframe=self.timeframe, limit=limit)
                return data
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print("Max retries reached for fetching data.")
                    return None

    def update_plot(self, i, ax):
        data = self.fetch_data_with_retry(limit=100)
        if data:
            new_df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            new_df['date'] = pd.to_datetime(new_df['timestamp'], unit='ms')

            # Append new data while avoiding duplicates
            self.df = pd.concat([self.df, new_df]).drop_duplicates(subset='timestamp').reset_index(drop=True)

            ax.clear()

            # Plot the close price
            ax.plot(self.df['date'], self.df['close'], label='Close Price', color='blue')

            # Highlight the last closing price
            last_close = self.df['close'].iloc[-1]
            ax.annotate(f"Last Close: {last_close:.2f} USD",
                        xy=(self.df['date'].iloc[-1], last_close),
                        xytext=(self.df['date'].iloc[-5], last_close + 50),
                        arrowprops=dict(facecolor='green', shrink=0.05))

            # Add titles and labels
            ax.set_title(f'{self.symbol} Price (Real-time updates)', fontsize=14)
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel('Price (USD)', fontsize=12)

            # Show high and low prices as annotations
            high_price = self.df['high'].max()
            low_price = self.df['low'].min()
            ax.annotate(f"High: {high_price:.2f} USD",
                        xy=(self.df['date'][self.df['high'].idxmax()], high_price),
                        xytext=(self.df['date'][self.df['high'].idxmax() - 5], high_price + 50),
                        arrowprops=dict(facecolor='red', shrink=0.05))
            ax.annotate(f"Low: {low_price:.2f} USD",
                        xy=(self.df['date'][self.df['low'].idxmin()], low_price),
                        xytext=(self.df['date'][self.df['low'].idxmin() - 5], low_price - 50),
                        arrowprops=dict(facecolor='purple', shrink=0.05))

            # Rotate x-axis labels for better readability
            ax.tick_params(axis='x', rotation=45)

    def plot_realtime_data(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        ani = animation.FuncAnimation(fig, self.update_plot, fargs=(ax,), interval=60000)  # Update every 60 seconds
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Fetch data for Ethereum (ETH) against USD on Kraken
    plotter = RealTimePlot('kraken', 'ETH/USD', '1m')  # For Ethereum
    plotter.plot_realtime_data()
