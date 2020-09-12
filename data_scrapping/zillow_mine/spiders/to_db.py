import datetime
from datetime import date, timedelta
import os
import mysql.connector


class db_parse:


    def __init__(self,  data = [], table = [], db = 'rfin_db', user = 'root', port = '3306', ssl='prefer'):
        
        self.data = data
        self.table = table
        self.db = db
        self.host = '127.0.0.1'
        self.user = user
        self.password = 'whore11'
        self.path = os.getcwd() + '\zillow_mine\spiders\sql_queries'
        self.conn = []
        self.cur = []


    def connect(self):
        self.conn = mysql.connector.connect(
            user = 'root',
            host = '127.0.0.1',
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
            host = '127.0.0.1',
            password = self.password,
            database = self.db
        )
        self.conn.autocommit=True
        cur = self.conn.cursor(buffered=True)
        try:
            cur.execute('select date from today')
            datee = cur.fetchone()

            if (date.today() > datee[0].date()):
                print('refreshing T_Y')
                cur.execute('delete from yesterday;')
                cur.execute('INSERT INTO yesterday SELECT * FROM today;')
                cur.execute('delete from today;')
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
    x = db_parse()
    x.connect()
    if x.check_db():
        pass
    x.dc()




