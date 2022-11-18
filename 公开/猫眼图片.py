# -*- coding = utf-8 -*-
# @Time : 2020/10/10 11:42
# @Author : 阿斌
# @File : 猫眼图片.py
# @Software : PyCharm



import requests, json
from copyheaders import headers_raw_to_dict
from lxml import etree

url = 'https://maoyan.com/board/4?offset=0'

head = headers_raw_to_dict(
    b'''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: __mta=142514701.1602231410466.1602297507438.1602301238385.22; uuid_n_v=v1; uuid=C67C5D200A0711EBBE7821F615C5DCCD6792A727EB7F4EF29175475CA1536999; _lxsdk_cuid=1750c6f1ec8c8-0989f7805d3e24-c781f38-100200-1750c6f1ec8c8; _lxsdk=C67C5D200A0711EBBE7821F615C5DCCD6792A727EB7F4EF29175475CA1536999; _csrf=32b948491bb9d1796c96ec63d23bf950a04bb0579e2b90ad88e403cd31ba6211; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1602231410,1602291224; __mta=142514701.1602231410466.1602292368600.1602292373618.7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1602301238; _lxsdk_s=17510988a5d-647-f8e-e23%7C%7C3
    Host: maoyan.com
    Pragma: no-cache
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: cross-site
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36



    '''
)
r = requests.get(url=url,headers=head).text
# print(r)
html = etree.HTML(r)
print(html)
tp = html.xpath('//*[@id="app"]/div[1]/div[1]/div[1]/dl/dd')
print(tp)
for i in tp:
    pic = i.xpath('a/img[2]/@data-src')[0][:-16]
    print(pic)
    # print(i)
    j = requests.get(url = pic).content
    mz = tp.index(i)
    with open('111\\{}.jpg'.format(mz+1),'wb') as l:
        l.write(j)

for m in range(100):
    print(m+1)




# a_list = ['a','b','c','d','e','f']
#
# n = a_list[1]
# print(n)
#
# m = a_list.index('b')
# print(m)


