import re
import requests 
import json
import pandas as pd
import numpy as np
import datetime

class pullData():
    def __init__(self, token_key):
        self.token = 'Bearer ' + token_key
        self.my_headers = {'Authorization': self.token}
        
    def pull_accounts(self):        
        response = requests.get("https://api.up.com.au/api/v1/accounts", headers = self.my_headers).json()
        
        acc_id = []
        acc_name = []
        acc_value = []
        acc_type = []
        time_now = datetime.datetime.now().astimezone().isoformat()
        acc_time = []
        for i in range(len(response['data'])):
            acc_id.append(response['data'][i]['id'])
            acc_name.append(response['data'][i]['attributes']['displayName'])
            acc_value.append(response['data'][i]['attributes']['balance']['value'])
            acc_type.append(response['data'][i]['attributes']['accountType']) 
            acc_time.append(time_now)

        d = {'name': acc_name, 'id': acc_id, 'value': acc_value, 'type': acc_type, 'dateTime': acc_time}
        df = pd.DataFrame(d)
        # df.to_csv('upBankData_acc.csv')
        # print(df)
        return df

    def pull_transactions(self):
        response = requests.get("https://api.up.com.au/api/v1/transactions/?page[size]=100", headers = self.my_headers).json()
        
        ids = []
        value = []
        date_settled = []
        parent_cat = []
        sub_cat = []
        vendor = []
        for i in range(len(response['data'])):
            ids.append(response['data'][i]['id'])
            value.append(response['data'][i]['attributes']['amount']['value'])
            date_settled.append(response['data'][i]['attributes']['createdAt'])
            vendor.append(response['data'][i]['attributes']['description'])

            try:
                parent_cat.append(response['data'][i]['relationships']['parentCategory']['data']['id'])
                sub_cat.append(response['data'][i]['relationships']['category']['data']['id'])
            except:
                parent_cat.append("None")
                sub_cat.append("None")           
        
        d = {'id': ids, 'dateTime': date_settled, 'value': value, 'description': vendor, 'parentCategory': parent_cat, 'subCategory': sub_cat}
        df = pd.DataFrame(d)
        # df.to_csv('upBankData.csv')
        # print(df)
        return df