from selenium import webdriver

bo = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
bo.get('https://www.baidu.com')
bo.find_element_by_id('a')
bo.close()