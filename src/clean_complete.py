import os
import pandas as pd

RAW_PATH = "../assets/complete_raw/"
CLEAN_PATH = "../assets/complete/"

print(f"Cleaning data files inside {RAW_PATH} ...\n")
if not os.path.exists(CLEAN_PATH):
    os.mkdir(CLEAN_PATH)

# Account
account_df = pd.read_csv(RAW_PATH + "account.csv", sep=";")
account_df["frequency"] = account_df["frequency"].replace("POPLATEK MESICNE", "monthly issuance")
account_df["frequency"] = account_df["frequency"].replace("POPLATEK TYDNE", "weekly issuance")
account_df["frequency"] = account_df["frequency"].replace("POPLATEK PO OBRATU", "issuance after transaction")
account_df.to_csv(CLEAN_PATH + "account.csv", sep=";", index=False)

# Card
card_df = pd.read_csv(RAW_PATH + "card.csv", sep=";")
card_df["issued"] = card_df["issued"].apply(lambda x: x.split(' ')[0])
card_df.to_csv(CLEAN_PATH + "card.csv", sep=";", index=False)

# Client
client_df = pd.read_csv(RAW_PATH + "client.csv", sep=";")
client_df.to_csv(CLEAN_PATH + "client.csv", sep=";", index=False)

# Disp
disp_df = pd.read_csv(RAW_PATH + "disp.csv", sep=";")
disp_df.to_csv(CLEAN_PATH + "disp.csv", sep=";", index=False)

# District
district_df = pd.read_csv(RAW_PATH + "district.csv", sep=";")
district_df.columns = ["code", "name", "region", "no. of inhabitants", "no. of municipalities with inhabitants < 499 ", "no. of municipalities with inhabitants 500-1999", "no. of municipalities with inhabitants 2000-9999 ", "no. of municipalities with inhabitants >10000 ", "no. of cities ", "ratio of urban inhabitants ", "average salary ", "unemploymant rate '95 ", "unemploymant rate '96 ", "no. of enterpreneurs per 1000 inhabitants ", "no. of commited crimes '95 ", "no. of commited crimes '96"]
district_df.to_csv(CLEAN_PATH + "district.csv", sep=";", index=False)

# Loan
loan_df = pd.read_csv(RAW_PATH + "loan.csv", sep=";")
loan_df["payments"] = loan_df["payments"].apply(lambda x: int(x))
loan_df["status"] = loan_df["status"].replace("A", 1)
loan_df["status"] = loan_df["status"].replace("B", -1)
loan_df["status"] = loan_df["status"].replace("C", 1)
loan_df["status"] = loan_df["status"].replace("D", -1)
loan_df.to_csv(CLEAN_PATH + "loan.csv", sep=";", index=False)

# Trans
loan_df = pd.read_csv(RAW_PATH + "trans.csv", sep=";")
loan_df["type"] = loan_df["type"].replace("PRIJEM", "credit")
loan_df["type"] = loan_df["type"].replace("VYDAJ", "withdrawal")
loan_df["type"] = loan_df["type"].replace("VYBER", "credit card withdrawal")

loan_df["operation"] = loan_df["operation"].replace("VYBER KARTOU", "credit card withdrawal")
loan_df["operation"] = loan_df["operation"].replace("VKLAD", "credit in cash")
loan_df["operation"] = loan_df["operation"].replace("PREVOD Z UCTU", "collection from another bank")
loan_df["operation"] = loan_df["operation"].replace("PREVOD NA UCET", "remittance to another bank")
loan_df["operation"] = loan_df["operation"].replace("VYBER", "withdrawal in cash")

loan_df["k_symbol"] = loan_df["k_symbol"].replace("SIPO", "household")
loan_df["k_symbol"] = loan_df["k_symbol"].replace("UVER", "loan payment") # NOP
loan_df["k_symbol"] = loan_df["k_symbol"].replace("POJISTNE", "insurrance payment")
loan_df["k_symbol"] = loan_df["k_symbol"].replace("SLUZBY", "payment for statement")
loan_df["k_symbol"] = loan_df["k_symbol"].replace("DUCHOD", "old-age pension")
loan_df["k_symbol"] = loan_df["k_symbol"].replace("UROK", "interest credited")
loan_df["k_symbol"] = loan_df["k_symbol"].replace("SANKC. UROK", "sanction interest if negative balance")

loan_df.to_csv(CLEAN_PATH + "trans.csv", sep=";", index=False)
