from data_loader import load_spy
from backtest import trading_signal, compute_moving_averages, compute_returns
from metrics import calc_av, calc_sharpe, calc_drawdown, calc_cagr
from plot import plot_equity, plot_moving_averages

#load data
spy = load_spy()

#backtest steps
spy = compute_moving_averages(spy, short = 10, long =50)
spy = trading_signal(spy)
spy = compute_returns(spy)

#Compute metrics
hold_cagr = calc_cagr(spy['Hold EQ Return'])
hold_av = calc_av(spy['Spy Daily Pct'])
hold_sharpe = calc_sharpe(hold_cagr, hold_av)
hold_drawdown = calc_drawdown(spy['Hold EQ Return'])


