# Global Macro Pulse

A systematic macro monitoring and regime classification framework built on 117 assets across 36 years of daily Bloomberg data. The system combines a six-branch rule-based classifier, machine learning regime discovery, forward-looking transition forecasting, and empirically optimised thresholds into a single integrated morning briefing.

---

## Architecture Overview

```
RAW DATA (Bloomberg, 117 assets, 1989-2026)
         │
         ▼
SIX BRANCH FRAMEWORK          CORRELATION ENGINE
  B1 Fear & Volatility    ──►  Static / Rolling / Conditional
  B2 Credit Stress             Cross-asset correlation matrices
  B3 Equity Internals          Regime-conditional correlations
  B4 Rates & Curve
  B5 Commodities & FX
  B6 Macro Fundamentals
         │
         ▼
RULE-BASED REGIME CLASSIFIER (11 states, daily)
         │
         ▼
ML REGIME CLASSIFIER
  PCA Factor Extraction  →  4 orthogonal factors, 51% variance
  HMM Regime Discovery   →  6 states, 36-day average duration
  Calibrated RF          →  62.4% OOS accuracy, 22.2% train-test gap
         │
         ▼
MULTI-TIMESCALE SYSTEM
  Daily    →  Rule-based (reactive)
  Medium   →  63D HMM + Calibrated RF (1-3 month trend)
  Strategic→  Fundamentals-based business cycle (ISM + curve + HY)
         │
         ▼
TRANSITION WARNING SYSTEM
  N-step Markov forecasting  →  P(t+n) = P(t) × T^n
  Composite warning score    →  0-100, 22.5x lift over random
  Forward probability matrix →  5D / 21D / 63D horizons
         │
         ▼
EMPIRICALLY OPTIMISED THRESHOLDS
  Regime mean separation     →  HMM ground truth anchoring
  Polarity correction        →  Data-driven branch direction
  Calibrated weighting       →  2x amplification for extreme signals
         │
         ▼
CORRELATION-ENHANCED CLASSIFIER
  9 rolling pairwise measures
  Correlation Stress Index (7th branch)
  VIX-credit confirmation signal
         │
         ▼
MORNING BRIEFING
  Regime label + probability vector
  Transition warning score
  PCA factor Z-scores
  Branch scorecard
  Multi-timescale divergence narrative
```

---

## Key Results

| Component | Result |
|---|---|
| Sequential signal accuracy | 64.4% directional across 27-year walk-forward |
| With threshold filter | 75.3% directional accuracy |
| Calibrated RF OOS accuracy | 62.4% on 6-class problem |
| HMM regime durations | 28-52 days (proper macro timescales) |
| Threshold optimisation | +17.7% accuracy improvement, all 6 regimes improved simultaneously |
| Transition warning lift | 22.5x over random baseline |
| Covid early warning | CSI elevated 42 days before March 2020 crash |
| PCA variance explained | 51% from 4 orthogonal factors |

---

## Repository Structure

```
GlobalMacroPulse/
│
├── config/
│   └── settings.py                  # Paths, tickers, parameters
│
├── data/
│   ├── raw/                         # Bloomberg raw exports
│   └── processed/
│       ├── master_returns.csv       # 117 assets, log returns / first diffs
│       ├── aligned_prices.csv       # Forward-filled price matrix
│       └── regimes/                 # Branch outputs, optimised thresholds
│
├── notebooks/
│   ├── 01_data_pipeline/            # Bloomberg ingestion, cleaning
│   ├── 02_branch1_fear/             # VIX, MOVE, put-call, term structure
│   ├── 03_branch2_credit/           # HY/IG spreads, TED, CDS
│   ├── 04_branch3_equity/           # Breadth, momentum, internals
│   ├── 05_branch4_rates/            # Yield curve, real rates, breakevens
│   ├── 06_branch5_commodities/      # Copper/Gold, oil, BCOM, FX
│   ├── 07_branch6_macro/            # ISM, CESI, LEI, PMI
│   ├── 08_correlation_engine/       # Static, rolling, conditional correlations
│   ├── 09_sequential_signal/        # US→Asia transmission, walk-forward
│   ├── 10_regime_classifier/        # Rule-based 11-state classifier
│   ├── 11_morning_briefing/         # Daily output integration
│   ├── 12_train_test_framework/     # Temporal validation infrastructure
│   ├── 13_ml_regime_classifier/     # PCA + HMM + Calibrated RF
│   ├── 14_transition_warning/       # N-step Markov, warning score
│   ├── 15_threshold_optimisation/   # Empirical threshold derivation
│   └── 16_correlation_regime/       # CSI, correlation features, enhanced RF
│
└── outputs/
    ├── charts/                      # All visualisations
    └── signals/                     # Regime labels, probabilities, forecasts
```

