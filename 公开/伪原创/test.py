import re, requests, time, json, os
from copyheaders import headers_raw_to_dict
from fake_useragent import UserAgent

import requests, json
from copyheaders import headers_raw_to_dict
from lxml import etree
# requests = requests.sessions
import time, random, hashlib


#http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=
key = 'She saw scars and bruises on her body.Tears fell on the wounds.This wasn’t the 1st time he abused and hit her.She decided to end life.Took a knife and went to the bedroom.She came outside with blood all over her face,But this is the 1st time it wasn’t her blood.'
print(key)

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

head = headers_raw_to_dict(
    b''' 
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: no-cache
    Connection: keep-alive
    Content-Length: 252
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    Cookie: OUTFOX_SEARCH_USER_ID=-1520472027@10.108.160.19; JSESSIONID=aaayEi3Shy2_rhX-UkWux; OUTFOX_SEARCH_USER_ID_NCOO=1465447778.2633374; ___rl__test__cookies=1602831265443
    Host: fanyi.youdao.com
    Origin: http://fanyi.youdao.com
    Pragma: no-cache
    Referer: http://fanyi.youdao.com/
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36




    '''
)

# key =input('请输入要翻译的内容：')
def youdao(key):
    sot = str(int(time.time() * 1000) + random.randint(0, 10))
    sig = "fanyideskweb" + key + sot + "]BjuETDhU)zqSxf-=B#7m"

    m = hashlib.md5()

    m.update(sig.encode('utf-8'))

    sig = m.hexdigest()

    form = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': sot,
        'sign': sig,
        'lts': '1602831265459',
        'bv': '4abf2733c66fbf953861095a23a839a8',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'

    }

    # ···················loads 字典 dumps 字符串·····················
    response = requests.post(url=url, headers=head, data=form, timeout=10)
    j = json.loads(response.text)
    fanyi = j['translateResult'][0][0]['tgt']
    print('翻译结果为：', fanyi)
    return fanyi

f = youdao(key)
def resq(f):
    url = 'http://www.seowyc.com/seo/api/wyc.html'
    data = {
        'content':f,
        'ratio':30
    }
    res = requests.post(url = url,data = data).text
    res = json.loads(res)
    key_2 = res['content']
    print('原创结果为：',res['content'])
    eng(key_2)
def eng(key_2):
    youdao(key_2)

if __name__ == '__main__':
    resq(f)












