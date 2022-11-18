
import tkinter,time,requests,json,threading
import requests,json,time,datetime
from chinese_calendar import is_workday


#获取一个月多少天
import calendar


# url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
# token = requests.get(url1).json()['access_token']
# # print('token:', token)
# # 部门
# url_bm = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={}'.format(token)
# res_bm = requests.get(url_bm).json()['department']
# # print(res_bm)
#
# for i in res_bm:
#     # print(i['id'],i['name'],i['department_leader'])
#     # print(i)
# #
# #     # #成员
#     url_cy = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child=0'.format(
#         token, i['id'])
#     res_cy = requests.get(url_cy).json()
#     # print(len(res_cy['userlist']))
#     # print(res_cy['userlist'])
#
#     z =1
#     for i_2 in res_cy['userlist']:
#         # print(i_2)
#         user_id = i_2['userid']
#         user_name = i_2['name']
#         bm_id = i_2['department'][0]
#         print('姓名：',user_name,'*****************','所属分类：',bm_id,'*****************','工号：',user_id)







#成员+

# url_cy = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child=0'.format(
#     token, '476')
# res_cy = requests.get(url_cy).json()
# print(res_cy['userlist'])
# z = 1
# for i_2 in res_cy['userlist']:
#     print(i_2)
#     user_id = i_2['userid']
#     user_name = i_2['name']
#     bm_id = i_2['department']


# bm_id = ['308','476']
# bm_id = ['308']
# for a_bm_id in bm_id:
#     bm_list = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={}&id={}'.format(token,a_bm_id)
#     bm_list_id = requests.get(bm_list).json()['department']
#     for b_bm in bm_list_id:
#         # 成员+
#         url_cy = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child=0'.format(
#             token, b_bm['id'])
#         res_cy = requests.get(url_cy).json()
#         # print(res_cy['userlist'])
#         z = 1
#         for i_2 in res_cy['userlist']:
#             print(i_2)
#             user_id = i_2['userid']
#             user_name = i_2['name']
#             bm_id = i_2['department']













#308 476










#
#
# nian = 2022
# yue = 5
#
#
# monthRange = calendar.monthrange(nian,yue)
# da = monthRange[1]
# print (monthRange[1],',天')
#
#
#
#
# url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
# token = requests.get(url1).json()['access_token']
# print('token:', token)
#
#
#
#
#
#
# for reg in range(1,da+1):
#     url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
#     token = requests.get(url1).json()['access_token']
#     # print('token:', token)
#     # print('循环第{}次'.format(reg),'有{}天'.format(da),'{}月'.format(yue),bm_id)
#
#
#     times_1 = time.mktime(time.strptime("2022-{}-{} 05:00:00".format(yue,reg),"%Y-%m-%d %H:%M:%S"))
#
#     if reg == da:
#         # reg = 0
#         # print(yue+1,reg)
#         times_2 = time.mktime(time.strptime("2022-{}-{} 05:00:00".format(yue+1,1),"%Y-%m-%d %H:%M:%S"))
#         # print(times_2)
#         nyr = '{}-{}-{}'.format(nian, yue, reg)
#
#     else:
#         times_2 = time.mktime(time.strptime("2022-{}-{} 05:00:00".format(yue, reg+1), "%Y-%m-%d %H:%M:%S"))
#         nyr = '{}-{}-{}'.format(nian, yue, reg)
#     url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
#     token = requests.get(url1).json()['access_token']
#     # print('token:',token)
#
#
#
#     # ------------------------------------------------------------------------------------------------------------------------
#     url2 = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckin_daydata?access_token={}'.format(token)
#     # print(url2)
#     # url2 = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckin_monthdata?access_token=ACCESS_TOKEN'
#     data1 = {
#         "starttime": times_1,
#         "endtime": times_2,
#         "useridlist": [
#             '3234'
#         ]
#     }
#     date_1 = datetime.datetime.fromtimestamp(times_1)
#     # print(date_2)
#
#     date_2 = datetime.datetime.fromtimestamp(times_2)
#     # print(date_2)
#     print(date_1, date_2)
#     res = requests.post(url=url2, data=json.dumps(data1)).json()
#     print(res)



m = 500
i = 1
while m>1 :
    print(i)
    m-=1
    i+=1



















