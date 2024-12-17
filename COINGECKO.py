import requests
import matplotlib.pyplot as plt
import datetime

# CoinGecko API endpoint for historical prices
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

# Parameters: Get historical data for the last 30 days in USD
parameters = {
    'vs_currency': 'usd',
    'days': '30',  # You can change this to 'max' or a specific number of days
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    prices = data['prices']

    # Extract dates and prices
    dates = [datetime.datetime.fromtimestamp(item[0] / 1000) for item in prices]  # Convert timestamp
    close_prices = [item[1] for item in prices]

    # Plot the graph
    plt.plot(dates, close_prices)
    plt.title("Bitcoin Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price in USD")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print(f"Error: {response.status_code}")
    print(response.json())
