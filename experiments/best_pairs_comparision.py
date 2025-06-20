import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plot import plot_sharpe_heatmap, plot_equity, plot_moving_averages
from movingaverage_size_test_method import moving_average_size
from metrics import calc_av, calc_cagr, calc_sharpe, calc_drawdown
from data_loader import load_spy
from backtest import compute_bh_returns, compute_moving_averages, compute_returns, trading_signal, compute_str_returns
#Diving deeper into the best pairs from the small moving average window size test


#sets up our moving average pairs dataframe and spy data with returns
short = range(3,31, 3)
long = range(10, 121, 5)
spy = load_spy()

result = moving_average_size(spy, short, long)
result_df = pd.DataFrame(result)
best_pairs = result_df.loc[result_df['sharpe'] > 1]
spy = compute_bh_returns(spy)

#Calculate metrics for bh
hold_cagr = calc_cagr(spy['Hold EQ Return'])
hold_av = calc_av(spy['Spy Daily Pct'])
hold_sharpe = calc_sharpe(hold_cagr, hold_av)
hold_drawdown = calc_drawdown(spy['Hold EQ Return'])

#Run back test for every window pair, each pair will get its own dataframe. Create a dict that will hold each data frame
pair_df = {}
for _, row in best_pairs.iterrows():
    s = int(row['short'])
    l = int(row['long'])

    df = spy.copy()
    df = compute_moving_averages(df, short_len = s, long_len= l)
    df = trading_signal(df)
    df = compute_str_returns(df)

    pair_df[(s,l)] = df

#Calculate metrics for each window pair and add to pairs dataframe
cagr, av, drawdown = [],[],[]

for _, row in best_pairs.iterrows():
    df = pair_df[(row['short'], row['long'])]
    cagr.append(calc_cagr(df['Strategy EQ Return']))
    av.append(calc_av(df['Strategy Daily Pct']))
    drawdown.append(calc_drawdown(df['Strategy EQ Return']))

#add metrics to the pairs dataframe
best_pairs_metrics = best_pairs.copy()
best_pairs_metrics['cagr'] = cagr
best_pairs_metrics['av'] = av
best_pairs_metrics['drawdown'] = drawdown

print(best_pairs_metrics)


