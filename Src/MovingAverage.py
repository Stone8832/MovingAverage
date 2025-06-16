import yfinance as yf
import pandas as pd

#import spy data; data holds date, close, high, low, open, and volume. Date is datetime
spy = yf.download("SPY", start = "2020-06-15", auto_adjust= True)

#set variables and close price dataframe
short = 10
long = 50

#create the short and long moving averages and add to spy
spy['ma_short'] = spy['Close'].rolling(short).sum().div(short)
spy['ma_long'] = spy['Close'].rolling(long).sum().div(long)
spy = spy.dropna()


#Create the trading single, if short > long signal = 1(in the market) otherwise signal = 0
spy['Signal'] = (spy['ma_short'] > spy['ma_long']).astype(int)
spy['Signal'] = spy['Signal'].shift(1)
spy.at['2020-08-24', 'Signal'] = 0
print(spy.head())
#Note for later, code above adds a Signal column to spy and outputs one if yesterday was short> long and 0 if false

#Caluculate returns and equity curvs
#Calculate daily spy returns







