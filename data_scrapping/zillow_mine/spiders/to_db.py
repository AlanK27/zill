import datetime
from datetime import date
import os
import mysql.connector


class db_parse:


    def __init__(self, table = [], data = [], db = 'zillwow', user = 'root', port = '3306', ssl='prefer'):
        self.data = data
        self.db = db
        self.host = '127.0.0.1'
        self.user = user
        self.password = []
        self.path = os.getcwd() + '\zillow_mine\spiders\sql_queries'

    def connect(self):
        print('connecting')
        print(self.password)
        if len(self.password) < 2:
            self.password = input('server pw:')
            
        cnx = mysql.connector.connect(
            user = 'root',
            host = '127.0.0.1',
            password = self.password,
            database = 'testbase'
        )
        cnx.autocommit=True
        print('cnx connected')
        # mycursor = cnx.cursor()
        # with open(self.path + '\\initiate_table.sql', 'r') as f:
        #     result = mycursor.execute(f.read(), multi=True)
        self.query(cnx)
        cnx.close()

    def query(self, conn):
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS zill (dates date,addrs varchar(150),bedroom int,sqft int,bathroom int,parking int,price float(2),rental_in float(2),year int,price_sq float(2),neighbor varchar(5));')
        cur.execute('CREATE TABLE IF NOT EXISTS today (dates date,addrs varchar(150),bedroom int,sqft int,bathroom int,parking int,price float(2),rental_in float(2),year int,price_sq float(2),neighbor varchar(5));')
        cur.execute('CREATE TABLE IF NOT EXISTS yesterday (dates date,addrs varchar(150),bedroom int,sqft int,bathroom int,parking int,price float(2),rental_in float(2),year int,price_sq float(2),neighbor varchar(5));')
        cur.execute('CREATE TABLE IF NOT EXISTS main (dates date,addrs varchar(150),bedroom int,sqft int,bathroom int,parking int,price float(2),rental_in float(2),year int,price_sq float(2),neighbor varchar(5));')
        
  
        try:
            cur.execute('select dates from today limit 1')
            datee = cur.fetchone()[0]
            if datetime.date.today() > datee:
                cur.execute('delete from yesterday;')
                cur.execute('INSERT INTO yesterday SELECT * FROM today;')
                cur.execute('delete from today;')
                self.insert_to_table('today', self.data, cur)
            else:
                self.insert_to_table('today', self.data, cur)
                #impliment check_dups
        except:
            self.insert_to_table('today', self.data, cur)


    def check_table(self):
        with open(self.path + '\\initiate_table.sql', 'r') as rf:
            return rf.read()

    def delete_table(self, tabs):
        with open(self.path + '\\delete_table.sql', 'r') as rf:
            return rf.read().format(tab = tabs)

    def retreive(self):
        with open(self.path + '\\retreive.sql', 'r') as rf:
            return rf.read()

    def check_dup(self):
        with open(self.path + '\\check_dups.sql', 'r') as rf:
            return rf.read()


    def insert_to_table(self, table, data, cur):
        with open(self.path + '\\insert.sql', 'r') as rf:
            quer = rf.read().format(tab = table)

        for d in data:
            cur.execute(quer, d)
        cur.execute('insert into main select * from {tab};'.format(tab = table))


    def operation(self):
        with open(self.path + '\\operation.sql', 'r') as rf:
            return rf.read()

    def test(self):
        with open(self.path + '\\test.sql', 'r') as rf:
            return rf.read()

if __name__ == '__main__':
    x = db_parse()
    x.connect()




