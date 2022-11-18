import requests,re

im = input('请输入解析链接：')

url = 'https://tenapi.cn/video/?url={}'.format(im)




res = requests.get(url).json()
print(res)