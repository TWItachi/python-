import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入待翻译的内容(输入q退出程序)：")
    if content == 'q':
        break


    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom']= 'fanyi.web'
    data['typoResult'] = 'false'
    data['ue']= 'utf-8'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    # print(req.headers)
    print(target)
    time.sleep(1)