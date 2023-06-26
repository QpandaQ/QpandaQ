# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 新闻.py
# Time       ：2023/5/16 14:48
# Author     ：Ppanda
# version    ：python 3.10
# Description：
"""
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import csv


csvfile = open('新闻.csv', mode='w', newline='', encoding='utf-8')
fieldnames = ['文章标题', '文章链接', '文章内容', '发布时间']
write = csv.DictWriter(csvfile, fieldnames=fieldnames)
write.writeheader()

for i in range(1,11):

    url = f'https://www.gdust.edu.cn/news/syyw/{i}.html'


    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text,'lxml')
    title_url_Date=soup.find('ul',class_='article').find_all('li')
    # print(title_url_Date)

    for j in title_url_Date:
        # print(i)
        # url地址
        url = j.find('a')['href']

        # url详情页
        url_main = requests.get(f'https://www.gdust.edu.cn/{url}')
        url_main.encoding = url_main.apparent_encoding

        # 详情页内容
        url_soup = BeautifulSoup(url_main.text,'lxml')
        url_main_detail = url_soup.find('div',class_='content').text
        url_main_detail = re.sub(r'[\s]+', '', url_main_detail)

        # 标题
        title = j.find('a').text

        # 日期
        date = j.find('span', class_='date').text

        # item = {
        #     "文章标题": title,
        #     "文章链接": f'https://www.gdust.edu.cn{url}',
        #     "文章内容": url_main_detail,
        #     '发布时间': date,
        # }

        write.writerow({'文章标题': title, "文章链接": f'https://www.gdust.edu.cn{url}',"文章内容": url_main_detail, '发布时间': date})
    print(f'第{i}页已爬取！')
    time.sleep(random.random() * 3)

csvfile.close()