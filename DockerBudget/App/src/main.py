import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import time

from upBank import pullData
from bankDatabase import transactionDatabase


def main():
    # Load in access token for Up Api    
    token_key = os.environ['upKey']
    
    # # Pull account and transaction data
    upApi = pullData(token_key)
    trans_data = upApi.pull_transactions()
    acc_data = upApi.pull_accounts()

    # # Save the transactions and accouint data into an SQL database
    db_interface = transactionDatabase('transactionData')
    db_interface.trans_2_db(trans_data)
    db_interface.acc_2_db(acc_data)


if __name__ == "__main__":        
    main()
        
        