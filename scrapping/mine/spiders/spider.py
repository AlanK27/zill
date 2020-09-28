
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mine.spiders.bs4 import bsj
from mine.spiders.todb import parse
import os
import time


class crawl:


    def __init__(self, site = 'https://www.redfin.com/city/10201/NV/Las-Vegas/filter/max-days-on-market=1d'):
        self.path = os.getcwd() + '\mine\driver\chromedriver.exe'
        self.site = site
        self.driver = []


    def crawler(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "PagingControls")))
        q = self.driver.find_element_by_css_selector("button[class='ModeOption button-text']")
        q.click()
        self.driver.switch_to_window(self.driver.window_handles[0])
        element_addr = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "location")))
        fg = True
        while fg:
            spyder = bsj(page_source = self.driver.page_source)
            spyder.initate()
            fg = self.next_pg()
        self.driver.quit()


    def next_pg(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.ID, 'content')))
        try:
            q = self.driver.find_element_by_css_selector("button[class='clickable buttonControl button-text'][data-rf-test-id='react-data-paginate-next']")
            q.click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "address")))
            self.driver.switch_to_window(self.driver.window_handles[0])
            return True
        except:
            return False


    def db_check(self):
        conn = parse()
        fg = conn.check_db()
        conn.disconnect()
        return fg


    def initiate(self):
        if self.db_check():
            print('db check pass')
            self.driver = webdriver.Chrome(self.path)
            self.driver.get(self.site)
            print(self.driver.title)
            self.crawler()
            
        else:
            print('scrap was done already')


if __name__ == '__main__':
    x = crawl()
    x.db_check()
    x.initiate()