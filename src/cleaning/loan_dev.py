import pandas as pd

def clean_loan_dev(rawPath, cleanPath):
    df = pd.read_csv(rawPath, sep=";", dtype= {
        "loan_id": "int64",
        "account_id": "int64",
        "date": "object",
        "amount": "int64",
        "duration": "int64",
        "payments": "int64",
        "status": "category",
    })

    df['date'] = pd.to_datetime(df['date'], format="%y%m%d")
    df['status'] = df['status'].cat.add_categories([0])
    df.loc[df.status == "-1", "status"] = 0
    df = df.rename(columns={"status": "paid"})
    df.to_csv(cleanPath, sep=",", index=False)
