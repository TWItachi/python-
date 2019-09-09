from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_thrid = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first, input_second, input_thrid)
browser.close()