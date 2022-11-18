

import requests

url = 'https://www.baidu.com/'
response=requests.get(url=url)
response.encoding = 'utf-8'
i = response.content
print(i)

with open('baidu.html','wb') as f:
    f.write(i)


























































































































































# lis = ['a','b','c',{'m':'n', 'x':'y'},'d','e']

# i = lis[3]
# print(i)
# i['m'] = 'z'
# i['x'] = 'z'
# i['i'] = 'o'
# print(i)
# lis[3] = i

'''

print(lis)

lis[3]['m'] = 'z'
lis[3]['n'] = 'z'
lis[3]['i'] = 'o'
print(lis)

'''
'''
['a','b','c',{'m':'z', 'x':'z', 'i':'o'},'d','e']
'''
