---

## Notebooks in Detail

### Data Pipeline (NB 01)
Ingests Bloomberg data for 117 assets across equities, rates, credit, FX, commodities, and macro indicators. Applies correct transformations — log returns for prices, first differences for rates and spreads. Handles the WTI negative price event (April 2020), missing data, and holiday alignment across 15+ global markets.

### Six Branch Framework (NB 02-07)
Each branch produces a 0-100 score measuring one dimension of the macro environment. Scores are constructed from weighted sub-signals, normalised using rolling percentile ranks, and validated for economic coherence.

**Branch 1 — Fear:** VIX level, VIX term structure slope, MOVE index, equity put-call ratio, volatility regime indicator.

**Branch 2 — Credit:** US HY OAS, US IG OAS, EU HY OAS, TED spread, cross-currency basis. Detects early credit deterioration — the most reliable leading indicator of regime transitions.

**Branch 3 — Equity Internals:** Market breadth, advance-decline, new highs vs lows, sector rotation, momentum dispersion. Measures health beneath the surface index level.

**Branch 4 — Rates:** Yield curve slope (2s10s, 3m10y), real rates, breakeven inflation, rate volatility (MOVE). Captures monetary cycle position.

**Branch 5 — Commodities and FX:** Copper/Gold ratio (growth vs safety), oil, BCOM, DXY, carry crosses. Commodity signals are among the most forward-looking in the system.

**Branch 6 — Macro Fundamentals:** ISM Manufacturing, CESI surprise index, LEI, global PMI composite. The weakest branch statistically (sparse data pre-2003) but provides the strategic economic anchor.

### Correlation Engine (NB 08)
Static, rolling (21D and 63D), and regime-conditional correlation matrices across all 117 assets. Key findings: equity correlations spike 2.6x in crisis vs goldilocks; stock-bond correlation structurally broke positive in 2022; gold does not reliably hedge equities in most regimes.

### Sequential Signal Validation (NB 09)
Tests whether US close prices predict Asian open direction. Builds composite transmission signal from six branches. Walk-forward validation across 1995-2022: 64.4% directional accuracy (26/27 years statistically significant), rising to 75.3% with threshold filter. The most rigorous validation in the project — uses bootstrap resampling with AR(1) block structure to correct for autocorrelation.

### Rule-Based Regime Classifier (NB 10-12)
Combines six branch scores into a composite pulse score. Classifies into 11 states: GOLDILOCKS, RISK-ON, RECOVERY, EXPANSION, TIGHTENING CYCLE, TRANSITIONAL, EASING CYCLE, STAGFLATION, GROWTH SCARE, RISK-OFF, FINANCIAL CRISIS. Includes opening gap correction, bootstrap analysis, and train/val/test split framework.

### ML Regime Classifier (NB 13)

**PCA Factor Extraction:** Runs PCA on all 117 asset returns. Extracts 4 orthogonal factors explaining 51% of daily variance: Risk Appetite (24.8%), Dollar Strength (11.0%), Inflation/Deflation (8.1%), Asia vs US (7.2%).

**HMM Regime Discovery:** Fits Gaussian HMM with K=6 states (BIC selected, economic judgment applied) on 63-day smoothed factor data. Discovers regime structure from data without imposing labels. Manual labelling anchored to 30 historical events including GFC, Covid, EU debt crisis, dot-com peak. Average regime duration 36 days — proper macro timescales.

**Calibrated Random Forest:** Trains on HMM labels using 15 features (branch scores, PCA factors, derived signals). 5-fold isotonic calibration reduces log-loss. Test accuracy 62.4% on 6-class problem; train-test gap reduced to 22.2% through depth and leaf-size constraints.

**Multi-Timescale Architecture:**
- Daily: Rule-based classifier (reactive, no smoothing)
- Medium: 63D HMM + Calibrated RF (1-3 month macro trend)
- Strategic: Fundamentals-based business cycle (ISM + yield curve + HY spreads), implementing the Bridgewater four-quadrant framework with 2-month momentum confirmation for PEAK detection

