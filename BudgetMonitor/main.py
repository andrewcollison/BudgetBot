import re
import requests 
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from upBank import pullData
from bankDatabase import transactionDatabase
from dataVis import displayData
import sqlite3

sns.set() # set plot style

# ToDo
# 1) Remove the print to csv feature. Replace it by pulling the data from the sql database.
#    This allows data to be edited in the database without conflicting.



def main():

    # Load in access token for Up Api
    tokenFile = open('personalToken.txt', 'r')
    token_key =tokenFile.read()
    tokenFile.close()

    # Pull account and transaction data
    upApi = pullData(token_key)
    trans_data = upApi.pull_transactions()
    acc_data = upApi.pull_accounts()

    # Save the trans actiona and accouint data into an SQL database
    db_interface = transactionDatabase('transactionData.db')
    db_interface.trans_2_db(trans_data)
    db_interface.acc_2_db(acc_data)
    
    # Plot spending by sub category
    displayData.catData(trans_data)


if __name__ == "__main__":
    main()