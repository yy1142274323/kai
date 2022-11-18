from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk
import tkinter,threading,requests

import lxml
from lxml import etree


# 微信
wx_url = 'https://pc.weixin.qq.com/'
wx_r = requests.get(wx_url).text
wx_mytree = lxml.etree.HTML(wx_r)
wx_lj = wx_mytree.xpath('//*[@id="downloadButton"]/@href')

# QQ
QQ_url = 'https://im.qq.com/pcqq'
QQ_r = requests.get(QQ_url).text
QQ_mytree = lxml.etree.HTML(QQ_r)
QQ_lj = QQ_mytree.xpath('//*[@id="app"]/div[2]/div[5]/div/a/@href')

# 企业微信
qyw_url = 'https://work.weixin.qq.com/#indexDownload'
qyw_r = requests.get(qyw_url).text
qyw_mytree = lxml.etree.HTML(qyw_r)
qyw_lj = qyw_mytree.xpath('//*[@id="indexDownload"]/div/a[1]/@href')
qyw_lj = 'https://work.weixin.qq.com'+str(qyw_lj[0])




def middle_windows(window, width=400, height=500):  # 设置窗口居中
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    x = int((screenwidth - width) / 2)  # x轴坐标
    y = int((screenheight - height) / 2)  # y轴坐标
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 放置窗口
    window.update()  # 更新窗口

a_list = []
def choose(event):
    widget = event.widget  # 当前的组件
    value = widget.get()  # 选中的值
    print('value:{}'.format(value))
    if value == '微信':

        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['微信'])  # 重新设置combobox2可下拉的值
        a_list.append(value)
    elif value == 'QQ':
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['QQ'])  # 重新设置combobox2可下拉的值
        a_list.append(value)
    elif value == '企业微信':
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['企业微信'])  # 重新设置combobox2可下拉的值
        a_list.append(value)
    elif value == '360浏览器':
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['360安全浏览器','360极速浏览器'])  # 重新设置combobox2可下拉的值
        a_list.append(value)
    elif value == '世界之窗':
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['世界之窗'])  # 重新设置combobox2可下拉的值
        a_list.append(value)
    else:
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=[])  # 重新设置combobox2可下拉的值


def choose2(event):
    widget = event.widget  # 当前的组件
    value = widget.get()  # 选中的值
    print('value:{}'.format(value))
    a_list.append(value)
    # print(a_list)
    # ccc(a_list)






def ccc():
    print(a_list)
    # print('开始下载',g_name)
    if a_list[-1] == '微信' :
        print('开始下载', '微信')
        url = wx_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('微信'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == 'QQ' :
        print('开始下载', 'QQ')
        url = QQ_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('Q'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == '企业微信' :
        print('开始下载', '企业微信')
        url = qyw_lj
        r = requests.get(url)
        with open("{}.exe".format('企业微信'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    # elif a_list[-1] == '360安全浏览器' :
    #     print('开始下载', '360安全浏览器')
    #     url = san_lj[0]
    #     r = requests.get(url)
    #     with open("{}.exe".format('360安全浏览器'), "wb") as code:
    #         code.write(r.content)
    #     print('下载完毕')
    # elif a_list[-1] == '360极速浏览器' :
    #     print('开始下载', '360极速浏览器')
    #     url = sanjs_lj[0]
    #     r = requests.get(url)
    #     with open("{}.exe".format('360极速浏览器'), "wb") as code:
    #         code.write(r.content)
    #     print('下载完毕')
    # elif a_list[-1] == '世界之窗' :
    #     print('开始下载', '世界之窗')
    #     url = sj_lj[0]
    #     r = requests.get(url)
    #     with open("{}.exe".format('世界之窗'), "wb") as code:
    #         code.write(r.content)
    #     print('下载完毕')



if __name__ == '__main__':

    win = Tk()
    middle_windows(win)
    win.title('南风丶轻语-浏览器下载')  # 标题
    label = tkinter.Label(win,
                          text="不要连续点击点击之后等待即可",
                          bg="black", fg="red",
                          font=("黑体", 20),
                          width=30,
                          height=1,
                          wraplength=500,
                          justify="left",
                          anchor="nw")

    # 显示出来
    label.pack()







    values1 = ['微信', 'QQ', '企业微信']

    value1 = StringVar(win)
    value1.set(values1[0])
    value1.set('请选择')  # 默认选中CCC==combobox.current(2)
    combobox1 = ttk.Combobox(
            master=win,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=20,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('', 16),  # 字体
            textvariable=value1,  # 通过StringVar设置可改变的值
            values=values1,  # 设置下拉框的选项
            background='pink',
            )
    print(combobox1.keys())  # 可以查看支持的参数
    combobox1.bind('<<ComboboxSelected>>', choose)  # 绑定选中事件
    combobox1.pack(pady=(50, 0))




    def thread_it(func, *args):
        '''将函数打包进线程'''
        # 创建
        t = threading.Thread(target=func, args=args)
        # 守护 !!!
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()
    button4 = tkinter.Button(win, text="下载", command=lambda: thread_it(ccc), width=10, height=1)
    button4.pack()
    button4.place(x=230, y=300)




    value2 = StringVar(win)
    value2.set('')
    combobox2 = ttk.Combobox(
            master=win,  # 父容器
            height=10,  # 高度,下拉显示的条目数量
            width=20,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('', 16),  # 字体
            textvariable=value2,  # 通过StringVar设置可改变的值
            )
    # print(combobox2.keys())  # 可以查看支持的参数
    combobox2.bind('<<ComboboxSelected>>', choose2)  # 绑定选中事件
    combobox2.pack(pady=(100, 0))

    win.mainloop()

