# updated code due to yahoo policy
import yfinance as yf
from datetime import datetime
import time

# take user inputs
company = input("Enter Company Inc: ")
from_date = input("Enter start date in yyyy-mm-dd format: ")
end_date = input("Enter end date in yyyy-mm-dd format: ")

# * download historical data for AAPL (Apple Inc.)
data = yf.download(company, start=from_date, end=end_date, interval="1d")
# data = yf.download("AAPL", start="1981-01-01", end="2024-10-29", interval="1d")

# * save data to CSV file
data.to_csv("data.csv")


#! out-dated version below...
# import requests

# url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1642032000&interval=1d&events=history&includeAdjustedClose=true"

# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# content = requests.get(url, headers=headers).content
# print(content)

# with open('data.csv', 'wb') as file:
#     file.write(content)


# """
# content = requests.get(url, headers=headers).text  #! .text for text, .content for content
# print(content)

# with open('data.csv', 'w') as file: #! wb for write binary, w for write text
#     file.write(content)
# """
