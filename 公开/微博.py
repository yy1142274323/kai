import re, requests, time, json, os
from copyheaders import headers_raw_to_dict
from fake_useragent import UserAgent

t = time.time() * 1000
print(int(t))
url = 'https://weibo.com/aj/mblog/add?ajwvr=6&__rnd={}'.format(int(t))
# headers = {'User-Agent': UserAgent().random}
headers = headers_raw_to_dict(
    b'''
    
    accept: */*
    accept-encoding: gzip, deflate, br
    accept-language: zh-CN,zh;q=0.9
    content-length: 284
    content-type: application/x-www-form-urlencoded
    cookie: login_sid_t=b0905a5b496287044a541a5031638a55; cross_origin_proto=SSL; WBStorage=8daec78e6a891122|undefined; _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=6903081933053.97.1613972296527; SINAGLOBAL=6903081933053.97.1613972296527; ULV=1613972296534:1:1:1:6903081933053.97.1613972296527:; ALF=1645508340; SSOLoginState=1613972340; SUB=_2A25NNzMkDeRhGeFL6lEX9SvEwjiIHXVuRSPsrDV8PUNbmtAKLRn4kW9NQmJq3YK7jVOWimx6G6gFF3s_3N71e2_i; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W59K.ezjoqpiRslQqFvK4CX5JpX5KzhUgL.FoMfeKecSK-R1KB2dJLoIEXLxK.L1KnLB.qLxKqL1KqL12eLxKnL1K5L12eLxKnL1K5L12eLxK-L1KeL1Kzt; wvr=6; wb_view_log_7513655894=1920*10801; webim_unReadCount=%7B%22time%22%3A1613972864007%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A43%2C%22msgbox%22%3A0%7D
    origin: https://weibo.com
    referer: https://weibo.com/u/7513655894/home?topnav=1&wvr=6
    sec-fetch-dest: empty
    sec-fetch-mode: cors
    sec-fetch-site: same-origin
    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36
    x-requested-with: XMLHttpRequest
    
    '''
)

data = {
    'location':' v6_content_home',
    'text':' 777#就挺突然的#',
    'appkey':' ',
    'style_type':' 1',
    'pic_id':'',
    'tid':' ',
    'pdetail':' ',
    'mid':' ',
    'isReEdit':' false',
    'gif_ids':' ',
    'rank':' 0',
    'rankid':' ',
    'module':' stissue',
    'pub_source':' main_',
    'updata_img_num':' 1',
    'pub_type':' dialog',
    'isPri':' null',
    '_t':' 0',

}

res = requests.post(url=url, headers=headers, data=data).text
print(res)
