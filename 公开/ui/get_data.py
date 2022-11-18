import requests,json,re,os
from lxml import etree
from copyheaders import headers_raw_to_dict
from urllib.parse import quote
from urllib.parse import urlencode


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



# lj = 'https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6cwJThYulHEtVjXrGTiVgS_ZOMvP-Zlui41j5DhYHh0TarROO5wSnO1qXa8Fplpd9hJr7Pjz6t3v19dnici1nYq1X4Y4Jstx2ZIhIR-HqBgyOT3p4pOa9CgIr1Qim3F8tlhbZwLBI0xXTasNilzgWXy-7mfKx5czKTWTj0ktyJ7AC9et_6DZikSbiutC6SAWRQ0j7Kz5YfdKhk_J6VaAYW1vKnCV-Omz2FdPs8udFFluq3X8EKMKOIA..&amp;type=2&amp;query=666&amp;token=DE19127415129D9A353383ABCA501BC3360C44ED5FDAF7EF'
lj = 'https://weixin.sogou.com/weixin?'


data = {
'type': 2,
's_from': 'input',
'query': 666,
'ie': 'utf8',
'_sug_': 'n',
'_sug_type_':''
}



url = lj + urlencode(data)
print(url)





