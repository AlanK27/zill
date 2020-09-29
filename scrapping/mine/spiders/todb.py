import datetime
from datetime import date, timedelta
import os
from os import listdir
import mysql.connector


class parse:


    def __init__(self,  data = [], table = [], db = 'rfin_db', user = 'root', port = '3306', ssl='prefer'):
        
        self.data = data
        self.table = table
        self.db = db
        self.host = '127.0.0.1'
        self.user = user
        self.password = '1111five'
        self.path = os.getcwd() + '\mine\spiders\sql_queries'
        self.conn = []
        self.cur = []


    def connect(self):
        self.conn = mysql.connector.connect(
            user = 'root',
            password = self.password,
            database = self.db
        )
        self.cur = self.conn.cursor(buffered=True)
        print('conn connected')


    def disconnect(self):
        self.conn.commit()
        self.conn.close()


    def query(self):
        self.insert_to_table(table='today', data=self.data)
        self.insert_to_table(table='main', data=self.data)


    def insert_to_table(self, table, data):
        with open(self.path + '\\insert.sql', 'r') as rf:
            query = rf.read().format(tab = table)
        for d in data:   
            self.cur.execute(query, d)

    def check_db(self):
        self.conn = mysql.connector.connect(
            user = 'root',
            password = self.password,
        )
        cur = self.conn.cursor(buffered=True)
        print('conn connected')

        with open(self.path + '\\initiate_table.sql', 'r') as rf:
            query = rf.read().split(';') 
        for squ in query:
            cur.execute(squ)

        try:
            cur.execute('select max(date) from today')
            datee = cur.fetchone()
            print(date.today())
            print(datee[0])
            if (date.today() > datee[0]):
                print('refreshing T_Y')
                with open(self.path + '\\operation.sql', 'r') as rf:
                    query = rf.read().split(';') 
                for squ in query:
                    cur.execute(squ)
                return True
            else:
                print('already scrapped today')
                return False
        
        except:
            print('fresh insert')
            return True


    def initiate(self):
        self.connect()
        self.query()
        self.disconnect()


if __name__ == '__main__':
    x = parse()
    x.connect()
    if x.check_db():
        pass
    x.disconnect()




