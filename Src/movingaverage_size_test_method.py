import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from metrics import calc_av, calc_cagr, calc_sharpe
from backtest import compute_moving_averages, trading_signal, compute_returns
from data_loader import load_spy

#A method to test different moving average sizes: when called it loads spy data and calculates sharpe ratios of each rolling window pair. Must provide window sizes. Will output a dictionary file
def moving_average_size(spy, short, long):
    result = []


    # for loop for each rolling average pair
    for s in short:
        for l in long:
            if s >= l:
                continue

            # copies the spy dataframe into a fresh dataframe for us to work with
            df = spy.copy()

            # run backtest
            df = compute_moving_averages(df, s, l)
            df = trading_signal(df)
            df = compute_returns(df)

            # Calculate sharpe ratio
            str_cagr = calc_cagr(df['Strategy EQ Return'])
            str_av = calc_av(df['Strategy Daily Pct'])
            str_sharpe = calc_sharpe(str_cagr, str_av)

            # appends the results into our list, the results are type dictionary
            result.append({'short': s, 'long': l, 'sharpe': str_sharpe})
    return result





