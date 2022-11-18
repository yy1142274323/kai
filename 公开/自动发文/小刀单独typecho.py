import requests,re,time
from lxml import etree









def fun(title,s):
    #
    from pytypecho import Typecho,Attachment,Post
    # print(title,s)



    pageContent = {
        }
    pageContent["title"] = title
    pageContent["content"] = s

    wp = Typecho("http://iiiqs.com/index.php/action/xmlrpc", "admin", "admin")
    post = Post(title=pageContent["title"],description=pageContent["content"])
    post.title = pageContent["title"]
    post.content = pageContent["content"]

    # post.categories = ['QQ微信']  # 分类

    # post.categories = ['游戏相关']  #分类

    # post.categories = ['办公学习']  # 分类

    # post.categories = ['盒子应用']  # 分类

    # post.categories = ['上传下载']  # 分类

    # post.categories = ['其他软件']  # 分类

    # post.categories = ['安卓软件']  # 分类

    post.categories = ['系统相关']  # 分类

    # post.categories = ['娱乐休闲']  # 分类


    # post.terms_names = {
    #     'category': ['游戏相关']  # 文章所属分类，没有则自动创建
    # }
    #print(post)
    wp.new_post(post,publish=True)







# url1 = 'https://www.x6d.com/html/24-{}.html'.format(1)#QQ微信    4
# url2 = 'https://www.x6d.com/html/96-{}.html'.format(1)#游戏相关  47
# url3 = 'https://www.x6d.com/html/26-{}.html'.format(1)#办公学习    16
# url4 = 'https://www.x6d.com/html/102-{}.html'.format(1)#盒子应用   2
# url5 = 'https://www.x6d.com/html/97-{}.html'.format(1)#上传下载    6
# url6 = 'https://www.x6d.com/html/49-{}.html'.format(1)#其他软件    6
# url7 = 'https://www.x6d.com/html/47-{}.html'.format(1)#安卓软件    26
# url8 = 'https://www.x6d.com/html/28-{}.html'.format(1)#系统相关    7
# url9 = 'https://www.x6d.com/html/29-{}.html'.format(1)#娱乐休闲    10


ssss = 9
while ssss > 0:
    print('第',ssss,'頁')
    res = requests.get('https://www.x6d.com/html/24-{}.html'.format(ssss)).text#QQ微信    4
    # res = requests.get('https://www.x6d.com/html/96-{}.html'.format(ssss)).text#游戏相关  55
    # res = requests.get('https://www.x6d.com/html/26-{}.html'.format(ssss)).text#办公学习  20
    # res = requests.get('https://www.x6d.com/html/102-{}.html'.format(ssss)).text#盒子应用   3
    # res = requests.get('https://www.x6d.com/html/97-{}.html'.format(ssss)).text#上传下载    6
    # res = requests.get('https://www.x6d.com/html/49-{}.html'.format(ssss)).text#其他软件    6
    # res = requests.get('https://www.x6d.com/html/47-{}.html'.format(ssss)).text#安卓软件    34
    res = requests.get('https://www.x6d.com/html/28-{}.html'.format(ssss)).text#系统相关    9
    # res = requests.get('https://www.x6d.com/html/29-{}.html'.format(ssss)).text#娱乐休闲    13

    selector=etree.HTML(res)
    content=selector.xpath('//ul/li/div/a/@href') #这里使用starts-with方法提取div的id标签属性值开头为a的div标签
    # print(content)
    for each in content[::-1]:
        print('https://www.x6d.com'+each)
        r = requests.get('https://www.x6d.com'+each).text
        # print(r)

        pattern2 = '<div class="left">(.*)<div class="mzsm">'
        con2 = re.search(pattern2, r, re.S).group(1)
        # print(con2)
        panx=etree.HTML(con2)
        # 发表时间
        t =panx.xpath('//div/time/text()')[0][:-6]
        # print(t)

        title=panx.xpath('//h1/text()')[0]
        panm = panx.xpath('//div/a/@title')
        panl=panx.xpath('//div/a/@data-url')
        title = str(title)
        # fun(title)
        print(title)
        # print(panm)




        if len(panl)== 1 :
            pattern1 = '<div class="article-content">(.*)<div class="article-down">'
            con1 = re.search(pattern1, r, re.S).group(1)

            pattern ='src="/uploads(.*)/allimg'
            con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
            # print(con1)
            a = '<a href="{}">{}</a>'.format(panl[0], panm[0])
            s = con1 + '\n' + '-------------------------------------------' + '\n' + a
            # print(type(s))
            fun(title, s)

        elif len(panl)== 2 :
            pattern1 = '<div class="article-content">(.*)<div class="article-down">'
            con1 = re.search(pattern1, r, re.S).group(1)
            pattern ='src="/uploads(.*)/allimg'
            con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
            a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])
            s=con1 + '\n' + '-------------------------------------------' + '\n' +a
            # print(type(s))
            fun(title,s)
        elif len(panl)==3:
            pattern1 = '<div class="article-content">(.*)<div class="article-down">'
            con1 = re.search(pattern1, r, re.S).group(1)
            pattern ='src="/uploads(.*)/allimg'
            con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
            a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])+'\t'+ '<a href="{}">{}</a>'.format(panl[2],panm[2])
            s=con1 + '\n' + '-------------------------------------------' + '\n' +a
            # print(s)
            fun(title,s)
        elif len(panl)==4:
            pattern1 = '<div class="article-content">(.*)<div class="article-down">'
            con1 = re.search(pattern1, r, re.S).group(1)
            pattern ='src="/uploads(.*)/allimg'
            con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
            a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])+'\t'+ '<a href="{}">{}</a>'.format(panl[2],panm[2])+'\t'+ '<a href="{}">{}</a>'.format(panl[3],panm[3])
            s = con1 + '\n' + '-------------------------------------------' + '\n' + a
            # print(s)
            fun(title,s)
        elif len(panl)==5:
            pattern1 = '<div class="article-content">(.*)<div class="article-down">'
            con1 = re.search(pattern1, r, re.S).group(1)
            pattern ='src="/uploads(.*)/allimg'
            con1 = re.sub(pattern, 'src="https://www.x6d.com/uploads/allimg', con1, count=0, flags=0)
            a = '<a href="{}">{}</a>'.format(panl[0],panm[0])+'\t'+ '<a href="{}">{}</a>'.format(panl[1],panm[1])+'\t'+ '<a href="{}">{}</a>'.format(panl[2],panm[2])+'\t'+ '<a href="{}">{}</a>'.format(panl[3],panm[3])+'\t'+ '<a href="{}">{}</a>'.format(panl[4],panm[4])
            s = con1 + '\n' + '-------------------------------------------' + '\n' + a
            # print(s)
            fun(title,s)

    ssss -= 1


else:
    print('结束')








































