import os
import shutil
# 导入模块
from tkinter import *
import tkinter
import random,threading,win32api,win32con, shutil,os,sys

# yyy = 'D:\/61434\Desktop\/111'
# # yyy = 'Q:\/10 常用软件\新电脑cad配置所需文件\Fonts'
# mmm = 'D:\/61434\Desktop\/222'
# def copy_allfiles(yyy,mmm):
# #src:原文件夹；dest:目标文件夹
#   src_files = os.listdir(yyy)
#   for file_name in src_files:
#     full_file_name = os.path.join(yyy, file_name)
#     if os.path.isfile(full_file_name):
#         shutil.copy(full_file_name, mmm)
#
#
#
# copy_allfiles(yyy,mmm)




def showinfo():
    # 获取输入的内容
    print(entry.get())
    lj = entry.get()



def song_download():
    # 创建文件夹
    # os.makedirs("music",exist_ok=True)
    # path = 'music\{}.mp3'.format(title)
    text.insert(END,'11111')
    # 文本框滑动
    text.see(END)
    # 更新
    text.update()
    text.insert(END,'22222')
    # 文本框滑动
    text.see(END)
    # 更新
    text.update()
# 1.用户界面
# 创建画板
root = Tk()
# 设置窗口标题
root.title('多功能处理器')
# 设置窗口大小以及出现的位置
root.geometry('860x620+400+200')
# 标签组件
label = Label(root,text="日期：",font=('楷体',20))
label.grid(row=2,columnspan=2)
# 定位与布局
label.grid(row=0)
# 输入框组件
entry = Entry(root,font=('宋体',20))
entry.grid(row=0,column=2)
# entry = tkinter.Entry(root, bd=2,width =50)
# entry.grid(row=0,column=2)
# entry.pack()


# 列表框
text = Listbox(root,font=('楷体',12),width=80,height=30)
text.grid(row=5,columnspan=10)
# 下载按钮
button1 = Button(root,text='test1',font=('楷体',15),command=showinfo)
button1.grid(row=0,column=5)



# 显示界面
root.mainloop()









