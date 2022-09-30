from cleaning.account import clean_account
from cleaning.card_dev import clean_card_dev

RAW_PATH = "../assets/raw/"
CLEAN_PATH = "../assets/clean/"

print("Cleaning data files inside assets/raw/ ...\n")

print("Cleaning account.csv ...")
clean_account(RAW_PATH + "account.csv", CLEAN_PATH + "account.csv")
print("Cleaning card_dev.csv ...")
clean_card_dev(RAW_PATH + "card_dev.csv", CLEAN_PATH + "card_dev.csv")
