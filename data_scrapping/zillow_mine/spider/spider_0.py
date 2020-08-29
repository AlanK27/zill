
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


path = 'C:/chromedriver/chromedriver.exe'
# site = 'https://www.zillow.com/homes/las-vegas_rb/'
site = 'https://cafend.net/'
# locale = 'Las Vegas'
driver = webdriver.Chrome(path)

driver.get(site)
print(driver.title)


try:
    # main = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'actionbar-inline srp-page-container zsg-layout_full responsive-search-page nav-full-width tengage wide znav-search-bar map-visible')))
    

    main = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'howl-iconpicker-outer')))
    print(main.text)

    # spider function here (.................)

    # head = driver.find_element_by_id('menu-menu-1')
    # print(head)
    # m = head.find_elements_by_tag_name('a')
    # print(m)
    # for n in m:
    #     if n.text == 'Coffee':
    #         n.click() 
    #         break

    head1 = driver.find_element_by_id('custom_html-18')
    print(head1)
    head = head1.find_elements_by_tag_name('a')
    print(head)
    for n in head:
        n.click()
        break


except:
    print('didnt reach')




# class io:

#     def __init__(self, name, pay):
#         self.name = name
#         self.age = []
#         self.pay = pay

#     @classmethod
#     def from_meaning(cls, stru):
#         name, ids, pay = stru.split('-')
#         # cls.ids = ids
#         return cls(name, pay)

#     @classmethod
#     def raises(cls, amount):
#         cls.raise_amount = amount

#     def pri(self):
#         print(self.name, self.ids, self.pay)

# kid = 'John-120522-25.99'

# x2 = io(1,2)
# x2.raises(90)
# print(x2.raise_amount)

# x = io.from_meaning(kid)
# print(x.ids)
# print(x.name)
# print(x.pay)