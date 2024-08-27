import yfinance as yf
import pandas as pd

# Define the stock ticker and period for which you want the data
ticker = "AAPL"
start_date = "2023-01-01"
end_date = "2023-12-31"

# Fetch the data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Display the first few rows of the data
print(stock_data.head())

# Save the data to a CSV file 
stock_data.to_csv(f'{ticker}_historic_data.csv')

