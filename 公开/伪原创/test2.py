import re, requests, time, json, os
from copyheaders import headers_raw_to_dict
from fake_useragent import UserAgent

key = 'What do you want to say by associating with it when it comes to Amazon? For the best selection on a variety of cool items and gifts this Christmas, right? In fact, Amazon has to be voted by a sufficient number of Retail\'s Customer Satisfaction Awards. From personal care to electronics, games and fashion items, full categories of each product are available on Amazon.'
print('原文:',key)
# url = 'http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=auto&tl=zh_TW&q={}'.format(key)
url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}'.format(key)#有道
res = requests.get(url).json()

# print('原文:',res['translateResult'][0][0]['src'])
fanyi = res['translateResult'][0]
# print('翻译:',res['translateResult'][0][0]['tgt'])
s = []
for i in fanyi:
    s.append(i['tgt'])
list=' '.join(s)
print('翻译:',list)


def run():
    url_w = 'http://www.seowyc.com/seo/api/wyc.html'
    data = {
        'content': list,
        'ratio': 50
    }
    res = requests.post(url=url_w, data=data).text
    res = json.loads(res)
    key_2 = res['content']
    print('原创:', res['content'])
    url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={}'.format(key_2)
    r = requests.get(url).json()
    # print('翻译结果为:',r['translateResult'][0][0]['tgt'])
    s = []
    for i in r['translateResult'][0]:
        s.append(i['tgt'])
    l = ''.join(s)
    print('翻译:',l)


if __name__ == '__main__':
    run()








