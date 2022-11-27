import pandas as pd
import matplotlib.pyplot as plt

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

# function that barplots with the values of paid and not paid loans
def plot_loan_values(paid, not_paid):
  # change colors of the bars
  plt.bar(['paid', 'not paid'], [paid, not_paid], color=['green', 'red'])

  for i, v in enumerate([paid, not_paid]):
    plt.text(i, v, str(v), color='black', ha='center')
  
  # set the title
  plt.title('Loan Success')

  # set the x and y labels
  plt.ylabel('Loan value (M/CZK)')

  # show the plot
  plt.show()

paid, not_paid = get_loan_values()
paid, not_paid = [round(paid / 1000000, 1), round(not_paid / 1000000, 1)]

plot_loan_values(paid, not_paid)