
from bs4 import BeautifulSoup
from datetime import date,  timedelta
from zillow_mine.spiders.to_db import db_parse
# from to_db import db_parse

import urllib.request

# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

class bsj:

    def __init__(self, page_source = 0):
        self.page_source = page_source
        self.dic = []
        self.data = []
        self.addrs = 0
        self.bed = 0
        self.sqft = 0
        self.bath = 0
        self.park = 0
        self.price = 0
        self.rental_in = 0
        self.rent = 0
        self.year = 0
        self.price_sq = 0
        self.neighbor = 0
        self.date = 0

    def extract(self):

        self.dic = []
        print('extract')
        soup = BeautifulSoup(self.page_source, 'html.parser')
        # filin = 'C:\\Users\\kai_t\\Desktop\\projects\\zillow\\data_scrapping\\zillow_mine\\spiders\\rental.html'
        # soup = BeautifulSoup(open(filin), features="html.parser")
        
        divs = soup.findAll("div", {"class": "col-md-4"})
        for sub in divs:
            try:
                self.addrs = sub.find('h4', {'class':'card-title'}).get_text()
                md6 = sub.findAll('div', {'class':'col-md-6'})

                col1 = md6[0].findAll('div', {'class':'f_icon_text'})
                self.bed = col1[0].get_text().strip().split()[0]
                self.sqft = col1[1].get_text().strip().split()[0].replace(',', '')

                col2 = md6[1].findAll('div', {'class':'f_icon_text'})
                self.bath = col2[0].get_text().strip().split()[0]
                self.park = col2[1].get_text().strip().split()[0]

                row = sub.findAll('div', {'class':'row f_row'})
                
                col3 = row[0].findAll('h3', {'class':'green-text'})
                self.price = col3[0].get_text().strip().strip('$').replace(',', '')
                self.rental_in = col3[1].get_text().strip().strip('$').replace(',', '')

                col4 = row[1].findAll('h3')
                self.year = col4[0].get_text().strip()
                self.price_sq = col4[1].get_text().strip().strip('$').replace(',', '')

                col5 = row[2].findAll('h3')
                self.neighbor = col5[1].get_text()

                self.dic = [str(date.today()), self.addrs, self.bed, self.sqft, self.bath, self.park, self.price, self.rental_in, self.rent, self.year, self.price_sq, self.neighbor]
                self.data.append(self.dic)

            except:
                pass
       

    def parse_db(self):
        inser = db_parse(data = self.data)
        inser.connect()
        print('parsed to db')

    def initate(self):
        self.extract()
        self.parse_db()





def clean():
    x = bsj()
    x.extract()
    x.parse_db()

if __name__ == '__main__':
    clean()
