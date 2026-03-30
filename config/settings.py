import os

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_PATH   = r"C:\Users\sarda\Desktop\GlobalMacroPulse"
DATA_PATH   = os.path.join(BASE_PATH, "data")
RAW_PATH    = os.path.join(DATA_PATH, "raw")
PROC_PATH   = os.path.join(DATA_PATH, "processed")
EVENT_PATH  = os.path.join(DATA_PATH, "events")
OUT_PATH    = os.path.join(BASE_PATH, "outputs")
CONFIG_PATH = os.path.join(BASE_PATH, "config")

# ── Raw sub-folders (mirrors Bloomberg asset classes) ────────────────────────
RAW_FOLDERS = {
    "equity":            os.path.join(RAW_PATH, "equities"),
    "volatility":        os.path.join(RAW_PATH, "volatility"),
    "credit":            os.path.join(RAW_PATH, "credit"),
    "rates":             os.path.join(RAW_PATH, "rates"),
    "commodity":         os.path.join(RAW_PATH, "commodities"),
    "fx":                os.path.join(RAW_PATH, "fx"),
    "macro":             os.path.join(RAW_PATH, "macro_fundamentals"),
}

# ── Bloomberg pull settings ──────────────────────────────────────────────────
BBG_START_DATE  = "19900101"       # BDH will return from actual series start
BBG_END_DATE    = "today"          # Always pull to latest available
BBG_FIELDS      = ["PX_OPEN", "PX_HIGH", "PX_LOW", "PX_LAST", "VOLUME"]
BBG_CLOSE_FIELD = "PX_LAST"        # The field we use for return computation
BBG_PERIODICITY = "DAILY"

# ── Calendar and timezone ────────────────────────────────────────────────────
ANCHOR_TIME     = "17:00"          # 5pm New York — daily data cut
ANCHOR_TZ       = "America/New_York"

# ── Return computation ───────────────────────────────────────────────────────
RETURN_TYPE     = "log"            # "log" or "simple" — log returns for correlation work
MIN_HISTORY_DAYS = 252             # An asset needs at least 1Y of data to be included

# ── Rolling window sizes (trading days) ─────────────────────────────────────
WINDOWS = {
    "short":    21,    # ~1 month
    "medium":   63,    # ~3 months
    "long":     252,   # ~1 year
    "verylong": 756,   # ~3 years
}

# ── Regime classifier ────────────────────────────────────────────────────────
REGIME_LABELS   = ["risk_on", "risk_off", "transitional", "crisis"]
REGIME_LOOKBACK = 252              # 1Y lookback for Z-score normalisation

# ── Sequential market open order (for Branch 3) ─────────────────────────────
# Each tuple: (asset_name, bloomberg_ticker, approx_open_UTC)
MARKET_SEQUENCE = [
    ("NZX 50",          "NZ50 Index",    "21:00"),   # NZ open (prev day UTC)
    ("ASX 200",         "AS51 Index",    "23:00"),   # Sydney open
    ("Nikkei 225",      "NKY Index",     "00:00"),   # Tokyo open
    ("TOPIX",           "TPX Index",     "00:00"),
    ("TAIEX",           "TWSE Index",    "01:00"),   # Taipei open
    ("KOSPI",           "KOSPI Index",   "00:00"),   # Seoul open
    ("Hang Seng",       "HSI Index",     "01:30"),   # HK open
    ("CSI 300",         "SHSZ300 Index", "01:30"),   # Shanghai open
    ("STI",             "STI Index",     "01:00"),   # Singapore open
    ("Nifty 50",        "NIFTY Index",   "03:45"),   # Mumbai open
    ("DAX",             "DAX Index",     "08:00"),   # Frankfurt open
    ("CAC 40",          "CAC Index",     "08:00"),   # Paris open
    ("SMI",             "SMI Index",     "08:00"),   # Zurich open
    ("FTSE 100",        "UKX Index",     "08:00"),   # London open
    ("Euro Stoxx 50",   "SX5E Index",    "08:00"),
    ("Bovespa",         "IBOV Index",    "13:00"),   # Sao Paulo open
    ("TSX",             "SPTSX Index",   "14:30"),   # Toronto open
    ("S&P 500",         "SPX Index",     "14:30"),   # NYSE open
    ("DJIA",            "INDU Index",    "14:30"),
    ("NASDAQ",          "CCMP Index",    "14:30"),
]

# ── Output file names ────────────────────────────────────────────────────────
MASTER_RETURNS_FILE  = os.path.join(PROC_PATH, "returns", "all_returns.csv")
ALIGNED_PRICES_FILE  = os.path.join(PROC_PATH, "aligned",  "all_prices_aligned.csv")
REGIME_HISTORY_FILE  = os.path.join(PROC_PATH, "regimes",  "regime_history.csv")

# ── Logging ──────────────────────────────────────────────────────────────────
LOG_LEVEL = "INFO"
