import requests


r = requests.get("http://www.httpbin.org/get")
#print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))