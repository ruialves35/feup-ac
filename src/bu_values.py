import pandas as pd

# function that reads the values from assets/clean/loan_dev.csv
# and calculates the quantity of paid and not paid loans
def get_loan_values():
  # read the data
  df = pd.read_csv('../assets/clean/loan_dev.csv')
  # calculate the quantity of paid and not paid loans
  paid = df[df['paid'] == 1]
  not_paid = df[df['paid'] == 0]
  # calculate sum the amount column of paid and not paid loans
  paid_sum = paid['amount'].sum()
  not_paid_sum = not_paid['amount'].sum()
  # return the values
  return paid_sum, not_paid_sum

print(get_loan_values())