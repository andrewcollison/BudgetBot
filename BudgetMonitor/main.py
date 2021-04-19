import re
import requests 
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import os
import sys
from dotenv import load_dotenv
from datetime import datetime, timedelta

from upBank import pullData
from bankDatabase import transactionDatabase
from dataProcess import processData
from UpEmailNotification import Gmail

sns.set() # set plot style

""" ToDo
1) Data management 
    - Purge print to csv features.                              => DONE
    - Replace it by pulling the data from the sql database.     => DONE
    - Pull data by date range                                   => DONE

2) Add email notification for when script runs correctly. 
    - Send confirmation of script running                       => DONE
    - Include a summary in email
    - Include graph in email of weeks spending 

3) Actual Vs Allowed Expenses
    - Import budget requirements from excel spreadsheet         => DONE
    - Compare acatual spending with budget outlay
    - vialise data for weekly monthly and yearly budget
    - Calulate remaning funds 
    - Email notification when spending exceeds set limit

"""

def main():

    # Load in access token for Up Api
    load_dotenv('UpBankApp.env')
    token_key = os.getenv('api_token')
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    
    # Pull account and transaction data
    upApi = pullData(token_key)
    trans_data = upApi.pull_transactions()
    acc_data = upApi.pull_accounts()

    # Save the trans actiona and accouint data into an SQL database
    db_interface = transactionDatabase('transactionData.db')
    db_interface.trans_2_db(trans_data)
    db_interface.acc_2_db(acc_data)
    
    # Pull from data base
    fd = datetime.now()
    sd = fd + timedelta(days=-60)

    fd = fd.astimezone().isoformat()
    sd = sd.astimezone().isoformat()   

    data = db_interface.pull_from_tran_db(sd, fd)
    df_acc_expenses = processData.acctual_expenses(data)
    df_budget_expenses = processData.budget_expenses()

    # displayData.catData(trans_data)
    
    # Send Email Notification
    # gm = Gmail(email_user, email_pass)
    # gm.send_message('UpApi Update', 'Up Api script run correctly')


if __name__ == "__main__":
    main()