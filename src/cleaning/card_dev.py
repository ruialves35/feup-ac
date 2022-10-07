import pandas as pd

def clean_card_dev(rawPath, cleanPath):
    df = pd.read_csv(rawPath, sep=";", dtype= {
        "card_id": "int64",
        "disp_id": "int64",
        "type": "category",
        "issued": "object",
    })
    df['issued'] = pd.to_datetime(df['issued'], format="%y%m%d")

    df.to_csv(cleanPath, sep=",", index=False)

