import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



# ======== read data set ========
account_data = pd.read_csv("./assets/clean/account.csv")
card_data = pd.read_csv("./assets/clean/card_dev.csv")
client_data = pd.read_csv("./assets/clean/client.csv")
disp_data = pd.read_csv("./assets/clean/disp.csv", dtype={"disp_id": int, "client_id": int, "account_id": int, "type": str})
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
    print("=============================================\n")
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
    print("=============================================\n")
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
    print("=============================================\n")
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
    print("=============================================\n")
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

# Auxiliary method to join 2 datasets
def join(df1, df2, key1, key2, suff, t="inner"):
    return df1.merge(df2, left_on=key1, right_on=key2, how=t, suffixes=suff)

def analyze_disposition():
    print("=============================================\n")
    print("Number of clients per disposition type:")
    print(disp_data["type"].value_counts())

    sb.displot(disp_data, x="type", hue="type")
    plt.show()

def join_acc_disposition():
    acc_disp = join(account_data, disp_data, "account_id", "account_id", ["", "_disp"])
    # acc_disp.rename(columns={"date": "acc_date"}, inplace=True)

    # Count Groups
    owner_count = acc_disp["account_id"].value_counts()
    acc_disp["is_co-owned"] = acc_disp.apply(lambda row: 1 if owner_count[row["account_id"]] > 1 else 0, axis='columns')
    # Cleanup
    acc_disp.drop(acc_disp[acc_disp["type"] == "DISPONENT"].index, inplace=True)
    acc_disp.drop(columns=["type"], inplace=True)
    ''' TODO: The column "disp_id" might also be useless since it's a 1-1 relation with the account now. But we
     will drop it after proving the correlation between the 2 attributes.'''

    return acc_disp

def join_clients(df : pd.DataFrame):
    df = join(df, client_data, "client_id", "client_id", ["", "_client"], t="left")
    # df.rename(columns={"age": "client_age"}, inplace=True)
    df.drop(['client_id'], axis='columns', inplace=True)
    return df

def join_districts(df : pd.DataFrame):
    df = join(df, district_data, "district_id_client", "code", ["", "_district"], t="inner")
    df.drop(['district_id_client'], axis='columns', inplace=True)

    df = join(df, district_data, "district_id", "code", ["_aDistrict", "_cDistrict"], t="inner")
    df.drop(['district_id'], axis='columns', inplace=True)

    return df

def join_datasets():
    print("============= Joining Datasets =============\n")
    # Joining Accounts with Disposition
    df = join_acc_disposition()
    #print(df.head(10))

    # Joining with Clients
    df = join_clients(df)
    df = join_districts(df)



    print(df)

# ========  ========
# joined_data = account_data.join(loan_data, on='account_id', how='right', lsuffix='_account', rsuffix='_loan')
# print(joined_data)

# analyze_loans()
# get_size()
# get_missing_values()
# check_null_attributes()
# analyze_disposition()
join_datasets()


