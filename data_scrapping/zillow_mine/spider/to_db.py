import datetime
from datetime import date
import os
import pgdb
import psycopg2



class db_parse:

    def __init__(self, table = [], data = [], db = 'zeal', user = 'postgres', port = '5433', ssl='prefer', passw = 'whore11'):
        self.data = data
        self.db = db
        self.host = 'localhost'
        self.user = user
        self.port = port
        self.table = table
        self.sslmode = ssl
        self.password = passw
        self.parameter = {'dbname': self.db, 'user': self.user, 'port': self.port, 'sslmode': self.sslmode}
        self.path = os.getcwd() + '\sql_queries'

    def connect(self):

        myConnection = psycopg2.connect( 
            host=self.host, 
            user=self.user, 
            port = self.port,
            password=self.password, 
            dbname=self.db
        )

        self.doQuery(myConnection)
        myConnection.close()

    def doQuery(self, conn):
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(self.check_table())
        try:
            cur.execute('select dates from today limit 1')
            datee = cur.fetchone()[0]

            print('try1')
            if datetime.date.today() > datee:
                print('date pass')
                cur.execute('delete from yesterday;')
                cur.execute('INSERT INTO yesterday select * from today;')
                cur.execute('delete from today;')
                self.insert_to_table('today', self.data, cur)
            else:
                self.insert_to_table('today', self.data, cur)


        except:
            self.insert_to_table('today', self.data, cur)



    def check_table(self):
        with open(self.path + '\\check_table.sql', 'r') as rf:
            return rf.read()

    def delete_table(self, tabs):
        with open(self.path + '\\delete_table.sql', 'r') as rf:
            return rf.read().format(tab = tabs)

    def retreive(self):
        with open(self.path + '\\retreive.sql', 'r') as rf:
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

    def active(self):
        x = db_parse()
        x.connect()

# if __name__ == '__main__':
#     x = db_parse(table = 0)
#     x.connect()




