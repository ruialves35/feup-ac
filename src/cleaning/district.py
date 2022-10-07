import pandas as pd

def clean_district(rawPath, cleanPath):
    df = pd.read_csv(rawPath, sep=";", dtype= {
        "code": "int64",
        "name": "object",
        "region": "object",
        "no. of inhabitants": "int64",
        "no. of municipalities with inhabitants < 499": "int64",
        "no. of municipalities with inhabitants 500-1999": "int64",
        "no. of municipalities with inhabitants 2000-9999": "int64",
        "no. of municipalities with inhabitants > 10000": "int64",
        "ratio of urban inhabitants": "float64",
        "average salary": "int64",
        "unemployment rate 95": "float64",
        "unemployment rate 96": "float64",
        "no. of enterpreneurs per 1000 inhabitants": "float64",
        "no. of commited crimes 95": "int64",
        "no. of commited crimes 96": "int64",
    })

    df.to_csv(cleanPath, sep=",", index=False)