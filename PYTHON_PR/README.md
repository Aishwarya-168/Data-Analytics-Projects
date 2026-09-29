# Bank Term Deposit Campaign Analysis — Streamlit App

An interactive local dashboard for the UCI Bank Marketing dataset. Filters live in
the sidebar; every chart, KPI, and table updates as you change them.

## 1. Get the dataset

1. Download **bank-full.csv** from the UCI Bank Marketing dataset page:
   https://archive.ics.uci.edu/dataset/222/bank+marketing
   (it's inside the `bank.zip` file — look for `bank-full.csv`)
2. Place it in this folder as:
   ```
   bank-marketing-app/
   └── data/
       └── bank-full.csv
   ```

## 2. Install dependencies

From inside this folder, ideally in a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

## 3. Run the app

```bash
streamlit run app.py
```

Streamlit will open the dashboard automatically at:

```
http://localhost:8501
```

If it doesn't open automatically, just paste that URL into your browser.

## What's inside

- **Overview tab** — monthly conversion trend, conversion by contact channel, job, and education
- **Segment Deep-Dive tab** — age group and loan-status conversion, balance-by-outcome boxplot, top converting job×month combinations
- **Campaign Effectiveness tab** — conversion vs. number of contacts (diminishing-returns check), conversion by previous-campaign outcome
- **Data Explorer tab** — raw filtered data table with a CSV download button

All filters (job, education, marital status, age range, contact channel) in the
sidebar apply across every tab at once.

## Notes

- The app expects the UCI file's default semicolon (`;`) delimiter, but will fall
  back to comma-separated if you're using a differently exported copy.
- Rebuilding charts on every filter change is intentional — it keeps the app
  simple (pure Matplotlib, no extra charting library) and matches the analysis
  plan we defined earlier.
