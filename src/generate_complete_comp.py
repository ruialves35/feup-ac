import pandas as pd

df = pd.read_csv("../assets/complete/loan.csv", sep=";")
df["status"] = ""
df.to_csv("../assets/raw/loan_complete_comp.csv", sep=";", index=False)
