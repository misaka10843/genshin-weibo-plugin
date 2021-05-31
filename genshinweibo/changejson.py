
import sys
import re
import os

from shutil import copyfile
import json
#########################################
#
#防止将修改的文件直接写入而删除文件
#
#########################################

path = './weibo.json'  # 文件路径
if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(path) 


#########################################
#
#规范json语法并且只提取第一行数据
#
#########################################

f1 = open('./weibo.txt','r+',encoding='utf8')
f2 = open('./weibo.json','w+',encoding='utf8')

lines = f1.readlines() 
first_line = lines[1] 
str1=r"'"
str2=r'"'
for ss in first_line:
    tt=re.sub(str1,str2,ss)
    f2.write(tt)
f1.close()
f2.close()


f3 = open('./weibo.json','r+',encoding='utf8')
f4 = open('./weibo1.json','r+',encoding='utf8')
earlier = json.load(f3) 
later = json.load(f4)

if earlier['id'] != later['id']:
    print(os.system("sh runafter.sh"))
    copyfile("./weibo.json", "./weibo1.json")
    print("have new weibo")
else:
    print("no new weibo")