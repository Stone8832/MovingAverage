import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import spy data; data holds date, close, high, low, open, and volume. Date is datetime
spy = yf.download("SPY", start = "2020-06-15", auto_adjust= True)

#set variables for what we want to define as short and long moving average periods
short = 10
long = 50

#create the short and long moving averages and add to spy
spy['ma_short'] = spy['Close'].rolling(short).sum().div(short)
spy['ma_long'] = spy['Close'].rolling(long).sum().div(long)
spy = spy.dropna()

#Create the trading single, if short > long signal = 1(in the market) otherwise signal = 0
spy['Signal'] = (spy['ma_short'] > spy['ma_long']).astype(int)
spy['Signal'] = spy['Signal'].shift(1)
spy['Signal'] = spy['Signal'].fillna(0)

#Calculate daily spy returns
spy['Spy Daily Pct'] = spy['Close'].pct_change()
spy['Spy Daily Pct'] = spy['Spy Daily Pct'].fillna(0)

#Trading strategy returns
spy['Daily Strategy Returns Pct'] = spy['Signal'] * spy['Spy Daily Pct']
spy['Strategy EQ Return'] = (1 + spy['Daily Strategy Returns Pct']).cumprod()

#buy and hold returns
spy['Hold EQ Return'] = (1 + spy['Spy Daily Pct']).cumprod()

#Plot
spy[['Close', 'ma_short', 'ma_long']].plot(title = 'SPY Price Chart and Moving Averages')
spy[['Hold EQ Return', 'Strategy EQ Return']].plot(title = 'SPY Trading Strategy Equity Comparison');plt.show()

#Notes: Need to make graphs prettier and define financial metrics and possibly test multiple rolling windows






