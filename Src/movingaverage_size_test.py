#This script is to test different moving average window sizes to determine which returns the best sharpe ratio out of different window size combos
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from metrics import calc_av, calc_cagr, calc_sharpe
from backtest import compute_moving_averages, trading_signal, compute_returns
from data_loader import load_spy

#Create rolling average ranges
short = range(5,31,5)
long = range(20, 121, 10)

#creates the empty list to input the results for the for loop
result = []

#inputs spy data
spy = load_spy(start = "2020-06-15")

#for loop for each rolling average pair
for s in short:
    for l in long:
        if s >= l:
            continue

        #copies the spy dataframe into a fresh dataframe for us to work with
        df = spy.copy()

        #run backtest
        df = compute_moving_averages(df, s, l)
        df = trading_signal(df)
        df = compute_returns(df)

        #Calcualte sharpe ratio
        str_cagr = calc_cagr(df['Strategy EQ Return'])
        str_av = calc_av(df['Strategy Daily Pct'])
        str_sharpe = calc_sharpe(str_cagr, str_av)

        #appends the results into our list, to results are type dictionary
        result.append({'short': s, 'long': l, 'sharpe': str_sharpe})

#now to create our heatmap
result_df = pd.DataFrame(result)
result_matrix = result_df.pivot(columns = 'short', index = 'long', values = 'sharpe').fillna(0)

plt.imshow(result_matrix, origin='lower', aspect='auto')
plt.colorbar(label='Sharpe ratio')
plt.xticks(range(len(result_matrix.columns)), result_matrix.columns)
plt.yticks(range(len(result_matrix.index)),   result_matrix.index)
plt.xlabel('Short window')
plt.ylabel('Long window')
plt.title('MA window Sharpe Ratio heat-map')
plt.show()

#so far how many windows beat the buy and hold strat: 22/62 has a greater sharpe ratio
print(len(result_df['sharpe'].loc[result_df['sharpe'] > 0.781]))

#note: short = 5, long = 20 was the winning rationwith a sharpe of 1.165