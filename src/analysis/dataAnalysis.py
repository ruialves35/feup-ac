import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# ======== read data set ========
account_data = pd.read_csv("./assets/clean/account.csv")
card_data = pd.read_csv("./assets/clean/card_dev.csv")
client_data = pd.read_csv("./assets/clean/client.csv")
disp_data = pd.read_csv("./assets/clean/disp.csv", dtype={"disp_id": str, "client_id": str, "account_id": str, "type": str})
district_data = pd.read_csv("./assets/clean/district.csv")
loan_data = pd.read_csv("./assets/clean/loan_dev.csv")
transaction_data = pd.read_csv("./assets/clean/trans_dev.csv", dtype=
    {"trans_id": str, "account_id": str, "date": str, "type": str, "operation": str, "amount": float, "balance": float, "k_symbol": str, "bank": str, "account": str}
)

def parse_k_symbol(k_symb):
    if isinstance(k_symb, float):
        return 'none'
    elif k_symb == " ":
        return 'none'
    else:
        return k_symb


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

    # TODO: Fix missing values 'disposition' and 'district'

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


# ======== Investigate attributes with a large quantity of nulls (operation, k_symbol, bank and account) ========
def check_null_attributes():
    print("\n\n")
    print("[Operation]:")
    print(transaction_data["operation"].value_counts())
    operationNullsPercentage = round(len(transaction_data[transaction_data["operation"].isnull()]) / len(transaction_data["operation"]) * 100, 2)
    print(f"Nulls (%): {operationNullsPercentage}%")
    ''' The operation attribute is categorical and doesn't reveal an inherited order. It can be encoded with 3 attributes
    using binary encoding. We will fill the 'nulls' with "unknown"
    '''

    transaction_data['operation'].fillna("unknown", inplace=True)
    # print(transaction_data["operation"].value_counts())

    print("\n[k_symbol]:")
    # print(transaction_data["k_symbol"].value_counts())
    ''' The k_symbol attribute is categorical and doesn't reveal an inherited order. It can be encoded with 3 attributes
    using binary encoding. We will replace the " " with "none"
    '''

    transaction_data["k_symbol"] = transaction_data["k_symbol"].apply(parse_k_symbol)
    print(transaction_data["k_symbol"].value_counts())
    k_symbol_none_percentage = round(len(transaction_data[transaction_data["k_symbol"] == "none"]) / len(transaction_data["k_symbol"]) * 100, 2)
    print(f"Nulls (%): {k_symbol_none_percentage}%")


    print("\n[bank]:")
    #print(transaction_data["bank"].value_counts())
    print("Number of unknown banks:", len(transaction_data[transaction_data['bank'].isnull()]))

    print("\n[account]:")
    # print(transaction_data["account"].value_counts())
    print("Number of unknown partners:", len(transaction_data[transaction_data['account'].isnull()]) + len(transaction_data[transaction_data['account'] == "0"]))

    rows = transaction_data[transaction_data["bank"].isnull() & (~transaction_data["account"].isnull()) & (transaction_data["account"] != "0")]
    print(f"Number of rows where bank is empty and the account isn't: {len(rows)}")
    '''This proves that these 2 feature are highly correlated. Although these 2 attributes aren't likely to contribute anything to our prediction, we can create an
    "unknown" bank and set all unknown account attributes to 0.'''

    transaction_data["account"].fillna(0, inplace=True)
    transaction_data["bank"].fillna("unknown", inplace=True)




# ========  ========
# joined_data = account_data.join(loan_data, on='account_id', how='right', lsuffix='_account', rsuffix='_loan')
# print(joined_data)

# analyze_loans()
# get_size()
# get_missing_values()
check_null_attributes()

