from lxml import etree

text = '''
<div>
<ul>
<li class='item-0'><a href="link1.html">first item</a></li>
<li class='item-1'><a href="link2.html">second item</a></li>
<li class='item-inactive'><a href="link3.html">third item</a></li>
<li class='item-1'><a href="link4.html">fourth item</a></li>
<li class='item-0'><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[2]/attribute::*')#这里attribute意为‘属性’，故这里匹配的是以一个li列表中下的class属性
print(result)
result = html.xpath('//li[1]/child::a[@href = "link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')#当前节点后的所有节点*表示匹配所有节点，*后面2表示匹配后续第2个节点
print(result)
result = html.xpath('//li[1]/following-sibling::*')#following-sibling表示匹配后面所有同级节点
print(result)