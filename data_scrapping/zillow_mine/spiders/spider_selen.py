
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from zillow_mine.spiders.bs4_json import bsj


class crawl:


    def __init__(self, site = 'https://www.redfin.com/city/10201/NV/Las-Vegas/filter/max-days-on-market=1d'):
        self.path = 'C:/chromedriver/chromedriver.exe'
        self.site = site
        self.driver = []

    def next_pg(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'content')))
        try:
            q = self.driver.find_element_by_css_selector("button[class='clickable buttonControl button-text'][data-rf-test-id='react-data-paginate-next']")
            q.click()
            wait = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "address")))
            self.driver.switch_to_window(self.driver.window_handles[0])
            return True
        except:
            return False


    def crawler(self):
        try:

            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "PagingControls")))
            q = self.driver.find_element_by_css_selector("button[class='ModeOption button-text']")
            q.click()
            self.driver.switch_to_window(self.driver.window_handles[0])
            element_addr = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "location")))
            
            
            fg = True

            #check DB condition

            while fg:
                spyder = bsj(page_source = self.driver.page_source)
                spyder.initate()
                fg = self.next_pg()
            self.driver.quit()

        except:
            print('didnt connect')
            exit()

    def initiate(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get(self.site)
        print(self.driver.title)
        self.crawler()

if __name__ == '__main__':
    x = crawl()
    x.initiate()