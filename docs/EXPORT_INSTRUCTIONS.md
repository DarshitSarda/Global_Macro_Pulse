# Bloomberg Manual Export Guide
# Global Macro Pulse Project
# ─────────────────────────────────────────────────────────────────────────────

## ONE-TIME SETUP (do this at the start of your first session)

1. Open Bloomberg Terminal — log in
2. Open Excel alongside it (it should already be open on university terminals)
3. Plug in USB / make sure you can access your email to send files

---

## FOR EVERY SINGLE TICKER — follow these exact steps

### Step 1: Load the ticker on Bloomberg
- Click on the Bloomberg Terminal window
- Type the ticker exactly as it appears in your checklist (e.g. "SPX Index")
- Press the yellow <EQUITY> or <INDEX> or <CMDTY> or <CURNCY> or <GOVT> key
  (Bloomberg auto-routes — or just type the full ticker and press GO)

### Step 2: Open Historical Prices
- Type: HP
- Press GO (Enter)

### Step 3: Set the date range
- Start Date: 01/01/1990  ← set this ONCE, it stays for the session
- End Date: leave as TODAY (or whatever today's date is)
- Periodicity: DAILY  ← confirm this is set to Daily every time

### Step 4: Export to Excel
- Look for the Export button (top right of HP screen, looks like a small Excel icon)
  OR press: Actions → Export to Excel
  OR press: F8 (on some terminal versions)
- This opens the data directly in Excel

### Step 5: Save as CSV
- In Excel: File → Save As
- Navigate to your USB drive OR a folder you'll email from
- File name: copy EXACTLY from your checklist (e.g. SPX_Index.csv)
- File type: CSV (Comma delimited) (*.csv)
- Click Save → Yes to the CSV warning

### Step 6: Go to next ticker
- Click back on Bloomberg Terminal
- Type the next ticker from your checklist
- Repeat from Step 1

---

## IMPORTANT RULES

✓ Always use DAILY periodicity — never weekly or monthly
✓ Always start from 01/01/1990 — Bloomberg will return from actual data start, that is fine
✓ Save filename EXACTLY as shown in checklist — the pipeline depends on exact names
✓ Do NOT rename columns in Excel before saving
✓ Do NOT delete any rows Bloomberg exports — leave the file exactly as exported
✓ If Bloomberg shows "N/A" or no data for a ticker — skip it, note it in your phone, tell me

---

## WHAT BLOOMBERG EXPORTS (what your CSV will look like)

Bloomberg HP exports look like this — do NOT worry about the header rows,
the pipeline handles them automatically:

  Dates,SPX Index
  ,PX_LAST
  01/02/1990,353.40
  01/03/1990,350.24
  ...

OR sometimes with OHLCV:

  Dates,SPX Index,,,,
  ,PX_OPEN,PX_HIGH,PX_LOW,PX_LAST,VOLUME
  01/02/1990,350.00,355.00,349.00,353.40,123456789
  ...

Both formats are fine. Just save as-is.

---

## AT THE END OF EACH SESSION

1. Make sure all your CSV files for that session are in one folder on USB
2. Zip the entire folder: Right click → Send to → Compressed (zipped) folder
3. Email the zip to yourself with subject: "GMP Data — Session [number] — [date]"
4. Cross off the tickers you completed in your checklist

---

## IF SOMETHING GOES WRONG

- Ticker not found: Try adding the correct market sector key
  e.g. for "KOSPI Index" press the yellow INDEX key after typing
- HP screen shows very little data: The asset may have a shorter history — that is fine, export what exists
- Excel crashes: The CSV is probably still saved, check before redoing
- Cannot export: Try copying the data manually — select all rows in HP, Ctrl+C, paste into Excel, save as CSV

---

## SESSION BATCHING PLAN

Session 1: Branch 1 (Fear/Vol) + Branch 2 (Credit) — 22 tickers — ~45 mins
Session 2: Branch 3 Equities Part 1 (Asia + Oceania) — 14 tickers — ~30 mins
Session 3: Branch 3 Equities Part 2 (Europe + Americas + US) — 20 tickers — ~45 mins
Session 4: Branch 4 (Rates) — 24 tickers — ~50 mins
Session 5: Branch 5 (Commodities + FX) — 23 tickers — ~50 mins
Session 6: Branch 6 (Macro Fundamentals) — 16 tickers — ~35 mins

Total: ~6 sessions, ~4-5 hours of terminal time across multiple visits
