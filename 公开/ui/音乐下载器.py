

# 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# 导入模块
from tkinter import *
import requests
import jsonpath
import os
from urllib.request import urlretrieve

# 2.功能实现
"""
    1.url
    2.模拟浏览器请求
    3.解析网页源代码
    4.保存数据
"""
def song_download(url,title,author):
    # 创建文件夹
    os.makedirs("music",exist_ok=True)
    path = 'music\{}.mp3'.format(title)
    text.insert(END,'歌曲:{0}-{1},正在下载...'.format(title,author))
    # 文本框滑动
    text.see(END)
    # 更新
    text.update()
    # 下载
    urlretrieve(url,path)
    text.insert(END,'下载完毕,{0}-{1},请试听'.format(title,author))
    # 文本框滑动
    text.see(END)
    # 更新
    text.update()

def get_music_name():
    """
    搜索歌曲名称
    :return:
    """
    name = entry.get()
    platfrom = var.get()
    # name = '白月光与朱砂痣'
    url = 'https://music.liuzhijin.cn/'
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        # 判断请求是异步还是同步
        "x-requested-with":"XMLHttpRequest",
    }
    param = {
        "input":name,
        "filter":"name",
        "type":platfrom,
        "page": 1,
    }
    res = requests.post(url=url,data=param,headers=headers)
    json_text = res.json()

    title = jsonpath.jsonpath(json_text,'$..title')
    author = jsonpath.jsonpath(json_text,'$..author')
    url = jsonpath.jsonpath(json_text, '$..url')
    print(title,author,url)
    song_download(url[0],title[0],author[0])


# 1.用户界面
# 创建画板
root = Tk()
# 设置窗口标题
root.title('全网音乐下载器')
# 设置窗口大小以及出现的位置
root.geometry('560x450+400+200')
# 标签组件
label = Label(root,text="请输入下载的歌曲:",font=('楷体',20))
# 定位与布局
label.grid(row=0)
# 输入框组件
entry = Entry(root,font=('宋体',20))
entry.grid(row=0,column=1)
# 单选按钮
var = StringVar()
r1 = Radiobutton(root,text='网易云',variable=var,value='netease')
r1.grid(row=1,column=0)
r2 = Radiobutton(root,text='QQ',variable=var,value='qq')
r2.grid(row=1,column=1)
# 列表框
text = Listbox(root,font=('楷体',16),width=50,height=15)
text.grid(row=2,columnspan=2)
# 下载按钮
button1 = Button(root,text='开始下载',font=('楷体',15),command=get_music_name)
button1.grid(row=3,column=0)
button2 = Button(root,text='退出程序',font=('楷体',15),command=root.quit)
button2.grid(row=3,column=1)
# 显示界面
root.mainloop()

# 如何将.py代码打包成.exe文件



# 22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
"""
网易云歌单歌曲迅速批量下载（图形界面）
https://www.52pojie.cn/forum.php?mod=viewthread&tid=1314335&extra=page%3D1%26filter%3Dtypeid%26typeid%3D29
"""

# import os
# import requests
# from bs4 import BeautifulSoup
# from tkinter import *
#
# def music_download():
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#     }
#     if not os.path.exists('./网易云歌单/'):
#         os.mkdir('./网易云歌单/')
#     play_url = entry1.get()
#     s = requests.session()
#     response = s.get(play_url,headers=headers).content
#     soup =BeautifulSoup(response,'lxml')
#     music_data = soup.find('ul',class_='f-hide')
#     lists = []
#     for music in music_data.find_all('a'):
#         #print('{}:{}'.format(music.text,music['href']))
#         list = []
#         music_url = 'http://music.163.com/song/media/outer/url'+ music['href'][5:] + '.mp3'
#         print(music_url)
#         music_name = music.text
#         list.append(music_name)
#         list.append(music_url)
#         lists.append(list)
#     #print(lists)
#     os.chdir('.\网易云歌单')
#     b = os.getcwd()
#     print('当前目录变为为：', b)
#     for i in lists:
#         url = i[1]
#         name = i[0]
#         try:
#             print("正在下载",name)
#             text.insert(END, '歌曲:{},正在下载。。。'.format(name))
#             text.see(END)
#             header1 ={"User-Agent":
#                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
#
#             }
#             #urllib.request.urlretrieve(url,'./网易云歌单/%s.mp3' % name)
#             res = requests.get(url,headers=header1)
#
#             with open(str(name)+'.mp3',"ab")as f:
#                 f.write(res.content)
#             print('下载成功。。。')
#             text.insert(END, '下载完毕:{},可以去听听'.format(name))
#             text.see(END)
#             text.update()
#
#         except:
#             pass
#
# root = Tk()
# root.geometry('590x480+400+260')
# root.title('网易云歌单下载器')
# labell1 = Label(root,text = '请输入歌单的网页链接，记得去除#号哦',font=('微软雅黑',15))
# labell1.grid()
# entry1 = Entry(root,font=('微软雅黑',12))
# entry1.grid(row=2,column=0)
#
# text = Listbox(root, font=('微软雅黑', 16), width=40, height=10)
# text.grid(row=3, columnspan=1)
#
# b1 = Button(root, text='开始下载', font=('微软雅黑', 15),command=music_download)
# b1.grid(row=4, column=0)
# b2 = Button(root, text='退出程序', font=('微软雅黑', 15), command=root.quit)
# b2.grid(row=4, column=1)
#
# root.mainloop()
#
#

























