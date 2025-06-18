#This script is to test different moving average window sizes to determine which returns the best sharpe ratio.
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from backtest import compute_moving_averages, trading_signal, compute_returns

#Create rolling average ranges
short = range(5,50,5)
long = range(50, 200, 50)



