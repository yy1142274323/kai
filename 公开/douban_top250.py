import requests,json
from copyheaders import headers_raw_to_dict
from lxml import etree
# requests = requests.sessions
#requests.session():维持会话,可以让我们在跨请求时保存某些参数


url = 'https://movie.douban.com/top250?start=0&filter='

headers = headers_raw_to_dict(
    b'''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: bid=Ey0upcr49GY; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1602754297%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D9VH_lPwYtaxXjsEdsFUtk0u-b7ZAGrMi8X5aNV1cRhPQGejxmSYZ_6ue2KdzK2Ul%26wd%3D%26eqid%3Df713004400000ebb000000025f8816f5%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.965679797.1602754297.1602754297.1602754297.1; __utmb=30149280.0.10.1602754297; __utmc=30149280; __utmz=30149280.1602754297.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1848900239.1602754297.1602754297.1602754297.1; __utmc=223695111; __utmz=223695111.1602754297.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __yadk_uid=iWPZjPHaiuEfn4f8QXFON7wwfGFM2nw5; __gads=ID=4628125feb5eb248-2235ff5c1bc4009c:T=1602754299:RT=1602754299:S=ALNI_Ma0JqD1n-HuDGURaAfqQsLSmRERKA; _pk_id.100001.4cf6=6bef604db0c48b3c.1602754297.1.1602754340.1602754297.; __utmb=223695111.4.10.1602754297
    Host: movie.douban.com
    Pragma: no-cache
    Referer: https://movie.douban.com/top250?start=50&filter=
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: same-origin
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36
    
    
    
    '''
)


response=requests.get(url=url,headers=headers,timeout=10)
response.encoding = 'utf-8'
i = response.content
# print(i)
html = etree.HTML(i)
# print(html)
html = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
# print(html)
for r in html:
    # print(r)
    name = r.xpath('div/div[2]/div[1]/a/span[1]/text()')[0].strip()
    print(name)
    with open('电影名字.txt','a+') as f:
        f.write(name+'\n')



