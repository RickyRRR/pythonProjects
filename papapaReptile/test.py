# from selenium import webdriver
# browser = webdriver.Chrome()
#
# browser.get("https://www.baidu.com/")
# print(browser.current_url)

import lxml
from selenium import webdriver
import  pyquery

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)


# browser = webdriver.PhantomJS()
# browser.get('https://www.baidu.com')
# print(browser.current_url)