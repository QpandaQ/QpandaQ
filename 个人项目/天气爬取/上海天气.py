# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 上海天气.py
# Time       ：2023/5/15 23:01
# Author     ：Ppanda
# version    ：python 3.10
# Description：
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from pandas import Series, DataFrame
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'
}

for i in range(1,7):
    url = f'https://lishi.tianqi.com/shanghai/20220{i}.html'  # 上海 2022年1月到6月天气
    res = requests.get(url, headers=headers)

    res.encodind = 'utf-8'
    html = BeautifulSoup(res.text, 'html.parser')
    data_all = []
    tian_three = html.find("div", {"class": "tian_three"})
    lishi = tian_three.find_all("li")
    for j in lishi:
        lishi_div = j.find_all("div")
        data = []
        for k in lishi_div:
            data.append(k.text)
        data_all.append(data)

    #print(data_all)
    weather = pd.DataFrame(data_all)
    weather.columns = ["当日信息", "最高气温", "最低气温", "天气", "风向信息"]
    weather_shape = weather.shape
    print(weather)
    weather['当日信息'].apply(str)
    result = DataFrame(
        weather['当日信息'].apply(lambda x: Series(str(x).split(' '))))
    result = result.loc[:, 0:1]
    result.columns = ['日期', '星期']
    weather['风向信息'].apply(str)
    result1 = DataFrame(
        weather['风向信息'].apply(lambda x: Series(str(x).split(' '))))
    result1 = result1.loc[:, 0:1]
    result1.columns = ['风向', '级数']
    weather = weather.drop(columns='当日信息')
    weather = weather.drop(columns='风向信息')
    weather.insert(loc=0, column='日期', value=result['日期'])
    weather.insert(loc=1, column='星期', value=result['星期'])
    weather.insert(loc=5, column='风向', value=result1['风向'])
    weather.insert(loc=6, column='级数', value=result1['级数'])
    weather.to_csv(f"上海{i}月天气.csv", encoding="utf_8")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    weather['最高气温'] = weather['最高气温'].map(lambda x: int(x.replace('℃', '')))
    weather['最低气温'] = weather['最低气温'].map(lambda x: int(x.replace('℃', '')))

    dates = weather['日期']
    highs = weather['最高气温']
    lows = weather['最低气温']

    # 画图

    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)

    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
    # 图表格式
    # 设置图标的图形格式
    plt.title(f'2022年上海{i}月天气情况', fontsize=24)
    plt.xlabel('', fontsize=6)
    fig.autofmt_xdate()
    plt.ylabel('气温', fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    # 修改刻度
    plt.xticks(dates[::5])
    # 显示
    plt.show()
