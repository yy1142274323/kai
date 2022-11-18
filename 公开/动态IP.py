
import requests
from fake_useragent import UserAgent

# print(ip)



url = 'http://httpbin.org/get'
headers = {'User-Agent': UserAgent().random}

# url_ip = 'http://120.79.85.144/freeip/ips?packid=1000&unkey=&freekey=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.IjE4NTQwMzU4MTQ3fFN1RGFpTGki.feKFPXo8XL8c77N0NVFq_U7esTY1SB__pxSZRLGoEBM&tid=&linePoolIndex=&qty=1&time=5&port=1&format=txt&ss=3&css=&pro=&city=&dt=1&usertype=18'
# ip = requests.get(url_ip).text

# 参数类型
# proxies
# proxies = {'协议': '协议://IP:端口号'}

fopen = open('qqq.txt', 'r')
lines = fopen.readlines()
for line in lines:
    line = line.strip('\n')  # 去掉换行符
    print(line)


    proxies = {
                # 'http': 'http://{}'.format('118.212.105.200:9999'),
                'https': 'https://{}'.format(line)
            }

    html = requests.get(url=url,headers=headers,proxies=proxies, timeout=3).text
    # print(ip)
    print(html)



# 'http://a.ipjldl.com/getapi?packid=1&unkey=&freekey=&tid=&linePoolIndex=&qty=1&time=1&port=1&format=txt&ss=3&css=&pro=&city=&dt=1&usertype=18'


