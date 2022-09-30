import shutil
from cleaning.account import clean_account
from cleaning.card_dev import clean_card_dev
from cleaning.loan_dev import clean_loan_dev

RAW_PATH = "../assets/raw/"
CLEAN_PATH = "../assets/clean/"

print("Cleaning data files inside assets/raw/ ...\n")

print("Cleaning account.csv ...")
clean_account(RAW_PATH + "account.csv", CLEAN_PATH + "account.csv")

print("Cleaning card_dev.csv ...")
clean_card_dev(RAW_PATH + "card_dev.csv", CLEAN_PATH + "card_dev.csv")

print("Copying disp.csv (no cleaning) ...")
shutil.copy(RAW_PATH + "disp.csv", CLEAN_PATH + "disp.csv")

print("Copying district.csv (no cleaning) ...")
shutil.copy(RAW_PATH + "district.csv", CLEAN_PATH + "district.csv")

print("Cleaning loan_dev.csv ...")
clean_loan_dev(RAW_PATH + "loan_dev.csv", CLEAN_PATH + "loan_dev.csv")
