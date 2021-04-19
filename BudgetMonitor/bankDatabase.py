import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


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
                                    .format(db_table = self.acc_db_table, dateTime = df.dateTime[i], name = df.name[i], id = df.id[i], value = df.value[i], type = df.type[i])
                    conn.execute(sql_command)
                    conn.commit()
                    conn.close()
                except:
                    print("acc database error: sql input")

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
            # print(df)

            # cursor.execute(sql_command)
            # result = cursor.fetchall()
            # print(result)

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

    db_interface.pull_from_tran_db(sd, fd)

if __name__ == "__main__":
    main()