import requests,json,time,re
f = time.time()*1000
t1 = int(f)
print(t1)
t2 = t1-1
print(t2)
url = 'https://upbigsubs-api.uc.cn/api/bigsubs/wm/26c02a37a7b949c7a389fc31cc9c4d10/msgs?uc_param_str=frdnpfvecpntgibiniprdswiutmt&app=ucweb&sub_type=wm&b_version=0.4&errCode=2&errMsg=ucapi.invoke%20not%20exsit%2C%20should%20load%20in%20UCBrowser%20%21&ut=AAQuLl0WSFNXJwCIgccPZnizKN9OiLo2pkPjd5oIoq2jnA%3D%3D&col_cont_src=wm-hp&from=msg&size=10&max_pos='
res=requests.get(url).text
res = json.loads(res)
list = res['data']['list']
# print(list)
for i in list:
    url1 = i['sku']['url']
    # print(url1)
    pattern = 'wm_aid=(.*)!!wm_id'
    id = re.search(pattern, url1, re.S)
    # print(id.group(1))
    url3 = 'https://ff.dayu.com/contents/origin/{}?biz_id=1002&_fetch_author=1&_incr_fields=click1,click2,click3,click_total,play,like'.format(id.group(1))
    # print(url3)
    r = requests.get(url3).text
    r = json.loads(r)
    print(r['data']['body'])
    # print(r['data']['title'])
    # print(r['data']['body']['text'])

    # pic = r['data']['body']['inner_imgs']
    # for n in pic:
    #     print(n['url'])
    print('---------------------------------')
    # break





