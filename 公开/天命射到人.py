import requests,re,time
from lxml import etree
from copyheaders import headers_raw_to_dict
#设置编码，直接设置为UTF8之后，中文显示正常
#html添加这句代码
# <meta charset="utf-8">

import json
import re


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


# 定义要创建的目录
mkpath = "c:/Users/Administrator/Desktop/1"
# 调用函数
mkdir(mkpath)
























w=419
while w<1000:
    print(w)
    url = 'http://www.tingshucloud.com/wp-content/uploads/2020/07/天命赊刀人0{}.mp3'.format(w)
    res = requests.get(url)
    # print(res.content)
    with open(r'c:/Users/Administrator/Desktop/1/{}.mp3'.format(w), 'wb+') as file:  # 保存到本地的文件名
        file.write(res.content)
        
    w+=1














