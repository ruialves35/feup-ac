import pandas as pd

import sys
sys.path.append('../')

from src.analysis.utils import predictColumnLR

def clean_district(rawPath, cleanPath):
    df = pd.read_csv(rawPath, sep=";", dtype= {
        "code ": "int64",
        "name ": "object",
        "region": "object",
        "no. of inhabitants": "int64",
        "no. of municipalities with inhabitants < 499": "int64",
        "no. of municipalities with inhabitants 500-1999": "int64",
        "no. of municipalities with inhabitants 2000-9999": "int64",
        "no. of municipalities with inhabitants >10000 ": "int64",
        "ratio of urban inhabitants ": "float64",
        "average salary ": "int64",
        "no. of enterpreneurs per 1000 inhabitants ": "float64",
    })

    df.rename(columns=lambda x: x.strip(), inplace=True)
    df.rename(columns={
        "no. of inhabitants": "num_inhabitants", 
        "no. of municipalities with inhabitants < 499": "municip499",
        "no. of municipalities with inhabitants 500-1999": "municip500_1999",
        "no. of municipalities with inhabitants 2000-9999": "municip2000_9999",
        "no. of municipalities with inhabitants >10000": "municip10000",
        "no. of cities": "num_cities",
        "ratio of urban inhabitants": "urban_ratio",
        "average salary": "avg_salary",
        "unemploymant rate '95": "unemp_rate95",
        "unemploymant rate '96": "unemp_rate96",
        "no. of enterpreneurs per 1000 inhabitants": "num_entrepreneurs",
        "no. of commited crimes '95": "num_crimes95",
        "no. of commited crimes '96": "num_crimes96",
    }, inplace=True)

    # TODO: num_crimes95 has some values as "?". We need to change them so that we can convert to int

    # Replace "?" occurrences by an empty string
    df["unemp_rate95"] = df["unemp_rate95"].replace("?", "")
    df["unemp_rate96"] = df["unemp_rate96"].replace("?", "")
    df["num_crimes95"] = df["num_crimes95"].replace("?", None).replace("none", None)
    df = predictColumnLR(df, "num_crimes95", ["num_inhabitants", "municip499", "municip500_1999", "municip2000_9999", "municip10000", "num_cities","urban_ratio", "avg_salary", "num_entrepreneurs", "num_crimes95", "num_crimes96"])
    df["num_crimes96"] = df["num_crimes96"].replace("?", "")
    df['num_crimes95'] = pd.to_numeric(df['num_crimes95'], errors='coerce').astype('float64')
    df['num_crimes96'] = pd.to_numeric(df['num_crimes96'], errors='coerce').astype('float64')
    df["num_crimes95_ratio"] = 1000 * df["num_crimes95"] / df["num_inhabitants"]
    df["num_crimes96_ratio"] = 1000 * df["num_crimes96"] / df["num_inhabitants"]

    df.to_csv(cleanPath, sep=",", index=False)