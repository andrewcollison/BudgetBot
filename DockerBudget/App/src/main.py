import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
from pandas.io.sql import read_sql_query

from upBank import pullData
from bankDatabase import transactionDatabase
from binanceData import accountData

def main():
    # Load in access token for Up Api    
    # token_key = os.environ['upKey']
    # bin_key = os.environ['bin_key']
    # bin_secret = os.environ['bin_secret']
    # bin_key = 'OmkFFB1UaQDx8rAiD5C78bE4JOXw4O9V9xxnY2lN5rP6T8cvY8sYRDA0ANub5f6I'
    # bin_secret = 'etDykKq85CUDP6p0BGNPrOO4E3juffM4YM9QDwUIJVEQ8murJDPcMbm8WgF4kcqg'
    
    load_dotenv('UpBankApp.env')
    token_key = os.getenv('api_token')
    bin_key = str(os.getenv('bin_token'))
    bin_secret = str(os.getenv('bin_secret'))
    print(token_key)
    
    # # Pull account and transaction data
    upApi = pullData(token_key)
    trans_data = upApi.pull_transactions()
    acc_data = upApi.pull_accounts()


    # # Pull Binance Account Data
    binanceApi = accountData(bin_key, bin_secret)
    binanceApi.pull_snapshot()
    binance_data = binanceApi.pull_assets()
    

    # # Save the transactions and accouint data into an SQL database
    db_interface = transactionDatabase('transactionData')
    db_interface.trans_2_db(trans_data)
    db_interface.acc_2_db(acc_data)
    db_interface.binance_2_db(binance_data)


if __name__ == "__main__":        
    main()
    
        
        