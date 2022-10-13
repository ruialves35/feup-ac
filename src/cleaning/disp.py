import pandas as pd

def clean_disp(rawPath, cleanPath):
  df = pd.read_csv(rawPath, sep=";", dtype= {
      "disp_id": "int64",
      "client_id": "int64",
      "account_id": "int64",
      "type": "object",
  })

  # print(df.dtypes)
  df.to_csv(cleanPath, sep=",", index=False)
  