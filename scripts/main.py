import gspread
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
from datetime import datetime
from utils.sheets_utils import log_transaction

# ---------------------------
# Config
# ---------------------------
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
CLIENT_SECRET_FILE = "config/client_secret.json"
TOKEN_PICKLE = "config/token.pickle"
SHEET_NAME = "MasterTransactions"

# ---------------------------
# OAuth setup
# ---------------------------
creds = None
if os.path.exists(TOKEN_PICKLE):
    with open(TOKEN_PICKLE, "rb") as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
    with open(TOKEN_PICKLE, "wb") as token:
        pickle.dump(creds, token)

# ---------------------------
# Connect to Google Sheets
# ---------------------------
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

# ---------------------------
# Test transaction
# ---------------------------
test_transaction = {
    "Account": "Cash",
    "Posting Date": datetime.now().strftime("%Y-%m-%d"),
    "Transaction Date": datetime.now().strftime("%Y-%m-%d"),
    "Payee": "Pizza Place",
    "Category": "Food",
    "Memo": "Lunch test",
    "Outflow": 20,
    "Inflow": 0,
}

log_transaction(sheet, test_transaction)

# ---------------------------
# Optional: print all records
# ---------------------------
print(sheet.get_all_records())
