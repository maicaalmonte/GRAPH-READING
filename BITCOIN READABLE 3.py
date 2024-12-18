import ccxt  # Import ccxt for exchange interactions
import pandas as pd  # Import pandas for data handling
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time  # Import time for sleep functionality
import webbrowser  # Import webbrowser to open the file in the default browser
import os  # Import os for file path management


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


# Plot real-time data with Plotly for better interactivity
def plot_realtime_data_interactive(exchange_name, symbol, timeframe):
    exchange = getattr(ccxt, exchange_name)()  # Initialize exchange
    fig = make_subplots(rows=1, cols=1)

    data = fetch_data_with_retry(exchange, symbol, timeframe, limit=100)
    if data:
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

        fig.add_trace(go.Scatter(x=df['date'], y=df['close'], mode='lines', name='Close Price'))
        fig.update_layout(title=f'{symbol} Price (Real-time)', xaxis_title='Time', yaxis_title='Price (USDT)')

        # Save the plot as an HTML file
        plot_filename = 'btc_price.html'
        fig.write_html(plot_filename)
        print(f"Plot saved as '{plot_filename}'. Open it in your browser.")

        # Open the plot automatically in the default web browser
        html_file_path = os.path.abspath(plot_filename)
        webbrowser.open(f"file://{html_file_path}")


# Example usage
plot_realtime_data_interactive('kraken', 'BTC/USDT', '1m')
