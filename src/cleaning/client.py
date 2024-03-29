import pandas as pd

def clear_month(date):
  month = int(date[2:4])
  if ( month > 50 ):
    return "19" + date[0:2] + "-" + str(int(date[2:4]) - 50).zfill(2) + "-" + date[4:]
  else:
    return "19" + date[0:2] + "-" + str(month).zfill(2) + "-" + date[4:]


def clean_client(rawPath, cleanPath):
  df = pd.read_csv(rawPath, sep=";", dtype= {
    "client_id": "int64",
    "birth_number": "object",
    "district_id": "int64",
  })

  # format birth_number and add gender column
  df["birth_number"] = df["birth_number"].astype(str)
  df["gender"] = df["birth_number"].apply(lambda date: 0 if int(date[2:4]) > 50 else 1)
  df["birth_number"] = df["birth_number"].apply(clear_month)

  df.to_csv(cleanPath, sep=",", index=False)  

