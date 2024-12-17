proxies = {
    'http': 'http://username:password@proxyserver:port',
    'https': 'https://username:password@proxyserver:port',
}
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Script started")
# Add more log messages as needed in different parts of your script
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Script started")

# Test plotting a simple graph
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title("Test Plot")
plt.show()

logging.info("Script finished")
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Fetching data...")

# Add a print or log here to ensure the function is being called
data = fetch_data_with_retry(exchange, symbol, timeframe)
if data:
    logging.info(f"Data fetched: {data[:5]}")  # Display the first few data points
else:
    logging.error("Failed to fetch data.")
