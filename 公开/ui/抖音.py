# !/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :抖音.py
# @Time      :2020/12/16 10:11
# @Editor    :python
# @Author    :阿斌
# coding: utf-8

import requests,json,copyheaders,time,re,os
from copyheaders import headers_raw_to_dict
from lxml import etree



# 'https://v.douyin.com/JqJb4SN/'
# 'https://www.iesdouyin.com/share/user/105107049084?iid=1565349952890989&sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U'
#
# ' https://v.douyin.com/JqeF1wV/'
# 'https://www.iesdouyin.com/share/video/6904855753044102413/'
#
# 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U&count=21&max_cursor=0&aid=1128&_signature=TCBxEwAAE.rFwUiJOVU2PUwgcQ&dytk='
# 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U&count=21&max_cursor=0&aid=1128&_signature=ExDrrAAATM37ysnRu34y0RMQ67&dytk='
# 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U&count=21&max_cursor=0&aid=1128&_signature=DTC0IQAAUu3l6pZcjbTxIQ0wtD&dytk='
# 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U&count=21&max_cursor=0&aid=1128&_signature=DJvoPgAAU0fkQcpD2Be8RQyb6C&dytk='




url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U&count=21&max_cursor=0&aid=1128&_signature=ExDrrAAATM37ysnRu34y0RMQ67&dytk='


head = headers_raw_to_dict(
    b'''


    referer: https://www.iesdouyin.com/share/user/105107049084?iid=1565349952890989&sec_uid=MS4wLjABAAAAUdkAUTiE7Oa7AWtOOe_gTqW4rS3lFdXdcVbTylha0-U
    user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
    
    '''
)





res = requests.get(url=url,headers= head).text
# res.encoding='utf-8'
# res=res.encode('utf-8'). decode('utf-8')
# res=res.encode('GBK')
print(res)
# r = json.loads(res)
# print(r)

# print ('张俊'.encode('utf-8'). decode('utf-8') )




























#当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == "__main__":
    run_code = 0