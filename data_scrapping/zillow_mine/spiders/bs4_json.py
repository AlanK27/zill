
from bs4 import BeautifulSoup
from datetime import date,  timedelta
from zillow_mine.spiders.to_db import db_parse


class bsj:

    def __init__(self, page_source = []):
        self.page_source = page_source
        self.dic = []
        self.data = []


    def stripz(self, inn):
        return inn.strip('$').replace(',','')

    def num_test(self, numb):
        numbz = numb.replace('.','').strip('$')
        if numbz.isnumeric():
            return numb
        else:
            return None

    def extract(self):

        self.dic = []
        soup = BeautifulSoup(self.page_source, 'html.parser')
        divs = soup.find_all("tr", {"class":"tableRow"})

        for sub in divs:
    
            try:
                address = sub.find('a', {'class':'address'}).get_text()
                location =  sub.find('div', {'class':'location'}).get_text()
                price = self.stripz(sub.find('td', {'class':'column column_3 col_price'}).get_text())
                price = self.num_test(price)
                beds = sub.find('td', {'class':'column column_4 col_beds'}).get_text()
                beds = self.num_test(beds)
                baths = sub.find('td', {'column column_5 col_baths'}).get_text()
                baths = self.num_test(baths)
                sqft = self.stripz(sub.find('td', {'class':'column column_6 col_sqft'}).get_text())
                sqft = self.num_test(sqft)
                per_sqft = self.stripz(sub.find('td', {'class':'column column_7 col_ppsqft'}).get_text())
                per_sqft = self.num_test(per_sqft)

                self.dic = [str(date.today()), address, location, price, beds, baths, sqft, per_sqft]
                self.data.append(self.dic)
           
            except:
                pass


    def parse_db(self):
        inser = db_parse(data = self.data)
        inser.initiate()


    def initate(self):
        self.extract()
        self.parse_db()


if __name__ == '__main__':
    x = bsj()
    x.extract()
    x.parse_db()
