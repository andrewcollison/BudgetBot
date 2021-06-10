import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from mysql.connector import connect, Error

class transactionDatabase():
    def __init__(self, databaseName):
        self.tran_db_name = databaseName
        self.tran_db_table = 'transactions'
        self.acc_db_table = 'accounts'
        self.db_host = "192.168.0.222"
        self.db_port = 4306
        self.db_usr = "root"
        self.db_pass = "ironman"

        mydb = connect(host=self.db_host, port = self.db_port, user=self.db_usr, password=self.db_pass)
        conn = mydb.cursor()

        create_db_cmd =  "CREATE DATABASE IF NOT EXISTS transactionData;" 
        conn.execute(create_db_cmd)
        
        mydb = connect(host=self.db_host, port = self.db_port, user=self.db_usr, password=self.db_pass, database = self.tran_db_name)
        conn = mydb.cursor()
    # Create table: transactions
        # mydb = connect(host="localhost", user="root", password="ironman", database = 'transactionData')
        conn.execute('''CREATE TABLE IF NOT EXISTS transactions (transactionID VARCHAR(100) PRIMARY KEY ,datetime TIMESTAMP, value DECIMAL(10,2), description VARCHAR(255), parentCategory VARCHAR(255), subCategory VARCHAR(255))''')

        # Create table: accounts
        conn.execute('''CREATE TABLE IF NOT EXISTS accounts \
        (datetime DATETIME, name VARCHAR(255), id VARCHAR(255), value DECIMAL(10,2), type VARCHAR(255))''')
        mydb.commit()
        mydb.close()

            

    def trans_2_db(self, df):
        # Pulls the last 100 transactions and adds them to a database.
        # Only data not already in the database will be entered into the database. The transaction id in the sql database is set to a unique data type        
        # Remove old data and update with most recent
        mydb = connect(host=self.db_host, port = self.db_port, user=self.db_usr, password=self.db_pass, database = self.tran_db_name)
        conn = mydb.cursor()

        try:
            for i in range(len(df['id'])):                     
                sql_delete = "DELETE FROM transactions WHERE transactionID = %s"
                conn.execute(sql_delete, (df.id[i],))
                mydb.commit()
                
        
        except OSError as err:
            print("Database Error: Failed to delete from database")
            print(err)

        try:
            for i in range(len(df['id'])):
                try:
                    sql_command = "INSERT INTO transactions (transactionID, datetime, value, description, parentCategory, subCategory) VALUES (%s, %s, %s, %s, %s, %s);"
                    inst_data = ( df.id[i], df.dateTime[i], df.value[i], df.description[i], df.parentCategory[i], df.subCategory[i])
                    conn.execute(sql_command, inst_data)
                    mydb.commit()
                                        
                except:
                    print("entry already in database")
                    
        except OSError as err:
            print('Database write failed')
            print(err)        

        mydb.close()

    def acc_2_db(self, df):
        # Used to track account balance with time
        mydb = connect(host=self.db_host, port = self.db_port, user=self.db_usr, password=self.db_pass, database = self.tran_db_name)
        conn = mydb.cursor()
        try:
            for i in range(len(df['id'])):
                try:
                    
                    sql_command = "INSERT INTO accounts (dateTime, name, id, value, type)\
                            VALUES (%s, %s , %s, %s, %s)"
                    inst_data = (df.dateTime[i], df.name[i], df.id[i], df.value[i], df.type[i])
                    conn.execute(sql_command, inst_data)
                    mydb.commit()
                    
                except OSError as err:
                    print("acc database error: sql input")
                    print(err)

        except:
            print('Account database write failed')

    # def pull_from_tran_db(self, date_from, date_to):
    #     # Insert code to filter data and pull from database
    #     try:
    #         mydb = connect(host="localhost", user="root", password="ironman", database = self.tran_db_name)
    #         conn = mydb.cursor()
    #         # cursor = conn.cursor()
    #         sql_command = """SELECT * FROM Transactions WHERE DATETIME BETWEEN '{sd}' and  '{fd}'""".format(sd = date_from, fd = date_to)        
    #         df = pd.read_sql(sql_command, con = mydb)
    #         mydb.commit()
    #         mydb.close()
    #     except Error as err:
    #         print("Data retrieval failed")
    #         print(err)

    #     mydb.close()
    #     return df





def main():

    db_interface = transactionDatabase('transactionData')

    # fd = datetime.now()
    # sd = fd + timedelta(days=-7)

    # fd = fd.astimezone().isoformat()
    # sd = sd.astimezone().isoformat()

    # print(db_interface.pull_from_tran_db(sd, fd))

if __name__ == "__main__":
    main()