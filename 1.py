import re


text = "asasasdd5555"
page = re.match("([A-z]{1,5}).?(\d{4})", text)
if page is not None:
    print(page.group(1))

