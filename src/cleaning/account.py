import pandas as pd

def clean_account(rawPath, cleanPath):
    df = pd.read_csv(rawPath, sep=";", dtype= {
        "account_id": "int64",
        "district_id": "int64",
        "frequency": "category",
        "date": "object",
    })
    df['date'] = pd.to_datetime(df['date'], format="%y%m%d")

    df.to_csv(cleanPath, sep=",", index=False)

