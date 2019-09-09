html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class = "title" name = "dormouse"><b>The Dormouse's story</b></p>
<p class = "story">Once upon a time there were three little sisters; and their names were
<a href = "http://example.com/elsie" class ="sister" id = "link1"><!-- Elsie --></a>
<a href = "http://example.com/lacie" class ="sister" id = "link2">Lacie</a> and
<a href = "http://example.com/tillie" class ="sisiter" id = "link3">Tillie</a>;
and they live at the bottom of a well.</p>
<p class = "story">...</p>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())#prettif作用是缩进格式输出，在初始化beautifulsoup时就已经修复错误了
print(soup.title.string)