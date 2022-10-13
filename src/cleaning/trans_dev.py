import pandas as pd

def clean_trans_dev(rawPath, cleanPath):
    df = pd.read_csv(rawPath, sep=";", dtype= {
        "trans_id": "int64",
        "account_id": "int64",
        "date": "object",
        "type": "category",
        "operation": "category",
        "amount": "float64",
        "balance": "float64",
        "k_symbol": "category",
        "bank": "category",
        "account": "object"
    })

    df['date'] = pd.to_datetime(df['date'], format="%y%m%d")
    df['account'] = pd.to_numeric(df['account'], errors='coerce').astype('Int64')
    df.to_csv(cleanPath, sep=",", index=False)
