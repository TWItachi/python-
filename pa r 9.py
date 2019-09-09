import requests


# data = {'name':'germy', 'age':'22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text) 可以试试
# r = requests.get('http://www.jianshu.com/')

headers = {
    'user-agent': 'Mozilla/5.0'
}

r = requests.get('http://www.jianshu.com', headers=headers)
if r.status_code == 200:
    exit()
else:
    print('Request Successfully')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)