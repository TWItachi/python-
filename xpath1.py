from lxml import etree

html = etree.parse('test.txt', etree.HTMLParser())



result = etree.tostring(html)
print(result.decode('utf-8'))
print()
result = html.xpath('//*')
print(result)
print()
print(result[0])
print()
result = html.xpath('//li')
print(result)
print()
result = html.xpath('//li/a')
print(result)
print()
result = html.xpath('//li/a/@href')
print(result)
result = html.xpath('//li[@class="li"]/a/text()')#无法匹配li和li-first
print(result)