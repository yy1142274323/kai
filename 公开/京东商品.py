import requests
from fake_useragent import UserAgent
from lxml import etree



headers = {'User-Agent': UserAgent().random}
url = 'https://search.jd.com/Search?keyword=卫衣&page=1&s=56&click=0'
res = requests.get(url = url,headers=headers).text
print(res)
html = etree.HTML(res)
tp = html.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/@href')
# print(tp)
for i in tp:
    print(i)


