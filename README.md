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
    
      
         python your_script_name.py
Usage
Once you've set up the project and installed all the dependencies, you can run the script to fetch and visualize cryptocurrency data.

For example, to fetch data from Kraken for the BTC/USD pair, you can run:
    
      
      python your_script_name.py

![Screenshot 2024-12-17 154736](https://github.com/user-attachments/assets/d8958d92-72f3-4789-8741-b208dcb72c58)
![Screenshot 2024-12-17 160830](https://github.com/user-attachments/assets/c22027cd-1353-4f5d-8f60-52bf7895882c)
![Screenshot 2024-12-17 194742](https://github.com/user-attachments/assets/26d8632b-79da-4703-ab39-5979c4272c9b)



