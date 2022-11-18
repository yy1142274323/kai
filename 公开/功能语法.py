import re, requests, time, json, os
from copyheaders import headers_raw_to_dict
from fake_useragent import UserAgent


# pip install -i https://pypi.douban.com/simple/
'''
xpath********************************************************************************xpath
from lxml import etree
r = requests.get(url)
html = etree.HTML(r)
tp = html.xpath('//')

'''



'''
******************************************************************************************读取文本
fopen = open('qqq.txt', 'r')
lines = fopen.readlines()
for line in lines:
    line = line.strip('\n')  # 去掉换行符
    print(line)

'''



'''
********************************************************************************************随机请求头
from fake_useragent import UserAgent
headers = {'User-Agent': UserAgent().random}
'''



'''
**********************************************************************************************代理设置
    proxies = {
                'http': 'http://{}'.format('118.212.105.200:9999'),
                'https': 'https://{}'.format(line)
            }
    html = requests.get(url=url,headers=headers,proxies=proxies, timeout=3).text
'''




'''
************************************************************************************************写入写入写入写入
        # with open('qqq.txt','a+') as f:
        #     f.write(name)
        
        # with open('文件夹\\{}.jpg'.format(mz+1),'wb') as l:
        #     l.write(j)
        
        # path = '图片\\{}.jpg'.format(n)
        # with open(path, 'wb') as f:
        #     f.write(response)
'''




'''
***********************************************************************************************sql语句
import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    user='root',
    passwd='root',
    db='dysj'
)

# 获取游标
cursor = connect.cursor()

************************************************************************存东西
# sql = "INSERT IGNORE INTO 表名称 (表头1, 表头2) VALUES ('%s', '%s')"
sql = "INSERT IGNORE INTO auto (nickname, goodsurl) VALUES ('%s', '%s')"
# data = (数据1,数据2)
data = ("xx","cc")
cursor.execute(sql % data)


************************************************************************取东西
sql = "SELECT 要的东西 FROM 表名称 WHERE 条件比如（id >= 1）"
sql = "SELECT * FROM auto WHERE id >= 1"
sql = "SELECT 字段 FROM 表名 where 字段=0 "
cursor.execute(sql)
keywords_list = cursor.fetchall()
print(keywords_list)

******************************************************更改--------+-----伪format
sql = "UPDATE 表名 SET 字段 = 1 WHERE 字段 = ('%s')" % ci

****************************************************************************查询
sql = 'SELECT * FROM 表 where 字段 = "数据"'
sql = 'SELECT 字段 FROM 表 where 字段 = "数据"'
sql = 'SELECT * FROM task_listb where keyword = "玩具"'
cursor.execute(sql)
#查询所有符合条件的
keywords_list = cursor.fetchall()
print(keywords_list)

****************************************************************************删除
sql = "DELETE FROM 表名称 WHERE 列名称 = 值"
'''




'''
# ``````````````````````````````````````````````````````````````````````````导入xls表格·······································
import xlwt
workbook = xlwt.Workbook(encoding='utf-8')          #创建workbook 对象
worksheet = workbook.add_sheet('sheet100')          #创建工作表
worksheet.write(0,0,'hellow')                       #写入数据  行  列  内容
workbook.save('xxx.xls')                            #保存数据

'''




'''
    ***************************************************************************时间***
    # 获得当前时间时间戳
    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(otherStyleTime)
'''




'''
**********************************************************************************保存错误
# try:
#     print(a)
# except Exception as e:
#     b = str(e) + '\n\n'
#     with open('a.text', 'a+') as f:
#         f.write(b)
'''



'''
#########################################################################################调用exe 结束程序
import os,sys
main = "777.exe"
os.system(main)
sys.exit(0)
'''








