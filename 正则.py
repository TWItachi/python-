import re

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)
#“\”为转移字符，如果目标匹配字符中本身有.，则使用该符号进行转义