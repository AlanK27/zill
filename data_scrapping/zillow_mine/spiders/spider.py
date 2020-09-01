
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from zillow_mine.spiders.bs4_json import bsj


class crawl:


    def __init__(self, site = 'https://www.noradarealestate.com/real-estate-investments/'):
        self.path = 'C:/chromedriver/chromedriver.exe'
        self.site = site
        self.driver = []

    def next_pg(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, 'pagination-links')))
        main_id = self.driver.find_element_by_id('pagination-links')
        # print(self.driver.page_source)

        indice = main_id.find_elements_by_tag_name('a')
        for n in indice:
            if 'next' in n.text:
                n.click()
                self.driver.implicitly_wait(7)
                break

        self.driver.switch_to_window(self.driver.window_handles[0])


    def cycle(self):
        # try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'pagination-links')))
            for i in range(4):
                spyder = bsj(self.driver.page_source)
                spyder.initate()
                self.next_pg()
            self.driver.quit()

        # except:
        #     print('didnt connect')
        #     exit()

    def initiate(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get(self.site)
        print(self.driver.title)
        self.cycle()

