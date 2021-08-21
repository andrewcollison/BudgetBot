import pandas as pd
from datetime import datetime
from binance.spot import Spot
from datetime import datetime
from currencyExchange import usd2aud

class accountData():
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        
    def pull_snapshot(self):
        # pulls account snapshot that is updated daily  
        client = Spot()
        client = Spot(key=self.key, secret=self.secret)

        accSnap = client.account_snapshot("SPOT")
        accTotalBTC = accSnap['snapshotVos'][0]['data']['totalAssetOfBtc']
        getBTCPrice = client.avg_price("BTCUSDT")
        accValueUSD = float(accTotalBTC)*float(getBTCPrice['price'])
        
    def pull_assets(self):
        # Pulls a list of assets from binance wallet.
        # Calculates wallet value in USD
        client = Spot()
        client = Spot(key=self.key, secret=self.secret)
        accSnap = client.account()
        accHoldings = accSnap['balances']
        dataList = []   
        for i in range(len(accHoldings)):
            if float(accHoldings[i]['free']) > 0 :
                asset = accHoldings[i]['asset']
                free = accHoldings[i]['free']
                locked = accHoldings[i]['locked']
                time = accSnap['updateTime']
                time = datetime.now().astimezone().isoformat()                
                assetString = asset+"USDT"
                usdMktValue = client.avg_price(assetString)
                usdValue = float(usdMktValue['price'])*float(free)                
                audValue = usd2aud(usdValue)
                dataItem = {
                    'time': time,
                    'asset': asset,
                    'free': str(free),
                    'locked': str(locked),
                    'USD': str(usdValue),
                    'AUD': str(audValue)            
                }
                dataList.append(dataItem)            
        
        df = pd.DataFrame(dataList)
        
        return df

        




            






