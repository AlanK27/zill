
from mine.spiders.spider import crawl
from calc.execute import execute


def run():
    print('starting')
    x = crawl()
    x.initiate()
    y = execute()
    

if __name__ == '__main__':
    run()