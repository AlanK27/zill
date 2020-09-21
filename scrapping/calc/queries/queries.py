import os
from calc.mysql.conn import conn


class query(conn):


    def __init__(self):
        super().__init__()
        self.path = os.getcwd() + "\calc\queries\queries"

    def del_dups(self):

        with open(self.path + '\\del_dups_main.sql',  'r') as rf:
            query = rf.read().split(';')
        for comm in query:
            self.cur.execute(comm)

    def weekly(self):

        with open(self.path + '\\weekly.sql',  'r') as rf:
            query = rf.read().split(';')
        for comm in query:
            self.cur.execute(comm)


    def monthly(self, months):
      
        with open(self.path + '\\monthly.sql',  'r') as rf:
            query = rf.read().split(';')
        for comm in query:
            self.cur.execute(comm.format(months))


    def initiate(self):
        self.connect()
        self.del_dups()
        self.weekly()
        self.monthly(1)
        self.monthly(6)
        self.disconnect()