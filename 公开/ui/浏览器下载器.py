from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk
import tkinter,threading,requests

import lxml
from lxml import etree


# 谷歌
g_url = 'https://www.iplaysoft.com/tools/chrome/'
g_r = requests.get(g_url).text
g_mytree = lxml.etree.HTML(g_r)
g_lj = g_mytree.xpath('//*[@id="result"]/div/div/div[2]/a[2]/@href')
g_name = g_mytree.xpath('//*[@id="result"]/div/div/h3/text()')

# 火狐
h_url = 'https://www.firefox.com.cn/download/#esr'
h_r = requests.get(h_url).text
h_mytree = lxml.etree.HTML(h_r)
h_lj = h_mytree.xpath('//*[@id="esr"]/div[2]/ul/li[2]/a/@href')

# 双核
s_url = 'http://chrome.wlxb49.cn/kwgg211/'
s_r = requests.get(s_url).text
s_mytree = lxml.etree.HTML(s_r)
s_lj = s_mytree.xpath('//*[@id="downurl"]/@href')

# 360安全浏览器
san_url = 'https://browser.360.cn/'
san_r = requests.get(san_url).text
san_mytree = lxml.etree.HTML(san_r)
san_lj = san_mytree.xpath('//*[@id="loadnew"]/@href')

# 360急速浏览器
sanjs_url = 'http://browser.360.cn/ee/'
sanjs_r = requests.get(sanjs_url).text
sanjs_mytree = lxml.etree.HTML(sanjs_r)
sanjs_lj = sanjs_mytree.xpath('//*[@id="loadnew"]/@href')

# 世界之窗
sj_url = 'http://www.theworld.cn/'
sj_r = requests.get(sj_url).text
sj_mytree = lxml.etree.HTML(sj_r)
sj_lj = sj_mytree.xpath('/html/body/div[1]/div[3]/div/a/@href')



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
    if value == '谷歌浏览器':

        value2.set('')  # 设置默认是空串
        combobox2.configure(values=g_name)  # 重新设置combobox2可下拉的值
        a_list.append(value)
    elif value == '火狐浏览器':
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['firefox'])  # 重新设置combobox2可下拉的值
        a_list.append(value)
    elif value == '双核浏览器':
        value2.set('')  # 设置默认是空串
        combobox2.configure(values=['双核（伪谷歌）'])  # 重新设置combobox2可下拉的值
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
    if a_list[-1] == g_name[0] :
        print('开始下载', g_name[0])
        url = g_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('正式版(稳定版) 64 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == g_name[2] :
        print('开始下载', g_name[2])
        url = g_lj[1]
        r = requests.get(url)
        with open("{}.exe".format('正式版(稳定版) 32 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == g_name[4] :
        print('开始下载', g_name[4])
        url = g_lj[2]
        r = requests.get(url)
        with open("{}.exe".format('测试版 64 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == g_name[6] :
        print('开始下载', g_name[6])
        url = g_lj[3]
        r = requests.get(url)
        with open("{}.exe".format('测试版 32 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == g_name[8] :
        print('开始下载', g_name[8])
        url = g_lj[4]
        r = requests.get(url)
        with open("{}.exe".format('开发版 64 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == g_name[10] :
        print('开始下载', g_name[10])
        url = g_lj[5]
        r = requests.get(url)
        with open("{}.exe".format('开发版 32 位'), "wb") as code:
            code.write(r.content)
    elif a_list[-1] == g_name[12] :
        print('开始下载', g_name[12])
        url = g_lj[6]
        r = requests.get(url)
        with open("{}.exe".format('金丝雀版 64 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == g_name[14] :
        print('开始下载', g_name[14])
        url = g_lj[7]
        r = requests.get(url)
        with open("{}.exe".format('金丝雀版 32 位'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == 'firefox' :
        print('开始下载', 'firefox')
        url = h_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('firefox'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == '双核（伪谷歌）' :
        print('开始下载', '双核（伪谷歌）')
        url = s_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('双核浏览器'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == '360安全浏览器' :
        print('开始下载', '360安全浏览器')
        url = san_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('360安全浏览器'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == '360极速浏览器' :
        print('开始下载', '360极速浏览器')
        url = sanjs_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('360极速浏览器'), "wb") as code:
            code.write(r.content)
        print('下载完毕')
    elif a_list[-1] == '世界之窗' :
        print('开始下载', '世界之窗')
        url = sj_lj[0]
        r = requests.get(url)
        with open("{}.exe".format('世界之窗'), "wb") as code:
            code.write(r.content)
        print('下载完毕')



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







    values1 = ['谷歌浏览器', '火狐浏览器', '双核浏览器','360浏览器','世界之窗']

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

