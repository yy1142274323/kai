import tkinter,threading
import http.client, mimetypes, urllib, json, time, requests,os,re
from copyheaders import headers_raw_to_dict




# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("站酷图片下载工具")
# 设置大小和位置
win.geometry("500x250+300+100")




# Label:标签控件,可以显示文本
# win：父窗体
# text：显示的文本内容
# bg：背景色
# fg：字体颜色
# font：字体
# wraplength：指定text文本中多宽之后换行
# justify：设置换行后的对齐方式
# anchor：位置 n北，e东，w西，s南，center居中；还可以写在一起：ne东北方向
label = tkinter.Label(win,
                      text="牢记：www.677688521.xyz",
                      bg="black", fg="red",
                      font=("黑体", 15),
                      width=25,
                      height=10,
                      wraplength=500,
                      justify="left",
                      anchor="nw",
                      )
# 显示出来
label.pack()




# def func():
#     print("aaaaaaaaaaaaaaaaaaaaaaa")

# 创建按钮
# button1 = tkinter.Button(win, text="按钮ONE", command=func, width=10, height=1)
# button1.pack()
# button1.place(x=300,y=450)
#
# button2 = tkinter.Button(win, text="按钮TWO", command=lambda: print("bbbbbbbbbbbb"), width=10, height=1)
# button2.pack()
# button2.place(x=300,y=500)

button3 = tkinter.Button(win, text="退出", command=win.quit, width=10, height=1)
button3.pack()
button3.place(x=400,y=150)




def showinfo():
    # 获取输入的内容
    # print(entry.get())
    lj = entry.get()





    #`````````````````````````````````````````````````
    m = 100
    s = 21
    while s > 0:

        # print(s)
            '''
            文本控件：用于显示多行文本
            '''

            # height表示的是显示的行数
            text = tkinter.Text(win, width=30, height=8)
            text.pack()

            str = '已经开始执行了不要再点了耐心等待'
            text.insert(tkinter.INSERT, str)



            res_1 = requests.get(lj).text
            try:
                pattern = '<input type="hidden" id="dataInput" data-objid="(.*?)" data-objtype='
                id = re.findall(pattern, res_1)[0]
                print(id)

                url_2 = 'https://www.zcool.com.cn/work/content/show?p={}&objectId={}'.format(2, id)

                res_2 = requests.get(url_2).text
                res_2 = json.loads(res_2)
                print(res_2)
            except:
                pass

            try:
                # list = res_2['data']['product']['productImages']
                list = res_2['data']['allImageList']
                title = res_2['data']['product']['title']
                if not os.path.exists('./{}'.format(title)):
                    os.makedirs('./{}'.format(title))
                for i in list[::-1]:
                    lj_2 = i['url']
                    # print(lj)
                    f = requests.get(url=lj_2).content
                    with open('{}\\{}.jpg'.format(title, m), 'wb') as l:
                        l.write(f)
                    m -= 1
            except:
                print('没这页面')
            s -= 1
            end = time.time()
            print('一共用时{}'.format(end-star))







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



entry = tkinter.Entry(win, bd=2,width =50)
entry.pack()

button4 = tkinter.Button(win, text="输出词条", command=lambda :thread_it(showinfo), width=10, height=1)
button4.pack()
button4.place(x=400,y=100)





# 进入消息循环，可以写控件
win.mainloop()








































