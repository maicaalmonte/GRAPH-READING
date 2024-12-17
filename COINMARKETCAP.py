import requests
import matplotlib.pyplot as plt
import datetime

# Replace with your actual API key from CoinMarketCap
api_key = 'your_actual_api_key'  # Ensure you replace this with your actual API key

# CoinMarketCap API URL for historical prices
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical'

# Parameters for fetching historical price data
parameters = {
    'symbol': 'BTC',  # Cryptocurrency symbol (BTC = Bitcoin, ETH = Ethereum)
    'convert': 'USD',  # Currency (USD, EUR, etc.)
    'time_start': '2023-11-01',  # Start date (YYYY-MM-DD)
    'time_end': '2023-11-30',    # End date (YYYY-MM-DD)
}

# Headers with the API key for authentication
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

# Fetch data from the CoinMarketCap API
response = requests.get(url, headers=headers, params=parameters)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    # Extract OHLC data (Open, High, Low, Close, Volume)
    prices = data['data']['quotes']

    # Prepare the data for plotting
    dates = [datetime.datetime.strptime(item['time_open'], "%Y-%m-%dT%H:%M:%S.%fZ") for item in prices]
    close_prices = [item['close'] for item in prices]

    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(dates, close_prices, label='Close Price (USD)', color='blue')
    plt.title('Bitcoin (BTC) Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ensure the graph fits well in the figure
    plt.legend()
    plt.show()

else:
    print(f"Error: {response.status_code}")
    try:
        error_details = response.json()
        print(f"Error Message: {error_details.get('status', {}).get('error_message', 'No error message available')}")
    except ValueError:
        print("Response is not in valid JSON format.")
