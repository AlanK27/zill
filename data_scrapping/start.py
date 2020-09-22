
from zillow_mine.spiders.spider_selen import crawl
from db_calc.execute import calc_execute


def run():
    print('starting')
    x = crawl()
    x.initiate()
    y = calc_execute()
    

if __name__ == '__main__':
    run()