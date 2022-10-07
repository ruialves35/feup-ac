import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# ======== read data set ========
account_data = pd.read_csv("./assets/clean/account.csv")
loan_data = pd.read_csv("./assets/clean/loan_dev.csv")
card_data = pd.read_csv("./assets/clean/card_dev.csv")

# ======== Get size of datasets ========
def get_size():
    print("\n\n")
    print(f"Client count: {len(account_data)}")
    print(f"Loan count: {len(loan_data)}")
    print(f"Card count: {len(card_data)}")


# ======== Get missing values ========
def get_missing_values():
    print("\n\n")
    print("Missing values: \n", account_data.isnull().sum(), "\n")

# ======== Use to show more columns if needed ========
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# ======== Analyze paid loans % ========
def analyze_loans():
    print("\n\n")
    paid_loans = loan_data[loan_data["paid"] == 1]
    unpaid_loans = loan_data[loan_data["paid"] == 0]
    paid_loans_percentage = (len(paid_loans)/len(loan_data)) * 100
    print(f"{paid_loans_percentage}% of loans are paid.")
    """ Approx 86% of loans have been paid (positive result). This means
    means that accuracy isn't a good metric to optimize for """

    plt.figure()
    plt.bar([0, 1], loan_data["paid"].value_counts(), tick_label=["Paid", "Unpaid"])
    # plt.ylim(0, 300)
    plt.title("Loans paid vs unpaid")
    plt.xlabel("Paid")
    plt.ylabel("Frequency")
    plt.show()


# ========  ========
# joined_data = account_data.join(loan_data, on='account_id', how='right', lsuffix='_account', rsuffix='_loan')
# print(joined_data)

analyze_loans()