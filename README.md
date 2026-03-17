# CashFlower

## Overview

**CashFlower** is a lightweight, automated personal finance tracker that combines transactions from multiple accounts into one clean, unified view.

Instead of manually reviewing statements, matching purchases, and categorizing expenses, CashFlower:

* Imports your bank and shopping CSV files
* Standardizes all transactions into a single format
* Automatically categorizes common expenses
* Removes duplicates
* Syncs everything to Google Sheets

👉 Goal: **Turn a stressful, manual process into a fully automated workflow.**

---

## Core Features

* ✅ Unified transaction log across all accounts
* ✅ Automatic inflow/outflow separation
* ✅ Basic auto-categorization (customizable)
* ✅ Deduplication of transactions
* ✅ Google Sheets integration (single source of truth)
* ✅ Supports multiple CSV sources

---

## Project Structure

```
CashFlower/
│
├── data/                   # Raw and processed data
│   ├── bank/               # Bank CSVs or PDFs
│   ├── shopping/           # Shopping app exports
│   └── master/             # Optional: saved master CSV
│
├── scripts/                # Core logic
│   └── main.py             # Main pipeline (run this)
│
├── config/                 # Configuration files
│   ├── credentials.json    # Google Sheets API credentials
│
├── logs/                   # Optional logs
│
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## Data Format

All transactions are standardized into this schema:

```
Account | Posting Date | Transaction Date | Payee | Category | Memo | Outflow | Inflow
```

### Notes

* **Outflow** = money spent (positive number)
* **Inflow** = money received (positive number)
* **Transaction Date** = when purchase happened
* **Posting Date** = when bank recorded it

---

## Setup Instructions

### 1. Install dependencies

```bash
python3 -m pip install pandas gspread oauth2client fuzzywuzzy python-Levenshtein
```

### 2. Setup Google Sheets

1. Create a Google Sheet named: `MasterTransactions`
2. Enable Google Sheets API
3. Create a service account and download `credentials.json`
4. Place it inside:

```
config/credentials.json
```

5. Share your Google Sheet with the service account email

---

## How to Use

### Step 1: Add your data

Drop your CSV files into:

```
data/bank/
data/shopping/
```

Example:

```
bank_202603.csv
shopping_202603.csv
```

---

### Step 2: Run the script

From the root folder:

```bash
python3 scripts/main.py
```

---

### Step 3: View results

* Open your Google Sheet: `MasterTransactions`
* All transactions will be:

  * Combined
  * Cleaned
  * Categorized
  * Deduplicated

---

## Workflow Summary

```
CSV files → Normalize → Categorize → Deduplicate → Google Sheets
```

---

## Customization

### Add categories

Edit the category rules inside `main.py`:

```python
category_rules = {
    "starbucks": "Coffee",
    "amazon": "Shopping",
    "netflix": "Entertainment"
}
```

---

## Future Improvements

* PDF statement parsing
* Smarter transaction matching (fuzzy matching)
* Scheduled automation (cron jobs)
* Spending dashboards (charts)
* Alerts for overspending

---

## Run Frequency

* Recommended: **once per week**
* Or automate it for a fully hands-off system

---

