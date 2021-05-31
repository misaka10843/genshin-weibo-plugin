import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import json 
import os


#########################################
#
#防止将修改的文件直接写入而删除文件
#
#########################################

path = './weibo.txt'  # 文件路径
if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(path) 


#########################################
#
#获取weibo正文及相关数据
#
#########################################

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/6593199887',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest', #设置请求为Ajax
}
max_page = 1

#模拟Ajax请求
def get_page(page):
    params = {
        'type': 'uid',
        'value': '6593199887',
        'containerid': '1076036593199887',
        'page': page
    }
    url = base_url + urlencode(params) #合成完整的URL
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200: #判断响应的状态码
            return response.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)
#解析并提取信息
def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog', {})
                weibo = {}
                weibo['id'] = item.get('id')
                yield weibo

if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        doc=open("weibo.txt","a",encoding='utf8')
        for result in results:
            print(result,file=doc)
        doc.close() 