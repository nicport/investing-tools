# investing-tools

### Overview
This Python script takes a CSV file of stock tickers and outputs the information for each stock using the yfinance Python module.

### Requirements
* Python 3.x
* yfinance Python module (you can install it using pip install yfinance)

### Usage
1. Place the CSV file containing the list of stock tickers in the same directory as the stock_info.py script.
2. Run the script from the command line using python stock_info.py.
3. The script will output the information for each stock in the CSV file.

### CSV file format
The CSV file should contain a list of stock tickers, one per line. For example:
```
AAPL
GOOG
TSLA
```

### Notes
The script uses the yfinance Python module to fetch the stock information. If a ticker is not found or there is an error fetching the information for a stock, 
the script will skip that stock and continue with the next one.
