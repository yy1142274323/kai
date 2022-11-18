# ***********************************************************************************************sql语句
import requests
from copyheaders import headers_raw_to_dict


import pymysql.cursors,datetime,time
now = time.time()  # 返回float数据
#  获取当前时间戳---秒级级
print(int(now))
# 将unix时间戳转换为“当前时间”格式
date_2 = datetime.datetime.fromtimestamp(int(now))
print(date_2)

import pymysql.cursors, datetime, time

now = time.time()  # 返回float数据
#  获取当前时间戳---秒级级
print(int(now))
# 将unix时间戳转换为“当前时间”格式
date_2 = datetime.datetime.fromtimestamp(int(now))
print(date_2)

conn = pymysql.connect(host='81.70.52.65', user='word', password='word', database='word')

cur = conn.cursor()

# sql = "INSERT INTO wp_posts (post_date_gmt,post_author) VALUES ('%s','%s')"
# data = (date_2, date_2,1)
# cur.execute(sql % data)
# # cur.execute(q)
# # 如果是插入、删除、更新语句切记要写提交命令con.commit()
# conn.commit()
# # print (cur.fetchall())
# cur.close()
# conn.close()



sql = 'SELECT * FROM wp_posts where post_title = "穿汉服不冷吗？同袍：不怕，我们有这些！123"'
cur.execute(sql)
#查询所有符合条件的
keywords_list = cur.fetchall()
if keywords_list==():
    print(123)
else:print(321)
print(keywords_list)





