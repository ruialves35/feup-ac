import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# ======== read data set ========
account_data = pd.read_csv("./assets/clean/account.csv")
card_data = pd.read_csv("./assets/clean/card_dev.csv")
client_data = pd.read_csv("./assets/clean/client.csv")
disp_data = pd.read_csv("./assets/clean/disp.csv")
district_data = pd.read_csv("./assets/clean/district.csv")
loan_data = pd.read_csv("./assets/clean/loan_dev.csv")
transaction_data = pd.read_csv("./assets/clean/trans_dev.csv", dtype=
    {"trans_id": str, "account_id": str, "date": str, "type": str, "operation": str, "amount": float, "balance": float, "k_symbol": str, "bank": str, "account": str}
)


# ======== Analyze Size of each Dataset ========
def get_size():
    print("\n\n")
    print("Number of rows for each dataset: \n")
    print(f"Account: {len(account_data)}")
    print(f"Card: {len(card_data)}")
    print(f"Client: {len(client_data)}")
    print(f"Disposition: {len(disp_data)}")
    print(f"District: {len(district_data)}")
    print(f"Loan: {len(loan_data)}")
    print(f"Transaction: {len(transaction_data)}")


# ======== Get missing values ========
def get_missing_values():
    print("\n\n")
    print("Missing values for each dataset: \n")
    print(f"Account: \n{account_data.isnull().sum()} \n")
    print(f"Card: \n{card_data.isnull().sum()} \n")
    print(f"Client: \n{client_data.isnull().sum()} \n")
    print(f"Disposition: \n{disp_data.isnull().sum()} \n")
    print(f"District: \n{district_data.isnull().sum()} \n")
    print(f"Loan: \n{loan_data.isnull().sum()} \n")
    print(f"Transaction: \n{transaction_data.isnull().sum()} \n")

# ======== Use to show more columns if needed ========
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# ======== Analyze paid loans % ========
def analyze_loans():
    print("\n\n")
    paid_loans = loan_data[loan_data["paid"] == 1]
    unpaid_loans = loan_data[loan_data["paid"] == 0]
    paid_loans_percentage = round((len(paid_loans)/len(loan_data)) * 100, 2)
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

# analyze_loans()
# get_size()
get_missing_values()

