
from zillow_mine.spiders.spider_selen import crawl


def run():
    print('starting')
    x = crawl()
    x.initiate()
    # x = call()
    # x.call()

if __name__ == '__main__':
    run()