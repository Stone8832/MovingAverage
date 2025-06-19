import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from metrics import calc_av, calc_cagr, calc_sharpe
from backtest import compute_moving_averages, trading_signal, compute_returns
from data_loader import load_spy
from movingaverage_size_test_method import moving_average_size


short = range(3, 50, 2)
long = range(50, 100, 5)

result = moving_average_size(short, long)

result_df = pd.DataFrame(result)

print(result_df)

#currewt problem, functiion isnt looping through all the ranges