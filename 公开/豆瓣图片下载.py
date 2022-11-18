import requests, json
from copyheaders import headers_raw_to_dict
from lxml import etree



# aaaurl = 'https://www.readnovel.com/book/22102399000135202'
#
# headers = headers_raw_to_dict(
#     b'''
#     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
#     Accept-Encoding: gzip, deflate, br
#     Accept-Language: zh-CN,zh;q=0.9
#     Cache-Control: max-age=0
#     Connection: keep-alive
#     Cookie: _csrfToken=TKeKeNNmJufcdeDJfxPqJVWkx0Ij9vaRxT9PRGHB; newstatisticUUID=1602222297_464862462
#     Host: www.readnovel.com
#     Referer: https://www.readnovel.com/book/22102399000135202
#     Sec-Fetch-Dest: document
#     Sec-Fetch-Mode: navigate
#     Sec-Fetch-Site: same-origin
#     Sec-Fetch-User: ?1
#     Upgrade-Insecure-Requests: 1
#     User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
#
#
#     '''
# )
#
# r = requests.get(url = aaaurl, headers = headers).text
# print(r)

# data = {"orderType":0,"afterSaleType":1,"remarkStatus":-1,"urgeShippingStatus":-1,"groupStartTime":1594441161,"groupEndTime":1602217161,"pageNumber":2,"pageSize":20}

# print(type(data))
# print(type(json.dumps(data)))

# r = requests.post(url = aaaurl, headers = headers, data = json.dumps(data)).text

# res = r.status_code



# print(r)

# a = {'aa':'bb', 'cc':'dd'}
#
# b = a['aa']
#
# print(b)
#
# city_name = result['data']

# lis = ['a','s','d','f','g','h']
#
# a = lis[3]
#
# print(a)

'''格式化  format'''
# s_time = ''
# e_time = ''
# a = 'fjiksagdjikghsdaoihgoisda{0}hoi{1}'.format(s_time,e_time)
# print(a)
# cook = 'gyugyjgiyugyyuigi'
#
# headers = {
#     'cookie': '{}'.format(cook),
#     'a':'b'
# }

