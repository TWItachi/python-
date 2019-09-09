import requests

r = requests.get("http://www.taobao.com", timeout = 1)
print(r.status_code)
