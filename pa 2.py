import requests
import re

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",

    "Referer": "http://fanyi.youdao.com/"
}

data = {
    "i": "i love mikasa",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15519659438256",
    "sign": "8d1ba324a44151449b21137ac7536d72",
    "ts": "1551965943825",
    "bv": "363eb5a1de8cfbadd0cd78bd6bd43bee",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
}


response = requests.post(url, headers=headers, data=data)

text = response.text

comname = re.compile('.*?"tgt":"(.*?)"}]]}')

lin = re.search(comname, text)

print(lin.groups(1))