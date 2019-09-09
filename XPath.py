from lxml import etree
text = '''
<div>
<ul>
<li class='item-0'><a href="link1.html">first item</a></li>
<li class='item-1'><a href="link2.html">second item</a></li>
<li class='item-inactive'><a href="link3.html">third item</a></li>
<li class='item-1'><a href="link.html">fourth item</a></li>
<li class='item-0'><a href="link1.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
#tostring()方法修正html代码
#结果是bytes类型，转换成str型