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
spy['Spy Daily Pct'] = spy['Close'].pct_change() #new column
spy['Spy Daily Pct'] = spy['Spy Daily Pct'].fillna(0)
spy['Hold EQ Return'] = (1 + spy['Spy Daily Pct']).cumprod() #buy and hold eq returns

#Trading strategy returns
spy['Strategy Daily Pct'] = spy['Signal'] * spy['Spy Daily Pct'] #new column, only applies spy daily pct change if position is true
spy['Strategy EQ Return'] = (1 + spy['Strategy Daily Pct']).cumprod()

#Plot SPY and moving averages
spy[['Close', 'ma_short', 'ma_long']].plot(title = 'SPY Price Chart and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')

#Plot EQ Returns
spy[['Hold EQ Return', 'Strategy EQ Return']].plot(title = 'SPY Trading Strategy Equity Comparison')
plt.xlabel('Date')
plt.ylabel('Equity')

#plt.show() uncomment this to bring graphs back

#Calculate CAGR: Compound annual growth rate, provides smooth year-over-year growth return
def calc_cagr(equity):
    ending_value = equity.iloc[-1]
    days = len(equity)
    annual_factor = 252 / days
    return (ending_value ** annual_factor) - 1

#Calculate Annualized volatility: Measure of how volatile an investment is over a year
def calc_av(returns):
    daily_variance = returns.std()
    return daily_variance * np.sqrt(252)

#Calculate Sharpe Ratio: Return per unit of risk "How much extra return did I get for each percent of volatility I endured". Note, we assume zero risk free rate
def calc_sharpe(cagr, vol):
    return cagr / vol if vol != 0 else np.nan

#Calculate Maximum drawdown: The worst peak-to- trough decline our equity curve experienced
def calc_drawdown(equity):
    peak = equity.cummax() #returns a series with the max up until that point
    drawdown = (equity - peak) / peak
    return drawdown.min()

#Compute metrics for buy and hold
hold_cagr = calc_cagr(spy['Hold EQ Return'])
hold_av = calc_av(spy['Spy Daily Pct'])
hold_sharpe = calc_sharpe(hold_cagr, hold_av)
hold_drawdown = calc_drawdown(spy['Hold EQ Return'])

#Compute metrics for trading strategy
str_cagr = calc_cagr(spy['Strategy EQ Return'])
str_av = calc_av(spy['Strategy Daily Pct'])
str_sharpe = calc_sharpe(str_cagr, str_av)
str_drawdown = calc_drawdown(spy['Strategy EQ Return'])

#Print and compare the financial metrics
print("Metric                 |     Buy-and-hold       |     Trading Strategy ")
print("-----------------------|------------------------|----------------------")
print(f"CAGR                  |    {hold_cagr: .2%}     |   {str_cagr: .2%}     ")
print(f"Annualized Volatility |    {hold_av: .2%}       |   {str_av: .2%}       ")
print(f"Sharpe Ratio          |    {hold_sharpe: .2f}   |   {str_sharpe: .2f}   ")
print(f"Maximum Drawdown      |    {hold_drawdown: .2%} |   {str_drawdown: .2%} ")

#Comparision
if hold_sharpe > str_sharpe:
    print("\nBuy-and-hold edges out the trading strategy on risk-adjusted returns based on the Sharpe ratio.")
else:
    print("\nThe trading strategy out performs the simply buy-and-hold strategy for the S&P500 based on the Sharpe ratio.")










