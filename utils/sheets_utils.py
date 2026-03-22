def log_transaction(sheet, transaction):
    """
    Logs a transaction dictionary to the next empty row in the sheet.
    Expected keys:
    'Account', 'Posting Date', 'Transaction Date', 'Payee',
    'Category', 'Memo', 'Outflow', 'Inflow'
    """
    next_row = len(sheet.get_all_values()) + 1
    values = [
        [
            transaction.get("Account", ""),
            transaction.get("Posting Date", ""),
            transaction.get("Transaction Date", ""),
            transaction.get("Payee", ""),
            transaction.get("Category", ""),
            transaction.get("Memo", ""),
            transaction.get("Outflow", 0),
            transaction.get("Inflow", 0),
        ]
    ]
    sheet.update(f"A{next_row}", values)
    print(f"Transaction logged to row {next_row}")
