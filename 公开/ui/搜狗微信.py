

import requests,json,re,os
from lxml import etree
from copyheaders import headers_raw_to_dict
from urllib.parse import quote

headers = headers_raw_to_dict(

    b'''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: IPLOC=CN2101; SUID=2024A8AF2E08990A000000005FDAB5B6; SUV=1608168887509897; ABTEST=5|1608168889|v1; SNUID=15129D9A353383ABCA501BC3360C44ED; weixinIndexVisited=1; JSESSIONID=aaaioQoBvg5fe6IdWpGzx
    Host: weixin.sogou.com
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: none
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4357.0 Safari/537.36
    
    
    '''


)
# li[1]/div[2]/h3/a[1]/@href

# sr = input('丁输入查询关键词：')

url_wx = 'https://weixin.sogou.com/weixin?query={}&type=2&page=1&ie=utf8'.format('666')
# url_wx = "https://weixin.sogou.com/weixin?query=%E5%91%A8%E6%98%9F%E9%A9%B0&type=2&page=1&ie=utf8"
# print(url_wx)
response = requests.get(url = url_wx,headers = headers).text

pattern = '/(.*?)" id="sogou_vr'

href_list = re.findall(pattern, response)
m = 1

for href in href_list:
    # print(href)

    head = headers_raw_to_dict(
        b'''
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    cache-control: max-age=0
    cookie: pgv_pvi=2327541760; ptui_loginuin=1142274323; RK=J8hlwfyCFD; ptcz=5c9427cbd3f81b138fa15262da04842732f5fe211e0bd8751581a30ddb377b06; eas_sid=G1a6h0d8M0F2e1q406Q3k573y9; pgv_pvid=6270237759; rewardsn=; wxtokenkey=777
    if-modified-since: Thu, 17 Dec 2020 13:50:08 +0800
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: cross-site
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4357.0 Safari/537.36

        '''
    )



    wz = 'https://weixin.sogou.com/'
    lj = wz + href
    print(lj)
    res = requests.get(url = lj,headers = head).text
    print(res)
    # res = res.encode('utf-8')
    #
    #     # print(m)
    # with open('{0}\\{1}.html'.format(666,m),'w') as l:
    #     l.write(str(res))
    #
    # m += 1






































































