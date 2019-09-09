from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">item</a></li>
'''
html = etree.HTML(text)


result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
result = html.xpath('//li[contains(@class, "li-first") and @name="item"]/a/text()')
print(result)