import os

from PIL import Image, ImageFont, ImageDraw

text = open('zhenwen.txt',encoding='utf8') 

im = Image.new("RGB", (300, 50), (255, 255, 255))

dr = ImageDraw.Draw(im)

font = ImageFont.truetype(os.path.join("fonts", "msyh.ttc"), 18)

dr.text((10, 5), text, font=font, fill="#000000")

im.show()

im.save("/www/wwwroot/sakurasociety/robotimage/t.png")