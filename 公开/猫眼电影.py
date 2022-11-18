import requests,json
from copyheaders import headers_raw_to_dict
from lxml import etree

for i in range(10):
    print('当前采集的是第{}页'.format(i+1))

    url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
    hea = headers_raw_to_dict(
        b'''
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Cache-Control: no-cache
        Connection: keep-alive
        Cookie: __mta=142514701.1602231410466.1602231410466.1602231596389.2; uuid_n_v=v1; uuid=C67C5D200A0711EBBE7821F615C5DCCD6792A727EB7F4EF29175475CA1536999; _csrf=7895f89c56de2ac3f632d5b886affe6e58352e952250e2ad8d77d1cbd5112fb5; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1602231410; _lxsdk_cuid=1750c6f1ec8c8-0989f7805d3e24-c781f38-100200-1750c6f1ec8c8; _lxsdk=C67C5D200A0711EBBE7821F615C5DCCD6792A727EB7F4EF29175475CA1536999; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1602231596; _lxsdk_s=1750c6f1ec9-b76-58f-44d%7C%7C7
        Host: maoyan.com
        Pragma: no-cache
        Referer: https://maoyan.com/board/1
        Sec-Fetch-Dest: document
        Sec-Fetch-Mode: navigate
        Sec-Fetch-Site: same-origin
        Sec-Fetch-User: ?1
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36
        
        
        
        '''
    )


    r = requests.get(url=url,headers = hea).text
    # x = json.loads(r)
    # print(r)
    html = etree.HTML(r)
    html1 = html.xpath('//*[@id="app"]/div[1]/div[1]/div[1]/dl/dd')
    # print(html)
    for i in html1:
        # print(i)
        name = i.xpath('div/div/div[1]/p[1]/a/text()')[0].strip()
        dy = i.xpath('div/div/div[1]/p[2]/text()')[0].strip()
        print(name,dy)
        with open('qqq.txt','a+') as f:
            f.write(name)



    '''
    result = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    
    for res in result:
        # print(res)                                    #索引第几个  strip() 去除空格和换行    
        name = res.xpath('div/div/div[1]/p[1]/a/text()')[0].strip()    
        actor = res.xpath('div/div/div[1]/p[2]/text()')[0].strip()
        print(name, actor)
    '''