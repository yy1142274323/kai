import tkinter,threading
import requests,re,time
from tkinter import *
from copyheaders import headers_raw_to_dict










# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("yudanqu")
# 设置大小和位置
win.geometry("400x600+300+100")





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
                      text="这个什么也不是",
                      bg="black", fg="red",
                      font=("黑体", 20),
                      width=20,
                      height=1,
                      wraplength=200,
                      justify="left",
                      anchor="nw")
# 显示出来
label.pack()




def func():
    print("aaaaaaaaaaaaaaaaaaaaaaa")

# 创建按钮
button1 = tkinter.Button(win, text="按钮ONE", command=func, width=10, height=1)
button1.pack()
button1.place(x=300,y=450)

button2 = tkinter.Button(win, text="按钮TWO", command=lambda: print("bbbbbbbbbbbb"), width=10, height=1)
button2.pack()
button2.place(x=300,y=500)

button3 = tkinter.Button(win, text="退出", command=win.quit, width=10, height=1)
button3.pack()
button3.place(x=300,y=550)




def showinfo():
    # 获取输入的内容
    print(entry.get())
    lj = entry.get()




    # title = res['title']
    #
    #
    #
    # '''
    # 文本控件：用于显示多行文本
    # '''
    #
    # # height表示的是显示的行数
    # text = tkinter.Text(win, width=50, height=8)
    # text.pack()
    #
    # str = title
    # text.insert(tkinter.INSERT, str)
    #
    #




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


'''
entry = tkinter.Entry(win, bd=2,width =50)
entry.pack()
button4 = tkinter.Button(win, text="输出词条", command=showinfo, width=10, height=1)
button4.pack()
button4.place(x=300,y=400)

'''
entry = tkinter.Entry(win, bd=2,width =50)
entry.pack()

button4 = tkinter.Button(win, text="输出词条", command=lambda :thread_it(showinfo), width=10, height=1)
button4.pack()
button4.place(x=300,y=400)



# 进入消息循环，可以写控件
win.mainloop()










