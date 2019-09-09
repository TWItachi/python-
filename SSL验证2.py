import requests

respone = requests.get('https://www.12306.cn', verify=False)
print(respone.status_code)