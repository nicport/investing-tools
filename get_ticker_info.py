import csv
import yfinance as yf


filename_csv = 'stock_tickers.csv'
''' 
  optional: 
    if all the stocks in the csv are from the same exchange this will help
    reduce ambiguity. In this case I am using .TO for the Toronto Stock Exchange
'''
exchange = '.TO'

if __name__ == '__main__':
    try:
      with open(filename_csv) as data:
        csvreader = csv.reader(data, delimiter='\n')
        for row in csvreader:
          print('Getting information for ticker ' + row[0] + '......')
          try:
            stock = yf.Ticker(row[0] + exchange)
            print(stock.info)
          except Exception as e:
            print(f'Error getting information for ticker {row[0]} : {e}')
      data.close()
    except Exception as e:
      print(f'Error opening file {filename_csv} : {e}')