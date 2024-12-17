# GRAPH-READING

A Python project for fetching and visualizing cryptocurrency data from the Etherium, Coingecko, Binance, Coinmarketcap API.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maicaalmonte/GRAPH-READING.git
   cd GRAPH-READING
2. Create virtual environment
   ```bash
   python -m venv .venv

2. # Activate the virtual environment:
 # On Windows:
      ```bash
      .venv\Scripts\activate
   
3. # On macOS/Linux:
      ```bash
      source .venv/bin/activate

5. #install requirement
      ```bash
      pip install -r requirements.txt

About
This project allows users to fetch real-time and historical cryptocurrency data from multiple sources (including Ethereum, Binance, CoinGecko, and CoinMarketCap) using their respective APIs. The data is then processed and visualized to aid in analysis.

Key Features:
Fetches OHLCV (Open, High, Low, Close, Volume) data for cryptocurrencies.
Supports multiple cryptocurrency exchanges like Binance and Kraken.
Data visualization using matplotlib.
Includes retry logic for handling temporary API issues or rate limits.
         ```bash
         python your_script_name.py
Usage
Once you've set up the project and installed all the dependencies, you can run the script to fetch and visualize cryptocurrency data.

For example, to fetch data from Kraken for the BTC/USD pair, you can run:
            ```bash
      python your_script_name.py
