














# 视频

'https://v9-xg-web-s.ixigua.com/673dc0ac79ef0dfa0109028e10aac0e7/5fdc3613/video/tos/cn/tos-cn-vd-0026/64d666a938a345929d75b2b33d6366ac/media-video-avc1/'
'https://v9-xg-web-s.ixigua.com/3174b2158c2d07b7b5bed77da5fe4057/5fdc3969/video/tos/cn/tos-cn-o-0004/9e68346e49354c42be7f2aca259ee4e3/media-video-avc1/'


# 视频页面
'https://www.ixigua.com/6903832917760279053/'



'https://www.ixigua.com/api/videov2/author/video?author_id=95767439500&type=video&max_time=1602239073&_signature=_02B4Z6wo00f01GtjttAAAIBA06XIj2O9EGRrYrJAAEUJ18'
'https://www.ixigua.com/api/videov2/author/video?author_id=95767439500&type=video&max_time=0&_signature=_02B4Z6wo00f01oycgkQAAIBCNFr8G9dhSQqMnYbAAP0K18'


# 主页
'https://www.ixigua.com/home/95767439500'





import requests,json,re
from copyheaders import headers_raw_to_dict




def zy ():

    headers = headers_raw_to_dict(

        b'''
    
    
        cookie: ttwid=1%7Cx4HvU-AP9QmysZSJuwBCtux1bKfncNCL9os2sAYtD70%7C1608256613%7C70d8f296188f4ed91547e01bf49b4d9e8bea2f75ff0e7a19b9d679c8aaa7503f; ixigua-a-s=0; MONITOR_WEB_ID=cfb80add-92e1-4b9d-a13e-e2eb30f68310; Hm_lvt_db8ae92f7b33b6596893cdf8c004a1a2=1608256616; _ga=GA1.2.1351546768.1608256617; _gid=GA1.2.1648611662.1608256617; Hm_lpvt_db8ae92f7b33b6596893cdf8c004a1a2=1608259053
        referer: https://www.ixigua.com/home/95767439500
        sec-fetch-dest: empty
        sec-fetch-mode: cors
        sec-fetch-site: same-origin
        tt-anti-token
        user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    
    
        '''

    )

    url = 'https://www.ixigua.com/api/videov2/author/video?author_id=95767439500'

    response = requests.get(url = url , headers = headers).text
    response = json.loads(response)
    res = response['data']['data']
    print(res)
    for li in res:
        # name = li['abstract']
        lj_url = li['display_url']
        pattern = 'group/(.*?)/'
        url_id = re.findall(pattern,lj_url)[0]
        # print(url_id)

        shipin_lj = 'https://www.ixigua.com/{}'.format(url_id)

        # print(shipin_lj)
        url_jx = 'https://jx.muzzz.cn/api/dsp/32C3D946380DCD222C5B55243B2F00FC88A3123D2C17F25816/1/?url={}'.format(shipin_lj)
        r = requests.get(url_jx).text
        r = json.loads(r)
        write = r['data']['url']
        name = r['data']['title']
        s = requests.get(url = write).content
        # print(write)
        # print(r)
        with open('视频\\{}.mp4'.format(name), 'wb') as l:
            l.write(s)
zy()




'https://www.ixigua.com/6906818467320726030/'
'http://toutiao.com/group/6906818467320726030/'


# '1602239073'    2020-10-09 18:24:33
# '1596366055'    2020-08-02 19:00:55
# '1592214638'    2020-06-15 17:50:38
# '1587741625'    2020-04-24 23:20:25
