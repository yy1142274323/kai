#-*- codeing = utf-8 -*-
# @Time :21/9/22/0022 21:03
# @Author:zx 
# @File :test.PY 
# @sOFTWARE:PyCharm


import requests
import tkinter as tk
from lxml import etree


def get_info():
    url = 'https://www.ip138.com/mobile.asp?mobile={}&action=mobile'.format(e1.get())
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    # url = ""
    r = requests.get(url = url,
                     headers = headers
                     )
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    adderss = html.xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/span/text()")[0].replace('\xa0','')
    type = html.xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/span/text()")[0]
    add_number = html.xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/span/text()")[0]
    zip_code = html.xpath("/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/span/text()")[0]
    print(adderss,type,add_number,zip_code)

    l6 = tk.Label(root, text=adderss, fg="green", font=14, height=2)
    l6.grid(row=1, column=1)

    l7 = tk.Label(root, text=type, fg="green", font=14, height=2)
    l7.grid(row=2, column=1)

    l8 = tk.Label(root, text=add_number, fg="green", font=14, height=2)
    l8.grid(row=3, column=1)

    l9 = tk.Label(root, text=zip_code, fg="green", font=14, height=2)
    l9.grid(row=4, column=1)

def clear_info():
    e1.delete(0,"end")
root = tk.Tk()
root.geometry("300x250+1000+500")
root.title("手机号码查询工具")
l1 = tk.Label(root,text="查询的号码:",fg = "green",font=14,height = 2)
l1.grid(row=0,column=0)

e1 = tk.Entry(root,text="")
e1.grid(row=0,column=1)

l2 = tk.Label(root,text="卡号归属地:",fg = "green",font=14,height = 2)
l2.grid(row=1,column=0)

l3 = tk.Label(root,text="卡  类  型:",fg = "green",font=14,height = 2)
l3.grid(row=2,column=0)

l4 = tk.Label(root,text="区      号:",fg = "green",font=14,height = 2)
l4.grid(row=3,column=0)

l5 = tk.Label(root,text="邮      编:",fg = "green",font=14,height = 2)
l5.grid(row=4,column=0)

a1 = tk.Button(root,text="查询",fg = "red",font = 16,height = 2,command=get_info)
a1.grid(row=5,column=1)

a2 = tk.Button(root,text="清除",fg = "red",font = 16,height = 1,command=clear_info)
a2.grid(row=0,column=2)
root.mainloop()
# get_info()
