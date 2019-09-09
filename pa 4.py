import urllib.request

url = 'http://www.baidu.com/'

response = urllib.request.urlopen(url)

html = response.read()

html = html.decode('UTF-8')

with open('baidu.txt', 'w', encoding='utf-8') as wb:
    for a in html:
        wb.write(a)

open('baidu.txt')

print(html)