# n = [binary message: \x08\xa9\x88\xa5\xc7\x01\x10\x9f\xf2\x9a\xd5\xa2\xca\x90\x9e\x16\x18\x91N \x012\x00:\x02pbB\xcb\x05\x08\xf4\x03\x10\x00\x18\x00"\x00(\x012\x93\x05\xa2\x1f\x8f\x05\x12 1:1:92868149435:3271763264289960\x18\x01 \x01*\xcb\x04\n 1:1:92868149435:3271763264289960\x10\x01\x18\xae\x80\xd9\x82\x91\x80\xfe\x02 \x89\xe4\x86\x9f\xfe\xa6\xec\x02(\x87\x82\x80\xc6\xae\xbf\xd4\xb8_0\xe8\x078\xbb\x81\xfe\xfa\xd9\x02B\x06ZhidaeJ\x16\n\x0breceiver_id\x12\x071552437J;\n\x13s:client_message_id\x12$2c7afb9f-5c8e-46cb-a1f1-11c3eda52862J\x0b\n\x04from\x12\x03apiJ\x0e\n\ttag_valid\x12\x011J \n\x0fsrc_create_time\x12\r1602228487997J\x0c\n\x04type\x12\x04textJ.\n\x13src_conversation_id\x12\x170:1:1552437:92868149435J\x10\n\x0bdisplayType\x12\x010J\x0b\n\x06s:mode\x12\x010J\x1e\n\x07talk_id\x12\x136881517845138751758J\x1a\n\x0bsrc_user_id\x12\x0b92868149435J\t\n\x03src\x12\x02dyJ\n\n\x05srcId\x12\x012J-\n\x19origin_service_message_id\x12\x101680058339036174J\x11\n\ts:biz_aid\x12\x041383J\x0b\n\x06source\x12\x010J\x16\n\x05uname\x12\r\xe5\x91\x86\xe5\x91\x86_\xe6\xa9\x98\xe5\xad\x90P\x91\x8f\x8a\xe2\xd0.X\x00`\x00h\xa8\xe6\xfd\xcc\xa2\xca\x90\x9e\x16r7MS4wLjABAAAACyJ-lMlxgodznImTN6lEfXpb0aXhr1DjWsT5eol7P9I0\xf7\x8a\x92\x97\xfe\xa6\xec\x028\xe3\xc2\x87\x9f\xfe\xa6\xec\x02@\x89\xe4\x86\x9f\xfe\xa6\xec\x02:!202010091528080101940260820279114H\xaa\x8f\x8a\xe2\xd0., binary message: \x08\x93N\x10\xd9\x93\x8a\xe2\xd0.\x18\x91N \x01:\x02pbB\xd2\x05\x08\xe0\x04\x10\x93N"6Jk3WGIWcKjZvnzQXWaXZ1LVJZWdxRA8C2X4THvDJglkPAcmCyJjYSw(\x030\x01B1\x82&.\n 1:1:92868149435:3271763264289960\x10\x87\x82\x80\xc6\xae\xbf\xd4\xb8_\x18\x01J\x010z\x9d\x01\n\nuser_agent\x12\x8e\x01Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) feige/0.5.6 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36z\x16\n\x0ecookie_enabled\x12\x04truez\x19\n\x10browser_language\x12\x05zh-CNz\x19\n\x10browser_platform\x12\x05Win32z\x17\n\x0cbrowser_name\x12\x07Mozillaz\x9a\x01\n\x0fbrowser_version\x12\x86\x015.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) feige/0.5.6 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36z\x16\n\x0ebrowser_online\x12\x04truez\x14\n\x0cscreen_width\x12\x041920z\x15\n\rscreen_height\x12\x041080z\x0b\n\x07referer\x12\x00z\x1e\n\rtimezone_name\x12\rAsia/Shanghaiz\x13\n\x0bsession_aid\x12\x041383z\x13\n\x08app_name\x12\x07ecom.imz\x15\n\x0fpriority_region\x12\x02CN\x90\x01\x02, binary message: \x08\xc6\x88\xa5\xc7\x01\x10\xb3\xe4\xa5\xf5\xa2\xca\x90\x9e\x16\x18\x91N \x012\x00:\x02pbB\x88\x04\x08\xe0\x04\x10\x93N\x18\x00"\x02OK(\x012\xb2\x03\x82&\xae\x03\n\xab\x03\n 1:1:92868149435:3271763264289960\x10\x87\x82\x80\xc6\xae\xbf\xd4\xb8_\x18\x01"\xa2\x011YcuJUNSe0uTpPBeUDjeZ1iNsgUW6WKCC9hMe9K36wttGXh70afRG8Euv6GOhZFNBGg9Guvs1EbVMoo283ntbHZJpxkeDZJgxIH4xVxt39bL46uN6imgEohq3wTHnhygDl2HZd2QTEdi473qVSZOLOnyH80bOmmBGM2\x14\n\x07\x08\xbb\x81\xfe\xfa\xd9\x02\n\t\x08\xa8\xf9\xa0\xf9\xeb\xf4\xe7\x058\x02@\x01\x92\x03t\x10\x87\x82\x80\xc6\xae\xbf\xd4\xb8_\x18\x01 \xfa\xa3\xc5\xfb\x05*\x002\x00:\x00@\x01J\x00Z\x0f\n\x07s:s_aid\x12\x041383`\xbb\x81\xfe\xfa\xd9\x02j7MS4wLjABAAAACyJ-lMlxgodznImTN6lEfXpb0aXhr1DjWsT5eol7P9Ip\x00x\x00\x80\x01\x00\x9a\x03D\n 1:1:92868149435:3271763264289960\x10\x87\x82\x80\xc6\xae\xbf\xd4\xb8_\x18\x01 \x00(\x000\x008\x00@\x01P\xfa\xa3\xc5\xfb\x05X\x00`\x00h\x00:502160222848816600000000000000000000ffff0ac63e6463322eP\xe7\x8f\x8a\xe2\xd0.X\xee\x8f\x8a\xe2\xd0., binary message: \x08\x80\x94\xeb\xdc\x03\x10\xc6\x96\x8a\xe2\xd0.\x18\x01 \xcc\x08:\x04jsonB\x06"ping", binary message: \x08\xe6\x89\xa5\xc7\x01\x10\xeb\xe7\xb8\x9f\xa4\xca\x90\x9e\x16\x18\x01 \xcc\x082\x00:\x00B\x00, binary message: \x08\x81\x94\xeb\xdc\x03\x10\xdd\xa7\x8a\xe2\xd0.\x18\x01 \xf2\x07:\x04jsonBN{"conversation_id":"1:1:92868149435:3271763264289960","user_id":"92868149435"}, binary message: \x08\x82\x94\xeb\xdc\x03\x10\xde\xa7\x8a\xe2\xd0.\x18\x01 \xe8\x07:\x04jsonBc{"conversation_id":"0:1:1552437:92868149435","user_id":"92868149435","create_time":"1602228488081"}, binary message: \x08\xe2\x92\xa5\xc7\x01\x10\xa8\xcb\xf0\xb8\xac\xca\x90\x9e\x16\x18\x01 \xf2\x072\x04json:\x00Bl{"conversation_id":"1:1:92868149435:3271763264289960","user_id":"92868149435","create_time":"1602228256001"}]
#
# m = binary message: \x08\xe2\x92\xa5\xc7\x01\x10\xa8\xcb\xf0\xb8\xac\xca\x90\x9e\x16\x18\x01 \xf2\x072\x04json:\x00Bl{"conversation_id":"1:1:92868149435:3271763264289960","user_id":"92868149435","create_time":"1602228256001"}

