import requests, json, time, datetime, re
from chinese_calendar import is_workday

# 获取一个月多少天
import calendar

nian = 2022
yue = 5

monthRange = calendar.monthrange(nian, yue)
da = monthRange[1]
print(monthRange[1], ',天')

url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
token = requests.get(url1).json()['access_token']
print('token:', token)

bm_id = ['478','479','485','510']
for a_bm_id in bm_id:

    bm_list = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={}&id={}'.format(token, a_bm_id)
    bm_list_id = requests.get(bm_list).json()['department']
    print(bm_list_id)
    for b_bm in bm_list_id:
        # 成员+
        url_cy = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={}&department_id={}&fetch_child=0'.format(
            token, b_bm['id'])
        res_cy = requests.get(url_cy).json()
        print(res_cy['userlist'])
        z = 1
        for i_2 in res_cy['userlist']:
            print(i_2)
            user_id = i_2['userid']
            try:

                pat = re.compile(r'[\u4e00-\u9fa5]+')
                user_name = pat.findall(i_2['name'])[0]
            except:
                # user_name = i_2['name']
                pass


            bm_id = i_2['department']
            # gh = '2742'

            for reg in range(1, da + 1):
                url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
                token = requests.get(url1).json()['access_token']
                print('token:', token)
                print('循环第{}次'.format(reg), '有{}天'.format(da), '{}月'.format(yue), bm_id)

                times_1 = time.mktime(time.strptime("2022-{}-{} 05:00:00".format(yue, reg), "%Y-%m-%d %H:%M:%S"))

                if reg == da:
                    # reg = 0
                    # print(yue+1,reg)
                    times_2 = time.mktime(time.strptime("2022-{}-{} 05:00:00".format(int(yue) + 1, 1), "%Y-%m-%d %H:%M:%S"))
                    # print(times_2)

                    nyr = '{}-{}-{}'.format(nian, yue, reg)



                else:
                    times_2 = time.mktime(
                        time.strptime("2022-{}-{} 05:00:00".format(yue, reg + 1), "%Y-%m-%d %H:%M:%S"))
                    nyr = '{}-{}-{}'.format(nian, yue, reg)

                url1 = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx4b8d64731b29abc1&corpsecret=5TgtjjZu65VB2z3KDjTCqffHMt6g9ZOZroVXmZx0e5k'
                token = requests.get(url1).json()['access_token']
                print('token:', token)

                # ------------------------------------------------------------------------------------------------------------------------
                url2 = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckin_daydata?access_token={}'.format(token)
                # print(url2)
                # url2 = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckin_monthdata?access_token=ACCESS_TOKEN'
                data1 = {
                    "starttime": times_1,
                    "endtime": times_2,
                    "useridlist": [
                        user_id
                    ]
                }
                print(user_id)
                print(times_1, times_2)
                res = requests.post(url=url2, data=json.dumps(data1)).json()
                # print(res)
                try:
                    xm = res['datas'][0]['base_info']['name']
                    print('姓名:', res['datas'][0]['base_info']['name'])  # 姓名

                    bm = res['datas'][0]['base_info']['departs_name'][15:]
                    print('分组:', res['datas'][0]['base_info']['departs_name'])  # 部门

                    qywxxm = res['datas'][0]['base_info']['name']  # 企业微信姓名
                    pat = re.compile(r'[\u4e00-\u9fa5]+')
                    result = pat.findall(qywxxm)[0]

                    # qywxbm = res['datas'][0]['base_info']['departs_name']#企业微信部门
                    szgzid = res['datas'][0]['base_info']['rule_info']['groupid']
                    print(szgzid)

                    user_id = res['datas'][0]['base_info']['acctid']
                    print('工号:', res['datas'][0]['base_info']['acctid'])

                    # 将unix时间戳转换为“当前时间”格式
                    date_2 = datetime.datetime.fromtimestamp(times_1)
                    # print(date_2)

                    if is_workday(date_2):

                        print("{}是工作日".format(date_2))
                        sfxxr = 0
                    else:
                        print("{}是休息日".format(date_2))
                        sfxxr = 1

                    # sfxxr = res['datas'][0]['base_info']['day_type']
                    # print('判断是否工作日(0工作日)(1休息):',res['datas'][0]['base_info']['day_type'])

                    sbsj = res['datas'][0]['summary_info']['earliest_time']
                    print('上班时间:', res['datas'][0]['summary_info']['earliest_time'])
                    # print('上班时间:',res['datas'][0]['summary_info']['earliest_time']/60/60)
                    xbsj = res['datas'][0]['summary_info']['lastest_time']
                    print('下班时间:', res['datas'][0]['summary_info']['lastest_time'])
                    # gzrjbscxs = res['datas'][0]['ot_info']['ot_duration']/3600
                    # print('工作日加班时长（小时）:',gzrjbscxs)
                    gzrjbscxs = round(res['datas'][-1]['ot_info']['ot_duration'] / 3600)
                    print('工作日加班时长（小时）:', gzrjbscxs)

                    url3 = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata?access_token={}'.format(token)
                    data3 = {
                        "opencheckindatatype": 3,
                        "starttime": times_1,
                        "endtime": times_2,
                        "useridlist": [
                            user_id
                        ]
                    }
                    res3 = requests.post(url=url3, data=json.dumps(data3)).json()
                    print(res3)
                    try:
                        un_time = res3['checkindata'][0]['checkin_time']
                        # 将unix时间戳转换为“当前时间”格式
                        times = datetime.datetime.fromtimestamp(un_time)
                        print(times)
                        # print(times.hour,'时')
                        h1 = times.hour * 3600
                        # print(times.minute,'分')
                        f1 = times.minute * 60
                        un_time2 = res3['checkindata'][-1]['checkin_time']
                        # print(un_time2)
                        # 将unix时间戳转换为“当前时间”格式
                        times2 = datetime.datetime.fromtimestamp(un_time2)
                        print(times2)

                        # print(times2.hour,'时')
                        h2 = times2.hour * 3600
                        # print(times2.minute,'分')
                        f2 = times2.minute * 60
                        if h2 > h1:  # 如果下班时间大于上班时间
                            print('没过夜--------------------------------------------------------------')
                            aaaa = round(((h2 + f2) - (h1 + f1)) / 3600, 2)

                            bbb = round((32400 - h1) / 3600, 2)
                            if bbb < 0:
                                bbb = 0
                            print('当日5-9点加班时长（小时）', bbb, '小时')
                            print('非工作日加班时长（小时)', aaaa, '小时')
                        elif h2 < h1:  # 如果下班时间小于上班时间
                            print('在这过夜了----------------------------------------------------------')
                            aaaa = round((86400 - (h1 + f1) + h2 + f2) / 3600, 2)
                            bbb = round((32400 - h1) / 3600, 2)
                            if bbb < 0:
                                bbb = 0
                            print('当日5-9点加班时长（小时）', bbb, '小时')
                            print('非工作日加班时长（小时)', aaaa, '小时')

                        if sfxxr == 0:
                            print('工作日------------------------------------------------------------------')

                            drzjbsc = gzrjbscxs + bbb
                            print('当日总加班时长', drzjbsc, '小时')
                        else:
                            print('非工作日-----------------------------------------------------------------')
                            drzjbsc = aaaa

                            print('当日总加班时长', drzjbsc, '小时')
                    except:
                        bbb = 0
                        print('当日5-9点加班时长（小时）', bbb, '小时')
                        aaaa = 0
                        print('非工作日加班时长（小时)', aaaa, '小时')
                        drzjbsc = 0
                        print('当日总加班时长', drzjbsc, '小时')
                        times = 0
                        times2 = 0
                except:

                    bm = 0
                    qywxxm = 0
                    szgzid = 0
                    sfxxr = 0
                    times = 0
                    times2 = 0
                    gzrjbscxs = 0
                    bbb = 0
                    aaaa = 0
                    drzjbsc = 0

                print('********************************************************************************************************************************************')


                import pymssql

                conn = pymssql.connect(host='10.10.60.108', user='sa', password='19761011Dzd', database='ecology')
                cur = conn.cursor()


                sql = "INSERT INTO uf_hqjbrbsj (xm,qywxbm,qywxxm,gh,szgzid,rq,sfxxr,sbsj,xbsj,gzrjbscxs,dr59djbscxs,fgzrjbscxs,drzjbsc,nf,yf) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

                data = (user_name, bm, user_name, user_id, szgzid, nyr, sfxxr, times, times2, gzrjbscxs, bbb, aaaa, drzjbsc,str(nian), str(nian)+'-'+str(yue))


                cur.execute(sql % data)
                # cur.execute(q)
                # 如果是插入、删除、更新语句切记要写提交命令con.commit()
                conn.commit()
                # print (cur.fetchall())
                cur.close()
                conn.close()
















