
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from bs4_json import bsj


class spider:


    def __init__(self):
        self.path = 'C:/chromedriver/chromedriver.exe'
        self.site = 'https://www.noradarealestate.com/real-estate-investments/'
        self.driver = []

    def next_pg(self, drive):
        main_id = drive.find_element_by_id('pagination-links')
        print(main_id)
        n = main_id.find_elements_by_tag_name('a')
        for nn in n:
            if nn.text == 'next »':
                nn.click()
        self.driver = drive.switch_to_window(driver.window_handles[1])
        driver.implicitly_wait(7)

    def cycle(self):
        try:
            driver.implicitly_wait(7) # need to change to EC
            for i in range(3):
                bsj.ex(self.driver)
                self.next_pg()
                
        except:
            print('didnt connect')
            exit()

    def initiate(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get(self.site)
        print(self.driver.title)

        self.cycle()

