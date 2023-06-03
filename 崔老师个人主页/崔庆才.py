# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 3.py
# Time       ：2023/5/31 18:48
# Author     ：Ppanda
# version    ：python 3.10
# Description：
"""
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.wei、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63',
    'X-Requested-With': 'XMXLHttpRequest',
}


def get_page(since_id=None):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'since_id': since_id
    }
    url = base_url+urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json = response.json()
            items = json.get('data').get('cardlistInfo')
            next_since_id = items['since_id']
            return (json, next_since_id)
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['text'] = pq(item.get('text')).text() # 为了方便检测，这里只爬取了微博的标题
            yield weibo

def main():
    for i in range(10):
        if i == 0:
            print("第{}页".format(i+1))
            tuple_since_id = get_page()
            results = parse_page(tuple_since_id[0])
            for result in results:
                print(result['text'])
        else:
            print("第{}页".format(i+1))
            tuple_since_id = get_page(tuple_since_id[1])
            results = parse_page(tuple_since_id[0])
            for result in results:
                print(result['text'])

if __name__ == '__main__':
    main()