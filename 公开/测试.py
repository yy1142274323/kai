from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo




# wp = Client('http://xb.677688521.xyz/xmlrpc.php', 'yy677', '677688')
# wp.call(GetPosts())
#
# wp.call(GetUserInfo())
#
# post = WordPressPost()
# post.title = '1'
# post.content = '1'
# post.terms_names = {
#     'post_tag': ['test', 'firstpost'],#标签
#     'category': ['Introductions', 'Tests']#分类
#     }
#
# wp.call(NewPost(post))
#
#
#
#
#
# 代理*********************************************
import requests,time,re
from lxml import etree
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().random}

url_dl = 'https://ip.jiangxianli.com/?page=1'
ip_dl = requests.get(url_dl).text
html = etree.HTML(ip_dl)
tp = html.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr/td[11]/button[1]/@data-url')
print(tp)


# 测试出可用IP

#
# '''代理IP地址（高匿）'''
# proxy = {
#   'http': tp[3],
#   # 'https': 'https://117.85.105.170:808'
# }
#
# '''http://icanhazip.com会返回当前的IP地址'''
# p = requests.get('http://icanhazip.com', headers=headers, proxies=proxy)
# print(p.text)
#
#





proxies = {
    # 'https': 'https://127.0.0.1:1080',
    'http': tp[3]
}
# print(proxies)
google_url = 'http://httpbin.org/get'
print('--------------使用requests--------------')
response = requests.get(google_url,headers = headers, proxies=proxies)
print(response.text)








# from wordpress_xmlrpc import Client, WordPressPost
# from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
# from wordpress_xmlrpc.methods.users import GetUserInfo
#
# wp = Client('http://hf.iiiqs.com/xmlrpc.php', 'yy677', '677688')
# wp.call(GetPosts())
# wp.call(GetUserInfo())
# post = WordPressPost()
# post.title = '222'
# post.content = '2222'
#
#
# post.terms_names = {
#     'post_tag': ['test', 'firstpost'],  # 标签
#     'category': ['汉服资讯']  # 分类
# }
#
# wp.call(NewPost(post))

# for xh in range(11)[::-1]:
#     if xh > 0 :
#         print(xh)





'''
学习中遇到问题没人解答？小编创建了一个Python学习交流QQ群：531509025
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
s = '学习中遇到问题没人解答？小编创建了一个Python学习交流QQ群：531509025寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！'
s1 = s.replace('531509025', '')
print(s1)
#输出：abccba




# a = 1.11111
# print(round(a,2))


# from pytypecho import Typecho, Attachment, Post
#
# # print(title, s)
#
# pageContent = {
# }
# pageContent["title"] = 'title'
# pageContent["content"] = s
#
# wp = Typecho("http://www.iiiqs.com/index.php/action/xmlrpc", "yy677", "677688")
# post = Post(title=pageContent["title"], description=pageContent["content"])
# post.title = pageContent["title"]
# post.content = pageContent["content"]
#
# post.categories = ['汉服资讯']  # 分类
#
# post.terms_names = {
#     'category': ['游戏相关']  # 文章所属分类，没有则自动创建
# }
# print(post)
# wp.new_post(post, publish=True)






# from pytypecho import Typecho,Post
# te = Typecho('http://iiiqs.com/index.php/action/xmlrpc', username='yy677', password='677688')
# post = Post(title='title', categories = ['文章分类'],description='content')
# te.new_post(post, publish=True)
# # time.sleep(5)#休息5秒




# import pymysql
#
# conn = pymysql.connect(host='81.70.52.65', user='www', password='www', database='www')
#
# cur = conn.cursor()
#
# cur.execute('SELECT cid FROM typecho_contents where title = %s','关于')
# keywords_list = cur.fetchall()[0][0]
# print(keywords_list)
#
# # 如果是插入、删除、更新语句切记要写提交命令con.commit()
# conn.commit()
# # print (cur.fetchall())
# cur.close()
# conn.close()







