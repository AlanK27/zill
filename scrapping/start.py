
from mine.spiders.spider import crawl
from calc.execute import execute
from apscheduler.schedulers.blocking import BlockingScheduler

def run():
    print('starting')
    x = crawl()
    x.initiate()
    y = execute()
    

if __name__ == '__main__':
    run()
    scheduler = BlockingScheduler()
    scheduler.add_job(run, 'interval', hours =24)
    scheduler.start()