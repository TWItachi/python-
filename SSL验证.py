import requests
respone =  requests.get('http://www.12306.cn')
print(respone.status_code)