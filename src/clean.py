from cleaning.account import clean_account

RAW_PATH = "../../assets/raw/"
CLEAN_PATH = "../../assets/clean/"

print("Cleaning data files inside assets/raw/ ...\n")

print("Cleaning account.csv ...")
clean_account(RAW_PATH + "account.csv", CLEAN_PATH + "account.csv")
