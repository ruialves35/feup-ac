from genericpath import exists
from cleaning.account import clean_account
from cleaning.card_dev import clean_card_dev
from cleaning.client import clean_client
from cleaning.loan_dev import clean_loan_dev
from cleaning.trans_dev import clean_trans_dev
from cleaning.disp import clean_disp
from cleaning.district import clean_district
import os

RAW_PATH = "./assets/raw/"
CLEAN_PATH = "./assets/clean/"

print("Cleaning data files inside assets/raw/ ...\n")
if not os.path.exists(CLEAN_PATH):
    os.mkdir(CLEAN_PATH)

print("Cleaning account.csv ...")
clean_account(RAW_PATH + "account.csv", CLEAN_PATH + "account.csv")

print("Cleaning card_dev.csv ...")
clean_card_dev(RAW_PATH + "card_dev.csv", CLEAN_PATH + "card_dev.csv")

print("Cleaning disp.csv ...")
clean_disp(RAW_PATH + "disp.csv", CLEAN_PATH + "disp.csv")

print("Cleaning district.csv ...")
clean_district(RAW_PATH + "district.csv", CLEAN_PATH + "district.csv")

print("Cleaning loan_dev.csv ...")
clean_loan_dev(RAW_PATH + "loan_dev.csv", CLEAN_PATH + "loan_dev.csv")

print("Cleaning trans_dev.csv ...")
clean_trans_dev(RAW_PATH + "trans_dev.csv", CLEAN_PATH + "trans_dev.csv")

print("Cleaning client.csv ...")
clean_client(RAW_PATH + "client.csv", CLEAN_PATH + "client.csv")
