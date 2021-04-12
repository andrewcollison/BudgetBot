import sqlite3
import pandas as pd
import numpy as np



class transactionDatabase():
    def __init__(self, databaseName):
        self.tran_db_name = databaseName
        self.tran_db_table = 'transactions'
        self.acc_db_table = 'accounts'

    def trans_2_db(self, df):
        # Pulls the last 100 transactions and adds them to a database.
        # Only data not already in the database will be entered into the database. The transaction id in the sql database is set to a unique data type
        try:
            for i in range(len(df['id'])):
                try:
                    conn = sqlite3.connect(self.tran_db_name)
                    sql_command = "INSERT INTO {db_table}(transactionID, datetime, value, description, parentCategory, subCategory)\
                            VALUES ('{id}', '{dateTime}', '{value}', '{description}',\
                                '{parentCategory}', '{subCategory}')"\
                                    .format(db_table = self.tran_db_table, id = df.id[i], dateTime = df.dateTime[i], value = df.value[i], description = df.description[i],\
                                        parentCategory = df.parentCategory[i], subCategory = df.subCategory[i])
                    conn.execute(sql_command)
                    conn.commit()
                    conn.close()
                except:
                    print("entry already in database")

        except:
            print('Database write failed')

    def acc_2_db(self, df):
        # Used to track account balance with time
        try:
            for i in range(len(df['id'])):
                try:
                    conn = sqlite3.connect(self.tran_db_name)
                    sql_command = "INSERT INTO {db_table}(dateTime, name, id, value, type)\
                            VALUES ('{dateTime}', '{name}' , '{id}', '{value}', '{type}')"\
                                    .format(db_table = self.acc_db_table, dateTime = df.dateTime[i], name = df.name[i], id = df.id[i], value = df.balance[i], type = df.type[i])
                    conn.execute(sql_command)
                    conn.commit()
                    conn.close()
                except:
                    print("acc database error: sql input")

        except:
            print('Account database write failed')
        

    def pull_from_db(self):
        # Insert code to filter data and pull from database
        pass