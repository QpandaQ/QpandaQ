# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 彼岸桌面.py
# Time       ：2023/5/25 13:28
# Author     ：Ppanda
# version    ：python 3.10
# Description：
"""
# 彼岸桌面的爬取
import requests
from lxml import etree
import time
import random
from bs4 import BeautifulSoup
import re
import os
# url = f'http://www.netbian.com/meinv/index_{i}.htm'

# 爬取网页

def load_page(base_url):
    '''

    :param url: 传入的根地址
    :return: 获取网页源代码
    '''
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
    }
    resp = requests.get(base_url, headers=headers,verify=False)
    resp.encoding = resp.apparent_encoding
    return resp.text

# 分析目标页
def load_html(index_url):
    '''

    :param index_url: 目标页url
    :return: 获取页面下的源代码
    '''
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
    }
    resp = requests.get(index_url, headers=headers, verify=False)
    resp.encoding = resp.apparent_encoding
    return resp.text

# 分析根网页
def parse_html(html):
    '''

    :param html:
    :return: 其获取的是每个分页链接
    '''
    items = []
    text = etree.HTML(html)
    for i in range(1,21):
        result = text.xpath(f'//div[@class="list"]/ul/li[{i}]/a/@href')
        items.append(result)
    return items

# 获取目标页下的jpg
def parse_index(html):
    text = etree.HTML(html)
    result = text.xpath(f'//div[@class="pic"]/p/a/img/@src')
    return result

def parse_index_name(html):
    text = etree.HTML(html)
    result = text.xpath(f'//div[@class="pic"]/p/a/img/@title')
    return result

def save_page(name, jpg):
    with open(f'./result/{name}.jpg', 'wb') as f:
        f.write(jpg.content)
        time.sleep(random.random() * 2)

# 主程序
def main(begin,end):
    try:
        for i in range(begin,end):
            if i == 1:
                base_url = 'http://www.netbian.com/meinv/index.htm'
            else:
                base_url = f'http://www.netbian.com/meinv/index_{i}.htm'
            # 获取网页源代码
            html = load_html(base_url)
            # 获取网页数据
            data = parse_html(html)
            data = [ele for ele in data if ele != []]
            for j in range(len(data)-1):
                html_index = f'http://www.netbian.com{data[j][0]}'

                # 目标页的源码
                htm = load_page(html_index)

                jpg = parse_index(htm)
                jpg = jpg[0]
                resp = requests.get(jpg)
                name = parse_index_name(htm)[0]

                save_page(name, jpg = resp)

                print(f'第{i}页{j+1}张已爬取')

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    begin = int(input('请输入开头：'))
    end = int(input('请输入结尾：'))
    main(begin,end)
    print('爬取完成')