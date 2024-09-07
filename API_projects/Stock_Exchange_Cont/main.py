from datetime import date,timedelta,datetime
import smtplib
from tkinter.messagebox import YES
import requests

EMAIL = "send.test02@gmail.com"
EMAIL_PWD = "1234@asdf"
COMPANY_NAME = "Apple"
#STOCK API
STOCK_APIKEY = "UXMJH2R4NBLHSNSR"
STOCK_APIURL = "https://www.alphavantage.co/query"
STOCK_NAME = "AAPL"
#fetching stock Data
STOCK_PARAM = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY
}
data = requests.get(url=STOCK_APIURL,params = STOCK_PARAM)
data.raise_for_status()
stock_data = data.json()

#NEWS API
NEWS_APIKEY = "5e778737a092480aa85219fab8afe835"
NEWS_APIURL = "https://newsapi.org/v2/everything"
NEWS_PARAM = {
    "qInTitle":COMPANY_NAME,
    "apiKey": NEWS_APIKEY
}
n_data = requests.get(url = NEWS_APIURL,params = NEWS_PARAM)
n_data.raise_for_status()
news_data = n_data.json()
articles = news_data["articles"]

#DATE
TODAY = date.today() - timedelta(days=1)
YESTERDAY = TODAY - timedelta(days=1)


#getting stock value of a specific day
def stock_val(date):
    try:
        new_val = float(stock_data["Time Series (Daily)"][str(date)]['4. close'])
    except KeyError:
        new_date = date - timedelta(days=1)
        return stock_val(new_date)
    else:
        return new_val

#calculating stock difference
def stock_difference(new_val,old_val):
    difference = new_val - old_val
    diff_percent = (difference / new_val)*100
    return round(diff_percent,2)

def send_mail(stock_val):
    pass


#Main Algorithm
today_stock = stock_val(TODAY)
yesterday_stock = stock_val(YESTERDAY)
difference_rate = stock_difference(today_stock,yesterday_stock)

#drastic stock change
if abs(difference_rate) >= 5.00:
    print("news sent!!")

