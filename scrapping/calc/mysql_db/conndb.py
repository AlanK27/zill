import datetime
from datetime import date, timedelta
import os
import mysql.connector


class conndb:


    def __init__(self, db = 'rfin_db', user = 'root', port = '3306', ssl='prefer'):
        self.db = db
        self.host = '127.0.0.1'
        self.user = user
        self.password = '1111five'
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


    def test_connection(self):
        self.connect()
        self.disconnect()


if __name__ == '__main__':
    x = db_parse()
    x.test_connection()



