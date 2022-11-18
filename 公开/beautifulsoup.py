# -*- coding = utf-8 -*-
# @Time : 2020/10/10 14:29
# @Author : 阿斌
# @File : d.py
# @Software : PyCharm
import requests
from bs4 import BeautifulSoup
from copyheaders import headers_raw_to_dict

header = headers_raw_to_dict(
    b'''
    Cookie: ll="118123"; bid=TR3WIuu_vQk; __utma=30149280.84619639.1606094971.1606094971.1606094971.1; __utmc=30149280; __utmz=30149280.1606094971.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1606094971; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1606094976%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; _vwo_uuid_v2=D272FC469DF3F13E83C00B02A020A2D84|693863dc4ca2d6178f58d10b0e4d69b7; __yadk_uid=vqE2QmZk0S6HXhgbJlRFJRbvMsucZQ85; __utma=223695111.1659943777.1606094976.1606094976.1606095014.2; __utmb=223695111.0.10.1606095014; __utmz=223695111.1606095014.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=98d3f1d61e7d7516.1606094976.1.1606095416.1606094976.Host: movie.douban.com
    Referer: https://movie.douban.com/top250?start=25&filter=
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36
    '''
)

url = 'https://movie.douban.com/top250?start=0&filter='
html = requests.get(url = url , headers = header)
html = requests.get(url = url)
print(html.text)
html.encoding = "UTF-8"
soup = BeautifulSoup(html.text,'lxml')
print(soup.prettify())           #返回源代码
print(soup.prettify()) # 格式化html结构

print(soup.title) # 获取title标签的名称
print(soup.title.name) # 获取title的name
print(soup.title.string) # 获取head标签的所有内容
# print(soup.head)
# print(soup.div)  # 获取第一个div标签中的所有内容
# print(soup.div["id"]) # 获取第一个div标签的id的值

# print(soup.find_all("a")) # 获取所有的a标签
# print(soup.find(id="u1")) # 获取id="u1"
# print(soup.a)
# print(soup.a.attrs)  ## 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
#
# #还可以利用get方法，传入属性的名称，二者是等价的
# print(soup.a['class']) # 等价 bs.a.get('class')
#
# # 可以对这些属性和内容等等进行修改
# soup.a['class'] = "newClass"
# print(soup.a)
#
# # 还可以对这个属性进行删除
# del soup.a['class']
# print(soup.a)



for item in soup.find_all(""):
    print(item)
    # print(item.get("href")) # 获取所有的a标签，并遍历打印a标签中的href的值
# for item in soup.find_all("a"):
#     print(item.get_text())
#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)
#content > div > div.article > ol > li:nth-child(2) > div > div.info > div.hd > a > span.title
#content > div > div.article > ol > li:nth-child(3) > div > div.info > div.hd > a > span:nth-child(1)

# name = soup.select('#content > div > div.article > ol > li:nth-child(2) > div > div.info > div.hd > a > span.title')
#
# print(name)

#content > div > div.article > ol > li:nth-child(1) > div > div.info > div.hd > a > span:nth-child(1)






