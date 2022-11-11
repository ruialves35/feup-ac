import pandas as pd

#  get the total amount of loans that were not paid back
def calculateLosses():
  df = pd.read_csv("../../assets/clean/loan_dev.csv")
  df = df[df['paid'] == 0]
  return df['amount'].sum()

def calculateWins():
  df = pd.read_csv("../../assets/clean/loan_dev.csv")
  df = df[df['paid'] == 1]
  return df['amount'].sum()

print(calculateWins())