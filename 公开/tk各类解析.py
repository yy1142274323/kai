
import requests,re,time
from lxml import etree
from copyheaders import headers_raw_to_dict

from tkinter import *


window = Tk()
window.title("First Window")
window.geometry("1050x500")
lbl = Label(window, text="输入链接")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
def clicked():
    # res = "好了" + txt.get()
    # lbl.configure(text=res)
    if txt.get()[:21]=='http://h5.ippzone.com':
        lj = 'https://api.tencentbridge.com/open/video/pipigaoxiao.php?url={}'.format(txt.get())
        l = Label(window, text=lj)
        l.grid(column=10, row=0)
    elif txt.get()[:21]=='https://v.kuaishou.co':
        lj = 'https://api.tencentbridge.com/open/video/kuaishou.php?url={}'.format(txt.get())
        print(lj)
btn = Button(window, text="解析", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()