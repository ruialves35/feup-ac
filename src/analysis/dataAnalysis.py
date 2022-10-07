import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# ======== read data set ========
account_data = pd.read_csv("./assets/clean/account.csv")


# ======== Get dataset size ========
print(f"The dataset size is {len(account_data)}")


# ======== Get missing values ========
print("Missing values: \n", account_data.isnull().sum(), "\n")


# ========  ========
