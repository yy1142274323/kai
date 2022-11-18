# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/21 16:17
@Auth ： 小黑
@File ：新浪搜索.py
@IDE ：PyCharm
@Motto:离人愁
"""
import time,datetime
import pymysql.cursors
import requests,json,re
from copyheaders import headers_raw_to_dict
from lxml import etree
from fake_useragent import UserAgent
from random import choice
from pytypecho import Typecho, Post

now = time.time()  # 返回float数据
#  获取当前时间戳---秒级级
print(int(now))

head = {'User-Agent': UserAgent().random}



def run():


    url_dl = 'https://ip.jiangxianli.com/?page=1'
    ip_dl = requests.get(url_dl).text
    html = etree.HTML(ip_dl)
    tp = html.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr/td[11]/button[1]/@data-url')
    print(tp)





    url = 'https://search.sina.com.cn/news'
    headers_list = {
        'referer': 'https://search.sina.com.cn/news',
        'user-agent': head['User-Agent']

    }
    for xh in range(5)[::-1]:
        if xh > 0 :
            # print(xh)
            data = {
                'q': '汉服',
                'c': 'news',
                'range':'all',
                'size': '7',
                'page': xh,
            }
            print(url)

            try:
                ip_1 = choice(tp)
                print('随机取出的是:', choice(tp))
                proxy_ip = {
                    'http': ip_1,
                    # 'https': ip_proxy,
                }
                res = requests.post(url=url,headers=headers_list,data=data,proxies=proxy_ip)
            except:
                try:
                    ip_1 = choice(tp)
                    print('随机取出的是:', choice(tp))
                    proxy_ip = {
                        'http': ip_1,
                        # 'https': ip_proxy,
                    }
                    res = requests.post(url=url, headers=headers_list, data=data, proxies=proxy_ip)
                except:
                    ip_1 = choice(tp)
                    print('随机取出的是:', choice(tp))
                    proxy_ip = {
                        'http': ip_1,
                        # 'https': ip_proxy,
                    }
                    print('使用代理的IP:', proxy_ip)
                    res = requests.post(url=url, headers=headers_list, data=data, proxies=proxy_ip)



            res.encoding = "utf-8"
            print(res)
            html = etree.HTML(res.text)
            tp = html.xpath('//*[@id="result"]/div/h2/a/@href')
            for i in tp[::-1]:
                print(i)
                try:
                    wz_sj_m = requests.get(i,proxies=proxy_ip)
                    wz_sj_m.encoding = "utf-8"
                    # print(wz_sj_m.apparent_encoding)
                    # print(wz_sj_m.encoding)
                    wz_sj = wz_sj_m.text
                    # print(wz_sj)

                    html_wz = etree.HTML(wz_sj)
                    title = html_wz.xpath('//h1/text()')[0]
                    print(title)

                    #                <!-- 原始正文 -->
                    pattern='			<!-- 正文 start -->(.*)<div style="font-size: 0px; height: 0px; clear: both;"></div><div class="article-notice" style="border: 1px solid #FF6861;border-radius: 4px;padding: 20px;font-family: MicrosoftYaHei;font-size: 14px;color: #FF6861;line-height: 24px;margin-top: 30px;">特别声明：以上文章内容仅代表作者本人观点，不代表新浪网观点或立场。如有关于作品内容、版权或其它问题请于作品发表后的30日内与新浪网联系。</div>'
                    res=re.search(pattern, wz_sj, re.S)
                    print(res.group(1))
                    s = res.group(1)





                    conn = pymysql.connect(host='81.70.52.65', user='www', password='www', database='www')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM typecho_contents where title = %s ",title)
                    # 查询所有符合条件的
                    keywords_list = cur.fetchall()
                    if keywords_list == ():
                        print('不在')
                        # sql = "INSERT INTO typecho_contents (title,text,authorId,created,modified) VALUES ('%s','%s','%s','%s','%s')"
                        # data = (title, s,int(1),now,now)
                        # cur.execute(sql % data)
                        # conn.commit()
                        #
                        # cur.execute('SELECT cid FROM typecho_contents where title = %s',title)
                        # keywords_list = cur.fetchall()[0][0]
                        # print(keywords_list)
                        #
                        #
                        # sql2 = "INSERT INTO typecho_relationships (cid,mid) VALUES ('%s','%s')"
                        # data2 = (keywords_list, 2)
                        # cur.execute(sql2 % data2)



                        # 如果是插入、删除、更新语句切记要写提交命令con.commit()
                        # conn.commit()
                        # cur.close()
                        # conn.close()


                        te = Typecho("http://iiiqs.com/index.php/action/xmlrpc", "yy677", "677688")
                        # 文章发布
                        print(type(title))
                        post = Post(title=str(title), categories=['汉服资讯'], description=s)
                        te.new_post(post, publish=True)


                    else:
                        print('在里面')

                except:pass





if __name__ == '__main__':
    run()


