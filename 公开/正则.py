# -*- coding = utf-8 -*-
# @Time : 2020/10/19 10:49
# @Author : 阿斌
# @File : 正则.py
# @Software : PyCharm


import re




# match·························································

'''
pattern = 'xiaowang'
lin = 'xiaowang'

res = re.match(pattern,lin)
print(res)
print(res.group(0))             #取出匹配数据
'''


'''
# search························································
#  任意位置开始配
pattern = 'xiaowang'
lin = 'sssssxiaowangkkkkkkkk'

res = re.search(pattern,lin)
print(res)

'''



'''

line = 'hkkk\nlll'
pattern = '^h.*'             #匹配     ^ 以h开头的字符串 . 匹配任意字符除了换行符 * 前一个字符匹配0次到多次·························
res = re.match(pattern,line,re.S)
print(res)
'''


'''
#以 h 开头后边跟着一个字符···············································
line = 'huang123'
pattern = '^h.'

res = re.match(pattern,line)
print(res)
'''



'''
#以h开头后边跟着任意数量的数字···········································
line = 'h321uang123'
pattern = '^h\d{0,2}'                      # []  内部的字符选一个进行匹配   \d 代表[0-9]    +前一个字符匹配1次到多次   ?前一个字符匹配0次到1次 !!!!
res = re.match(pattern,line)            #{}   匹配多少多少次{*,*}
print(res)
print(res.group(0))

'''

'''
line = 'liujianq123'
pattern = '.*3$'
res = re.search(pattern,line)
print(res.group())

'''


'''

#```````````````````````````````````````````````````````````````````````````````Z转义字符！！！······
line = 'www.bai\ndu.com'
pattern = '.*'
res = re.search(pattern,line,re.S)
print(res.group())

'''


'''
#···················································！！！！取出其中什么到什么
line = 'qhuuhhaaahang123'
pattern = '.*?(h.*?h).*'
res = re.search(pattern,line,re.S)
print(res.group(1))                             #没括号写0   选第几个写几

'''




'''
line = 'apple'
# pattern = '^[c0-9]'
pattern = '^(a|b|c).*'              #         [ab]     !!     |   代表或！！！！````````````````````````````````
res = re.match(pattern,line)
print(res.group(0))

'''

'''
line = 'cbpple123b123'
pattern = '(^[^a|b|c].*)'                                  # [^xx]   不匹配 尖号后的内容
res = re.search(pattern,line)
print(res)

'''


'''
line = 'asd\ncom'
# pattern = '.*\\n.*'     #可以
pattern = '.*\n.*'
res = re.search(pattern,line)
print(res)
'''







'''

# ``````````````````````````````````````````````````````````````findall  和 findinter```````````````````````````````````````````
line = 'Send the dragonfly to see love to eat it quickly.'
pattern = '\w+ly'
# re.findall(r'\w+ly')
# res = re.search(pattern,line)
# print(res)
# res = re.findall(pattern,line)
# print(res)
res = re.finditer(pattern,line)
for i in res:
    print(i.group(0))

'''



'''
#sub 替换···············································································································

line = 'Send the dragonfly to see love to eat it quickly.'

pattern = '\w+ly'
res = re.sub(pattern,'shuai',line)
print(res)

'''



'''

#·································································次调用  的  【模式】(pattern)·····································
line = 'Send the dragonfly to see love to eat it quickly.'
pattern = '\w+ly'
pat = re.compile(pattern)                      #pat 调用pattern
res = pat.search(line)                         #等同于 res = re.search(pattern,line)
print(res)

'''







































'''
# ```````````````````````````````````````````````````````````````````````````````````````````````++++++++``````````````
class Cats():

    def __init__(self):
        self.age = 2
if __name__ == '__main__':
    a = Cats()
    b = a.age
    print(b)

'''




































































