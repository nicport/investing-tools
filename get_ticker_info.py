import csv
import yfinance as yf

if __name__ == '__main__':
    with open('stock_tickers.csv') as data:
      csvreader = csv.reader(data, delimiter='\n')
      for row in csvreader:
        print('Getting information for ticker ' + row[0] + '......')
        try:
          stock = yf.Ticker(row[0])
          print(stock.info)
        except Exception as e:
           print(e)
    data.close()