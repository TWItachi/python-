import requests
import urllib.parse
from lxml import etree
from selenium import webdriver
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}


def getList(url):
    driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    source = driver.page_source

    html = etree.HTML(source)
    xpath = html.xpath('//ul[@class="gl-warp clearfix"]/li')
    for i in xpath:
        a = i.xpath("div/div[4]/a/em/text()")
        b = i.xpath("div/div[3]/strong/i/text()")
        print(a)
        print(b)

if __name__ == '__main__':
    label = "手机"
    label = urllib.parse.quote(label)
    url = "https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&cid2=653&cid3=655&page={}&s=110&click=0"
    num = 0
    for index in range(1, 3, 2):
        u = url.format(label, label, index)
        print(u)
        getList(u)