from cleaning.account import clean_account
from cleaning.card_dev import clean_card_dev
from cleaning.client import clean_client
from cleaning.loan_dev import clean_loan_dev
from cleaning.trans_dev import clean_trans_dev
from cleaning.disp import clean_disp
from cleaning.district import clean_district
import os

IS_COMPETITION = True

RAW_PATH = "../assets/raw/"
if not IS_COMPETITION:
    CLEAN_PATH = "../assets/clean/"
    CARD_FILE = "card_dev.csv"
    LOAN_FILE = "loan_dev.csv"
    TRANS_FILE = "trans_dev.csv"
else:
    CLEAN_PATH = "../assets/kaggleClean/"
    CARD_FILE = "card_comp.csv"
    LOAN_FILE = "loan_comp.csv"
    TRANS_FILE = "trans_comp.csv"


print("Cleaning data files inside assets/raw/ ...\n")
if not os.path.exists(CLEAN_PATH):
    os.mkdir(CLEAN_PATH)

print("Cleaning account.csv ...")
clean_account(RAW_PATH + "account.csv", CLEAN_PATH + "account.csv")

print("Cleaning card_dev.csv ...")
clean_card_dev(RAW_PATH + CARD_FILE, CLEAN_PATH + "card_dev.csv")

print("Cleaning disp.csv ...")
clean_disp(RAW_PATH + "disp.csv", CLEAN_PATH + "disp.csv")

print("Cleaning district.csv ...")
clean_district(RAW_PATH + "district.csv", CLEAN_PATH + "district.csv")

print("Cleaning loan_dev.csv ...")
clean_loan_dev(RAW_PATH + LOAN_FILE, CLEAN_PATH + "loan_dev.csv")

print("Cleaning trans_dev.csv ...")
clean_trans_dev(RAW_PATH + TRANS_FILE, CLEAN_PATH + "trans_dev.csv")

print("Cleaning client.csv ...")
clean_client(RAW_PATH + "client.csv", CLEAN_PATH + "client.csv")
