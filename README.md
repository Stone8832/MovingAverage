# Moving-Average Crossover Study (SPY 2020-06-15 → present)

> Evaluate a two-moving-average crossover trading strategy on SPY, sweep window pairs,  
> and identify the zone with the best risk-adjusted return compared to a simple buy-and-hold strategy.

---

## 1 Project highlights

| Item                             | Result                        |
|----------------------------------|------------------------------:|
| Buy-and-Hold Sharpe              | **0.78**                      |
| Buy-and-Hold CAGR                | **13.86%**                    |
| Best MA pair                     | **short 6 / long 15**         |
| Best-pair Sharpe                 | **1.27**                      |
| Best-pair CAGR                   | **13.58%**                    |
| Max Drawdown cut vs SPY          | –24.5 % → **–13.94 %**        |
| Code style                       | Modular `Src/`, reproducible `experiments/` |
| Visuals                          | Coarse + refined heat-maps (`Results/`)      |

---

## 2 Repo layout

```text
MovingAverage/          ← project root
├─ Src/                reusable modules
│    ├─ data_loader.py   # load_spy(start="2020-06-15")
│    ├─ backtest.py      # compute_moving_averages, signals, returns
│    ├─ metrics.py       # CAGR, annualised vol, Sharpe, drawdown
│    ├─ plot.py          # price+MA, equity curves, heat-maps
│    └─ movingaverage_size_test_method.py   # helper for moving average size tests
├─ experiments/        experiments and test
│    ├─ best_pairs_comparision.py
│    └─ movingaverage.py
│    └─ movingaverage_size_test.py
│    └─ movingaverage_small_size_test.py
├─ Results/            output CSVs & PNG heat-maps
├─ final_report.py     one-click demo of MA(5,20) vs SPY
├─ requirements.txt    pinned dependencies
└─ README.md           this file
```

---

## 3 Quick start

```bash
git clone https://github.com/Stone8832/MovingAverage.git
cd MovingAverage

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

pip install -r requirements.txt

# Run the final summary (prints metrics + charts)
python final_report.py
```

---

## 4 Methodology

* **Data**  
  SPY daily, split-adjusted prices via `yfinance`, from **2020-06-15** to latest available date.  
* **Signal**  
  Long = 1 when MA<sub>short</sub> > MA<sub>long</sub>; flat = 0 otherwise.  
  Positions execute *next* trading session (`signal.shift(1)`) to avoid look-ahead bias.  
* **Back-test**  
  Vectorised in pandas:  
  - `Spy Daily Pct` = daily pct change of `Close`  
  - Equity curves via `cumprod(1 + returns)`  
* **Metrics**  
  - **CAGR** (compound annual growth rate)  
  - **Annualised volatility** (`σ` × √252)  
  - **Sharpe** (rf = 0)  
  - **Max drawdown** (peak-to-trough)  
* **Parameter search**  
  1. **Coarse grid:** short 5–30 (step 5) × long 20–120 (step 10)  
  2. **Refined grid:** short 2–10 (step 1) × long 10–40 (step 2)  
  Two high-Sharpe clusters emerge:  
  - short < 9 & long 10–30  
  - short < 9 & long ≥ 100  

**Top-3 pairs** → (6, 15), (9, 10), (3, 100) all beat SPY on Sharpe while roughly halving drawdown.

---

## 5 Conclusions

1. **Initial test (10,50)**  
   - Back‐tested a 10-day/50-day MA crossover vs. buy-and-hold on SPY (2020-06-15 – present).  
   - Buy-and-hold: CAGR 13.86 %, Sharpe 0.78, Max DD –24.5 %.  
   - MA(10,50): CAGR 7.66 %, Sharpe 0.64, Max DD –14.94 %.  
   - *Takeaway:* Simple 10/50 cut drawdown but gave up too much upside. Did not showcase to be a valuable strategy with the given window sizes.

2. **Coarse grid search**  
   - Ranged short 5–30 (step 5) × long 20–120 (step 10).  
   - 22 out of 62 pairs (≈ 36.6 %) beat SPY’s Sharpe.  
   - Best pair: MA(5,20) with Sharpe 1.03.
    - This pair was the only one that resulted in a Sharpe ratio above 1 which made me do further testing. I hypothesized that tighter window size pairs will yield better results. 

3. **Refined grid search**  
   - Ranged short 3–30 (step 3) × long 10–121 (step 5).  
   - 73 out of 210 pairs (≈ 35 %) beat SPY’s Sharpe.  
   - 8 pairs exceeded Sharpe 1.0, clustering where short < 9 and long in [10–30] or ≥ 100.
   - Results showed that the short range moving average window best performed under 9-day MA. The long range MA showed best results when it had a smaller time frame close to the short MA OR a long range MA that was greater than 100. Long range MAs between these values had lackluster results.

4. **Top-3 selection**  
   - Chosen by highest Sharpe and reasonable drawdowns:  
     - MA(6,15) → Sharpe 1.19, CAGR 12.7 %, Max DD –13.9 %  
     - MA(9,10) → Sharpe 1.17, CAGR 13.0 %, Max DD –12.1 %  
     - MA(3,100) → Sharpe 1.07, CAGR 12.4 %, Max DD –17.1 %  
   - These three all outperform buy-and-hold on risk-adjusted return while cutting drawdown roughly in half.

5. **Equity-curve trade-off**  
   - All top pairs end with lower nominal equity (×1.7–1.9) vs. buy-and-hold (×2.1).  
   - They deliver smoother P&L, higher Sharpe, and smaller drawdowns.

6. **Key insight**  
   - **Short MAs of ~5–9 days** combined with **long MAs of ~10–30 days** yield the best risk-adjusted performance on SPY.  
   - Simple crossover can reduce downside and risk, but at the cost of some upside capture.

---


*Completed by **William R.** (Applied Math Major ’27).*  