#
# dic = {}
# dic['name'] = 'xiaoming'
# dic['age'] = '18'
# dic['sex'] = 'nan'
#
# print(dic)
#
#
# Ka=QM5NHaZ6XWSNPY3HF4E5=6HN2RWdfuxLVzzBVHRRt1qo6DF==Cy1uVt1GgvPUDZYOYIZuBtfy9GUIsx2w2gz4yYxGccZcuVtPWv3GuBtR9KxXwUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u@ZPuBt0x7wmo1koDFS=22I=L=OCimNNz1yt@@YwD
# Ka=QM5NHaZ6XWSNPY3HF4E5=6HN2RWdfuxLVzzBVHxRtxjhNwzWWvy1uVt1GgvPUDZYOYIZuztFexLwWvGccZcuVtPWv3GuBtR9KxXwUvhgMZSguxzBEHLNRTVtlEeLZNz1@Db17dDFC8zv7u@ZPuztgw6vlnDjnCER@GGH@K@NBimNNz1yt@@YwD
#


url = 'https://maoyan.com/board/4'
headers = headers_raw_to_dict(
    b'''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: __mta=212253995.1602231311261.1602311722800.1602312711605.7; uuid_n_v=v1; uuid=8C7A0D700A0711EBA834BBA9FFFEB016710C09FBA81E4B26B404A43DC7392651; _lxsdk_cuid=1750c6d9b85c8-0c76e12d6fb3b5-3f6b4e04-1fa400-1750c6d9b85c8; _lxsdk=8C7A0D700A0711EBA834BBA9FFFEB016710C09FBA81E4B26B404A43DC7392651; _csrf=cfaa16c87e9585a4ad1c2a905d1172957988bb91f42e2f9d98c99c776e1f1342; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1602231311,1602311723; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1602312712; _lxsdk_s=175113896cc-744-a22-48c%7C%7C6
    Host: maoyan.com
    Sec-Fetch-Dest: document
    Sec-Fetch-Mode: navigate
    Sec-Fetch-Site: cross-site
    Sec-Fetch-User: ?1
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36
    
    '''
)


r = requests.get(url = url, headers = headers)

print(r.text)

html = etree.HTML(r.text)
# a = html.xpath('//*[@id="app"]/div/div/div[1]/dl[.class="board-wrapper"]')
# print(a)
# for n in a:
#     print(n)

# result_name = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a')
# result_actor = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[2]')
'''
result = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]')
for d in result:
    # print(d)
    # name = d.xpath('div/div/div[1]/p[1]/a/text()')
    # actor = d.xpath('div/div/div[1]/p[2]/a/text()')
    name = d.xpath('p[1]/a/text()')
    actor = d.xpath('p[2]/text()')
    print(name, actor)
'''

result = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')

for res in result:
    # print(res)
    # name = res.xpath('div/div/div[1]/p[1]/a/text()')[0].strip()
    # actor = res.xpath('div/div/div[1]/p[2]/text()')[0].strip()
    # print(name, actor)
    # with open('movie.txt', 'a+') as f:
    #     f.write(name + '  ' + actor + '\n')

    '''图片'''
    pic = res.xpath('a/img[2]/@data-src')[0][:-16]
    print(pic)

    response = requests.get(url = pic).content

    n = result.index(res)

    path = '图片\\{}.jpg'.format(n)
    with open(path, 'wb') as f:
        f.write(response)






















