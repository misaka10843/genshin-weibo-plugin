import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import json 
import os
import re
from bs4 import BeautifulSoup
from PIL import Image, ImageFont, ImageDraw
#########################################
#
#防止将修改的文件直接写入而删除文件
#
#########################################

f = open('weibo.json',encoding='utf8') 
   
# returns JSON object as  
# a dictionary 
data = json.load(f)
base_url = 'https://m.weibo.cn/statuses/extend?id=%s' % data['id']
url = requests.get(base_url)
text = url.json()
html_text = text['data']['longTextContent']
html_text = re.sub('<br />', '\n', html_text)
pattern = re.compile(r'<[^>]+>',re.S)
result = pattern.sub('', html_text)


text = result

im = Image.new("RGB", (2000, 800), (255, 255, 255))

dr = ImageDraw.Draw(im)

font = ImageFont.truetype("./msyh.ttc", 18)

dr.text((10, 5), text, font=font, fill="#000000")

im.show()

im.save("/www/wwwroot/网站目录/weibo.png")
#这里填写保存图片的路径，因为好像QPOBot使用lua语言编写的插件不能访问本地路径，所以就直接让插件访问网址来获取图片
#比如你的网站目录名字是baidu，域名是www.baidu.com，IP是192.168.0.123，那么这里填写的就是/www/wwwroot/baidu/weibo.png，
#在weibo-genshin.lua中填写的就可以是http://www.baidu.com/weibo.png 或者http://192.168.0.123/weibo.png

print("now,the new weibo has save to png")