import pandas as pd

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
        "ratio of urban inhabitants": "urban_ratio",
        "average salary": "avg_salary",
        "unemploymant rate '95": "unemp_rate95",
        "unemploymant rate '96": "unemp_rate96",
        "no. of enterpreneurs per 1000 inhabitants": "num_entrepreneurs",
        "no. of commited crimes '95": "num_crimes95",
        "no. of commited crimes '96": "num_crimes96",
    }, inplace=True)

    # Replace "?" occurrences by an empty string
    df["unemp_rate95"] = df["unemp_rate95"].replace("?", "")
    df["unemp_rate96"] = df["unemp_rate96"].replace("?", "")
    df["num_crimes95"] = df["num_crimes95"].replace("?", "")
    df["num_crimes96"] = df["num_crimes96"].replace("?", "")


    df.to_csv(cleanPath, sep=",", index=False)