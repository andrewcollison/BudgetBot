import os
from dotenv import load_dotenv

from upBank import pullData
from bankDatabase import transactionDatabase
from binanceData import accountData

def main():
    # Load in access token for Up Api      
    load_dotenv('UpBankApp.env')
    token_key = os.getenv('api_token')
    bin_key = str(os.getenv('bin_token'))
    bin_secret = str(os.getenv('bin_secret'))
    
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
    
        
        