### Regime Transition Warning System (NB 14)
Converts the HMM transition matrix into actionable forward-looking signals. For every day in history and in real time, computes:
- P(regime) at 5D, 21D, and 63D horizons via matrix exponentiation
- Regime stability score (probability of remaining in current regime)
- Downgrade probability (probability of transitioning to worse regime)
- Regime entropy (uncertainty in current state distribution)
- Composite warning score (0-100)

Validated: warning score >= 50 preceded regime transitions 62.1% of the time versus 2.8% base rate — 22.5x lift. Covid stress detected 42 days before the March 2020 crash. Ukraine/inflation stress flagged 63 days before February 2022 invasion.

### Empirical Threshold Optimisation (NB 15)
Replaces intuition-based thresholds (all branches at 65) with data-derived optimal thresholds anchored to HMM regime means. Key methodological contributions:

- Branch polarity discovery from data: rates, commod, equity, macro are negative polarity (low score = stress)
- Macro branch anchor correction: EXPANSION vs RISK-OFF instead of GOLDILOCKS vs CRISIS
- Calibrated weighting: extreme signals weighted 2x vs calm signals at 0.8x
- Result: +17.7% accuracy improvement, every single regime improved simultaneously
- Mean threshold shift: only 5.4 points — validates original intuition was well-calibrated

### Correlation-Enhanced Classifier (NB 16)
Adds correlation structure as a distinct information layer beyond branch score levels. Constructs 9 rolling pairwise correlation measures (21D and 63D) plus the Correlation Stress Index as a 7th branch. Key finding: smoothed branch scores (42.2% RF importance) nearly equal raw branches (41.4%), confirming both daily readings and sustained trends matter simultaneously. Stock-bond correlation 63D and equity correlation 63D ranked in top 10 features. Enhanced RF adds 2.0% incremental test accuracy.

---

## Methodology Notes

### Train / Validation / Test Splits
All models use strict temporal separation. Training: 1995-2014. Validation: 2015-2019. Test: 2020-present. No model sees test data during training or hyperparameter selection.

### Overfitting Controls
Random Forest: max_depth=5, min_samples_leaf=50, class_weight=balanced, 5-fold calibration. HMM: 30 random initialisations, best log-likelihood selected. BIC model selection on training data only for regime number selection.

### Known Limitations
HMM transition warning system has 22.5x lift that is partially mechanical — the warning score uses the same HMM that generated the labels. Exogenous shocks (9/11, Covid) cannot be predicted by any market-based system and the model correctly misses these. The central bank buy-the-dip era (2020-2024) inverted the historical relationship between crisis regimes and forward equity returns — the system correctly identifies crisis regimes but the market response changed structurally post-2020.

### Data Requirements
Bloomberg Terminal access required for full data. The following Bloomberg tickers are used across 117 assets: global equity indices (SPX, NDX, RTY, DAX, CAC, UKX, NKY, HSI, AS51, KOSPI and others), credit spreads (LF98OAS, LUACOAS, LP01OAS), rates (USGG2YR, USGG10YR, GDBR10, GJGB10), volatility (VIX, V2X, MOVE), commodities (GC1, CL1, HG1, CO1, BCOM), FX (DXY, EURUSD, USDJPY, AUDUSD) and macro (NAPMPMI, LEI TOTL, CESIUSD, USGGBE10).

---

## Current System Reading

As of March 13, 2026 (last data pull):

```
Daily  (rule-based)  : GROWTH SCARE
Medium (63D HMM+RF)  : GOLDILOCKS (54% adjusted confidence)
Strategic (fundamentals): EXPANSION → PEAK
Transition warning   : 59.5/100  [HIGH — 95th percentile historically]

Narrative: Geopolitical fear spike (Iran conflict) on top of a
late-cycle expansion backdrop. VIX-credit correlation at 0.57
suggests fear is being partially confirmed by credit markets.
P(regime downgrade in 21D): 51%. CSI: 67.8/100 ELEVATED.
```

---

## Tech Stack

```
Python 3.11
pandas, numpy, scipy
scikit-learn (RandomForest, CalibratedClassifierCV, PCA, GMM)
hmmlearn (GaussianHMM)
matplotlib, seaborn
Bloomberg blpapi (data ingestion)
```

---

## Author

Darshit Sarda
MS Financial Engineering, NYU Tandon School of Engineering
