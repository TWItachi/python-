import requests



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url = "https://movie.douban.com/chart"
r = requests.get(url)
r.encoding = "utf-8"

print(r.text)