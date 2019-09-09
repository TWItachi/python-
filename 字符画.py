# coding=gbk

from PIL import Image
img = Image.open(r"C:\Users\datongmusheren\Desktop\6.jpg")
out = img.convert("L")
 

width,height = out.size
zoom = float(input())
vscale = float(input())

out = out.resize((int(width * zoom),int(height * zoom * vscale)))
asciis = "#@$&=+,."
texts = ""
for row in range(int(height* zoom)):
	for col in range(int(width* zoom *vscale)):
		gray = out.getpixel((col,row))
		texts += asciis[int(gray / 270 * 8)]
	texts += "\n"

with open(r'C:\Users\datongmusheren\Desktop\a.txt' , "w") as file:
	file.write(texts)
