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

    def connect(self):
    
        conn = mysql.connector.connect(
            user = 'root',
            host = '127.0.0.1',
            password = self.password,
            database = self.db
        )
        conn.autocommit=True
        print('conn connected')
        self.query(conn)
        conn.close()

    def query(self, conn):
        cur = conn.cursor(buffered=True)
        try:
            cur.execute('select date from today')
            datee = cur.fetchone()
  

            if ((date.today() + timedelta(days=1)) > datee[0].date() ):
                print('new data to today')
                cur.execute('delete from yesterday;')
                cur.execute('INSERT INTO yesterday SELECT * FROM today;')
                cur.execute('delete from today;')
                self.insert_to_table('today', self.data, cur)
                self.insert_to_table('main', self.data, cur)
            else:
                print('already scrapped today')
                pass
            
        except:
            print('nvm, fresh insert')
            self.insert_to_table(table='today', data=self.data, cur=cur)
            self.insert_to_table('main', self.data, cur)


    def insert_to_table(self, table, data, cur):
        with open(self.path + '\\insert.sql', 'r') as rf:
            query = rf.read().format(tab = table)

        print('insert query')
        for d in data:   
            cur.execute(query, d)


if __name__ == '__main__':
    x = db_parse()
    x.connect()




