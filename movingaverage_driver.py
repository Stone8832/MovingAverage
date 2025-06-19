from data_loader import load_spy
from backtest import trading_signal, compute_moving_averages, compute_returns
from metrics import calc_av, calc_sharpe, calc_drawdown, calc_cagr
from plot import plot_equity, plot_moving_averages
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#This script is the file driver which will run the original moving average backtest but does so using the created methods.
#load data
spy = load_spy()

#backtest steps
spy = compute_moving_averages(spy, 10, 50)
spy = trading_signal(spy)
spy = compute_returns(spy)

#Compute metrics for buy and hold
hold_cagr = calc_cagr(spy['Hold EQ Return'])
hold_av = calc_av(spy['Spy Daily Pct'])
hold_sharpe = calc_sharpe(hold_cagr, hold_av)
hold_drawdown = calc_drawdown(spy['Hold EQ Return'])

#Compute metrics for strategy
str_cagr = calc_cagr(spy['Strategy EQ Return'])
str_av = calc_av(spy['Strategy Daily Pct'])
str_sharpe = calc_sharpe(str_cagr, str_av)
str_drawdown = calc_drawdown(spy['Strategy EQ Return'])

#Plot Graphs
#plot_moving_averages(spy); plot_equity(spy); plt.show()

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







