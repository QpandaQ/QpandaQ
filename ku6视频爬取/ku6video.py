# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : ku6video.py
# Time       ：2023/5/30 19:26
# Author     ：Ppanda
# version    ：python 3.10
# Description：
"""
import json
import uuid
import requests

def down_videos(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
    }
    res = requests.get(url,headers=headers).text
    # 把json字符串编程字典
    dic = json.loads(res)
    for item in dic["data"]:
        video_url = item.get("playUrl","")
        if video_url == "":
            continue
        # video_name = item.get("title","")
        # 爬取视频的数据
        video_data = requests.get(video_url,headers=headers).content
        # wb 写入二进制数据
        # with 表示f对象，使用完毕之后，要从内存里面释放
        # with open(f"video/{video_name}.mp4","wb") as f:
        #   f.write(video_data)
        # uuid.uuid4()产生全球唯一的文件名
        with open(f'video/{uuid.uuid4()}.mp4','wb')as f:
            # f.write(video_data)
            for chunk in video_data.iter_content(trunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

if __name__ == '__main__':
    page_size = int(input('请输入你想要爬取的页数'))
    # 获取所有页的接口地址
    urls = []
    for i in range(page_size):
        url = f'https://www.ku6.com/video/feed?pageNo={i}&pageSize=40'
        urls.append(url)

    # 函数推导式写法, python里面“语法塘”
    # urls = [f'https://www.ku6.com/video/feed?pageNo={i}&pageSize=40' for i in range(page_size)]

    for url in urls:
        down_videos(url)