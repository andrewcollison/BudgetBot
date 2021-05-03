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
import time

from upBank import pullData
from bankDatabase import transactionDatabase
from dataProcess import processData
from UpEmailNotification import Gmail
from disp_data import budget_expenses

sns.set() # set plot style

""" ToDo
1) Data management 
    - Purge print to csv features.                              => DONE
    - Replace it by pulling the data from the sql database.     => DONE
    - Pull data by date range                                   => DONE
    - Update Entries in data base                               => DONE 
    - Create database if none already exists                    => DONE      

2) Add email notification for when script runs correctly. 
    - Send confirmation of script running                       => DONE
    - Include a summary in email                                => DONE
    - Include graph in email of weeks spending                  

3) Actual Vs Allowed Expenses
    - Import budget requirements from excel spreadsheet         => DONE
    - Compare acatual spending with budget outlay               => DONE
    - vialise data for weekly monthly and yearly budget         => DONE
    - Calulate remaning funds 
    - Email notification when spending exceeds set limit

"""

def main():

    # Load in access token for Up Api
    load_dotenv('UpBankApp.env')
    token_key = os.getenv('api_token')
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    
    # # Pull account and transaction data
    upApi = pullData(token_key)
    trans_data = upApi.pull_transactions()
    acc_data = upApi.pull_accounts()

    # # Save the transactions and accouint data into an SQL database
    db_interface = transactionDatabase('transactionData.db')
    db_interface.trans_2_db(trans_data)
    print(trans_data.head(10))
    db_interface.acc_2_db(acc_data)
    
    # Pull from data base
    fd = datetime.now()
    start = fd - timedelta(days=fd.weekday())
    sd = start.replace(hour = 0, minute=0, second=0, microsecond=0).astimezone().isoformat()
    fd = fd.astimezone().isoformat()

    data = db_interface.pull_from_tran_db(sd, fd)

    # Process and analyze data
    process_data = processData()
    df_acc_expenses = process_data.acctual_expenses(data)
    df_budget_expenses = process_data.budget_expenses()


    # Visualize data
    displayData = budget_expenses('weekly')
    displayData.cat_expenses(df_acc_expenses, df_budget_expenses)

    # Send Email Notification
    html_message = pd.DataFrame(df_acc_expenses.reset_index()).to_html()
    gm = Gmail(email_user, email_pass)
    gm.send_message('UpApi Weekly Expenses', html_message)


if __name__ == "__main__":
    main()