import requests
from lxml import etree
import time



def get_one_page (url):
   headers = {
      'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
   }
   response = requests.get(url, headers=headers)
   if response.status_code == 200:
      return response.text
   return None


def main(offset):
   url = "https://maoyan.com/board/4?offset=" + str(offset)
   html = get_one_page(url)
   re = etree.HTML(html)
   result = re.xpath('//*[@id="app"]/div/div/div/dl/dd/div/div/div/p/a/text()')
   print(result)


for i in range(10):
   main(offset=i * 10)
   time.sleep(1)

