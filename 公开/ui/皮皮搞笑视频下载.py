# import math
import requests,json,copyheaders,time,re,os
from copyheaders import headers_raw_to_dict
from lxml import etree
# from selenium import webdriver
from tkinter import *

# pyside2
def close_window():
    if not os.path.isdir("视频"):
        os.mkdir("../视频")
    entry = e1.get()


    # url = 'https://h5.ippzone.com/pp/post/387420696741?zy_to=copy_link&share_count=1&m=65a735b628fdcf6780a0ad9c440f2aef&app=&type=post&did=f166323b1530394e&mid=83612128&pid=387420696741'
    #
    i = entry
    i = 'http://share.ippzone.com/pp/post/373898257638'

    c = i.rfind('/')  # 符号最后出现  第一次是find  多少位
    id = i[c + 1:]    #开始截取
    url = 'http://api.63code.com/pipigx/api.php?url=http://h5.ippzone.com/pp/post/{}'.format(id)
    print(url)


    res = requests.get(url).text
    res = json.loads(res)
    r = res["url"]
    m = res['content']
    print(r)
    print(res)
    f = requests.get(url = r).content
    with open('视频\\{}.mp4'.format(m), 'wb') as l:
        l.write(f)

close_window()









# 创建Tk对象，Tk代表窗口
root = Tk()
root.geometry('550x100+885+465')
# root.resizable(0, 0)  # 窗口大小固定
# 设置窗口标题
root.title('啥也不是程序')
# 创建Label对象，第一个参数指定该Label放入root
w = Label(root, text="请输入链接地址！！！")
# 调用pack进行布局
w.pack()
# 输入框
e1 = Entry(root, bd=2,width =50 )
e1.pack()
# 创建Button对象，第一个参数指定该Button放入root
okButton = Button(root, text="确定", width=10, height=1, command=close_window)  # command 调用函数
okButton['background'] = 'yellow'
okButton.configure(background='yellow')
okButton.pack()
# 启动主窗口的消息循环
root.mainloop()

