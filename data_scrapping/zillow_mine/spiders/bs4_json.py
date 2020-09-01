
from bs4 import BeautifulSoup
from datetime import date,  timedelta
from zillow_mine.spiders.to_db import db_parse


class bsj:

    def __init__(self, page_source = 0):
        self.page_source = page_source
        self.dic = []
        self.data = []

    def extract(self):

        self.dic = []
        soup = BeautifulSoup(self.page_source, 'html.parser')
        
        divs = soup.findAll("div", {"class": "col-md-4"})
        for sub in divs:
            try:
                addrs = sub.find('h4', {'class':'card-title'}).get_text()
                md6 = sub.findAll('div', {'class':'col-md-6'})

                col1 = md6[0].findAll('div', {'class':'f_icon_text'})
                bed = col1[0].get_text().strip().split()[0]
                sqft = col1[1].get_text().strip().split()[0].replace(',', '')

                col2 = md6[1].findAll('div', {'class':'f_icon_text'})
                bath = col2[0].get_text().strip().split()[0]
                park = col2[1].get_text().strip().split()[0]

                row = sub.findAll('div', {'class':'row f_row'})
                
                col3 = row[0].findAll('h3', {'class':'green-text'})
                price = col3[0].get_text().strip().strip('$').replace(',', '')
                rental_in = col3[1].get_text().strip().strip('$').replace(',', '')

                col4 = row[1].findAll('h3')
                year = col4[0].get_text().strip()
                price_sq = col4[1].get_text().strip().strip('$').replace(',', '')

                col5 = row[2].findAll('h3')
                neighbor = col5[1].get_text()

                self.dic = [str(date.today()), addrs, bed, sqft, bath, park, price, rental_in, year, price_sq, neighbor]
                self.data.append(self.dic)
            except:
                pass
       

    def parse_db(self):
        inser = db_parse(data = self.data)
        inser.connect()

    def initate(self):
        self.extract()
        self.parse_db()


# if __name__ == '__main__':
#     x = bsj()
#     x.extract()
#     x.parse_db()
