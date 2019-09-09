import requests

data = {
    'name' : 'germy',
    'age' : 22
}

r = requests.get("http://www.httpbin.org/get", params = data)

print(r.text)
#这个程序主要是改变网址，就是把原来的"http://www.httpbin.org/get"改成"https://www.httpbin.org/get?name=germy&age=22"
#利用data去改变访问的网址
