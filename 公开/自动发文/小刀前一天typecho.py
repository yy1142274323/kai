import requests,re,time
from lxml import etree




#
# proxies = {'http': "socks5://127.0.0.1:8080",
#            'https': "socks5://127.0.0.1:8080"}
# print(requests.get(url, proxies=proxies).content)



# 获得当前时间时间戳
now = int(time.time())
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
print(otherStyleTime)


url1 = 'https://www.x6d.com/html/24-{}.html'.format(1)#QQ微信    4
url2 = 'https://www.x6d.com/html/96-{}.html'.format(1)#游戏相关  39
url3 = 'https://www.x6d.com/html/26-{}.html'.format(1)#办公学习    16
url4 = 'https://www.x6d.com/html/102-{}.html'.format(1)#盒子应用   2
url5 = 'https://www.x6d.com/html/97-{}.html'.format(1)#上传下载    6
url6 = 'https://www.x6d.com/html/49-{}.html'.format(1)#其他软件    6
url7 = 'https://www.x6d.com/html/47-{}.html'.format(1)#安卓软件    26
url8 = 'https://www.x6d.com/html/28-{}.html'.format(1)#系统相关    7
url9 = 'https://www.x6d.com/html/29-{}.html'.format(1)#娱乐休闲    10





def fun(title,s,url):
    #
    from pytypecho import Typecho,Attachment,Post
    # print(title,s)



    pageContent = {
        }
    pageContent["title"] = title
    pageContent["content"] = s

    wp = Typecho("http://677688521.xyz/index.php/action/xmlrpc", "yy677", "677688")
    post = Post(title=pageContent["title"],description=pageContent["content"])
    post.title = pageContent["title"]
    post.content = pageContent["content"]
    if url == url1:
        post.categories = ['QQ微信']  # 分类
    elif url == url2:
        post.categories = ['游戏相关']  #分类
    elif url == url3:
        post.categories = ['办公学习']  # 分类
    elif url == url4:
        post.categories = ['盒子应用']  # 分类
    elif url == url5:
        post.categories = ['上传下载']  # 分类
    elif url == url6:
        post.categories = ['其他软件']  # 分类
    elif url == url7:
        post.categories = ['安卓软件']  # 分类
    elif url == url8:
        post.categories = ['系统相关']  # 分类
    elif url == url9:
        post.categories = ['娱乐休闲']  # 分类
    else:
        pass

    # post.terms_names = {
    #     'category': ['游戏相关']  # 文章所属分类，没有则自动创建
    # }
    #print(post)
    wp.new_post(post,publish=True)





#QQ微信24-4游戏相关96-39办公学习26-16盒子应用102-2上传下载97-6 其他软件49-6安卓软件47-26系统相关28-7娱乐休闲29-10
# url = 'https://www.x6d.com/html/24-{}.html'.format(q)#QQ微信    4
# url = 'https://www.x6d.com/html/96-{}.html'.format(q)#游戏相关  39
# url = 'https://www.x6d.com/html/26-{}.html'.format(q)#办公学习    16
# url = 'https://www.x6d.com/html/102-{}.html'.format(q)#盒子应用   2
# url = 'https://www.x6d.com/html/97-{}.html'.format(q)#上传下载    6
# url = 'https://www.x6d.com/html/49-{}.html'.format(q)#其他软件    6
# url = 'https://www.x6d.com/html/47-{}.html'.format(q)#安卓软件    26
# url = 'https://www.x6d.com/html/28-{}.html'.format(q)#系统相关    7
# url = 'https://www.x6d.com/html/29-{}.html'.format(q)#娱乐休闲    10
# print(url)



eee= [url1,url2,url3,url4,url5,url6,url7,url8,url9]
for url in eee:


    res = requests.get(url).text

    selector=etree.HTML(res)
    content=selector.xpath('//ul/li/div/a/@href') #这里使用starts-with方法提取div的id标签属性值开头为a的div标签
    print(content)
    for each in content[::-1]:
        print('https://www.x6d.com'+each)
        r = requests.get('https://www.x6d.com'+each).text
        # print(r)

        pattern2 = '<div class="left">(.*)<div class="mzsm">'
        con2 = re.search(pattern2, r, re.S).group(1)
        # print(con2)
        panx=etree.HTML(con2)
        t =panx.xpath('//div/time/text()')[0][:-6]
        print(t)
        title=panx.xpath('//h1/text()')[0]
        panm = panx.xpath('//div/a/@title')
        panl=panx.xpath('//div/a/@data-url')
        title = str(title)
        # fun(title)
        # print(title)
        # print(panm)


        # if t == otherStyleTime:
        if t== '2021-10-10':
            print(1111111111111111111111)

            if len(panl)== 1 :
                pattern1 = '<div class="article-content">(.*)<div class="article-down">'
                con1 = re.search(pattern1, r, re.S).group(1)

                pattern ='src="/uploads(.*)/allimg'
                con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
                # print(con1)
                a = '<a href="{}">{}</a>'.format(panl[0], panm[0])
                s = con1 + '\n' + '-------------------------------------------' + '\n' + a
                # print(type(s))
                fun(title, s,url)

            elif len(panl)== 2 :
                pattern1 = '<div class="article-content">(.*)<div class="article-down">'
                con1 = re.search(pattern1, r, re.S).group(1)
                pattern ='src="/uploads(.*)/allimg'
                con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
                a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])
                s=con1 + '\n' + '-------------------------------------------' + '\n' +a
                # print(type(s))
                fun(title,s,url)
            elif len(panl)==3:
                pattern1 = '<div class="article-content">(.*)<div class="article-down">'
                con1 = re.search(pattern1, r, re.S).group(1)
                pattern ='src="/uploads(.*)/allimg'
                con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
                a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])+'\t'+ '<a href="{}">{}</a>'.format(panl[2],panm[2])
                s=con1 + '\n' + '-------------------------------------------' + '\n' +a
                # print(s)
                fun(title,s,url)
            elif len(panl)==4:
                pattern1 = '<div class="article-content">(.*)<div class="article-down">'
                con1 = re.search(pattern1, r, re.S).group(1)
                pattern ='src="/uploads(.*)/allimg'
                con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
                a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])+'\t'+ '<a href="{}">{}</a>'.format(panl[2],panm[2])+'\t'+ '<a href="{}">{}</a>'.format(panl[3],panm[3])
                s = con1 + '\n' + '-------------------------------------------' + '\n' + a
                # print(s)
                fun(title,s,url)
            elif len(panl)==5:
                pattern1 = '<div class="article-content">(.*)<div class="article-down">'
                con1 = re.search(pattern1, r, re.S).group(1)
                pattern ='src="/uploads(.*)/allimg'
                con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
                a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])+'\t'+ '<a href="{}">{}</a>'.format(panl[2],panm[2])+'\t'+ '<a href="{}">{}</a>'.format(panl[3],panm[3])+'\t'+ '<a href="{}">{}</a>'.format(panl[4],panm[4])
                s = con1 + '\n' + '-------------------------------------------' + '\n' + a
                # print(s)
                fun(title,s,url)









    else:
        pass














































