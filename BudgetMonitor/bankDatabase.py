import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import sys


class transactionDatabase():
    def __init__(self, databaseName):
        self.tran_db_name = databaseName
        self.tran_db_table = 'transactions'
        self.acc_db_table = 'accounts'

        if os.path.isfile(databaseName):
            print ("Databse detected")
        else:
            print ("Creating Database")
            # Create Database
            conn = sqlite3.connect(self.tran_db_name)
            c = conn.cursor()

            # Create table: transactions
            c.execute('''CREATE TABLE Transactions \
             ([transactionID] text PRIMARY KEY,[datetime] date, [value] integer, [description] text, [parentCategory] text, [subCategory] text)''')
   
            # Create table: accounts
            c.execute('''CREATE TABLE accounts \
             ([datetime] date, [name] text, [id] text, [value] integer, [type] text)''')

            conn.commit()    

    def trans_2_db(self, df):
        # Pulls the last 100 transactions and adds them to a database.
        # Only data not already in the database will be entered into the database. The transaction id in the sql database is set to a unique data type        
        # Remove old data and update with most recent
        conn = sqlite3.connect(self.tran_db_name)

        try:
            for i in range(len(df['id'])):                     
                sql_delete = "DELETE FROM transactions WHERE transactionID = ?"
                conn.execute(sql_delete, (df.id[i],))
                conn.commit()
                # conn.close()
        
        except OSError as err:
            print("Database Error: Failed to delete from database")
            print(err)

        try:
            for i in range(len(df['id'])):
                try:
                    sql_command = "INSERT INTO transactions (transactionID, datetime, value, description, parentCategory, subCategory) VALUES (?, ?, ?, ?, ?, ?);"
                    inst_data = ( df.id[i], df.dateTime[i], df.value[i], df.description[i], df.parentCategory[i], df.subCategory[i])
                    conn.execute(sql_command, inst_data)
                    conn.commit()
                    # conn.close()                    
                except:
                    print("entry already in database")
                    
        except OSError as err:
            print('Database write failed')
            print(err)

        

        conn.close()

    def acc_2_db(self, df):
        # Used to track account balance with time
        try:
            for i in range(len(df['id'])):
                try:
                    conn = sqlite3.connect(self.tran_db_name)
                    sql_command = "INSERT INTO {db_table}(dateTime, name, id, value, type)\
                            VALUES ('{dateTime}', '{name}' , '{id}', '{value}', '{type}')"\
                                    .format(db_table = self.acc_db_table, dateTime = df.dateTime[i], name = df.name[i], id = df.id[i], value = df.value[i], type = df.type[i])
                    conn.execute(sql_command)
                    conn.commit()
                    conn.close()
                except OSError as err:
                    print("acc database error: sql input")
                    print(err)

        except:
            print('Account database write failed')

    def pull_from_tran_db(self, date_from, date_to):
        # Insert code to filter data and pull from database
        try:
            conn = sqlite3.connect(self.tran_db_name)
            # cursor = conn.cursor()
            sql_command = """SELECT * FROM {db_table} WHERE DATETIME BETWEEN '{sd}' and '{fd}'"""\
                .format(db_table = self.tran_db_table, sd = date_from, fd = date_to)
                
            df = pd.read_sql(sql_command, conn)
            conn.commit()
            conn.close()

        except OSError as err:
            print("Data retrieval failed")
            print(err)


        return df





def main():

    db_interface = transactionDatabase('transactionData.db')

    fd = datetime.now()
    sd = fd + timedelta(days=-7)

    fd = fd.astimezone().isoformat()
    sd = sd.astimezone().isoformat()

    print(db_interface.pull_from_tran_db(sd, fd))

if __name__ == "__main__":
    main()