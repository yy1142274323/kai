from chinese_calendar import is_workday
import datetime,time
from datetime import date, timedelta



now = time.time()  # 返回float数据
#  获取当前时间戳---秒级级
print(int(now))
# 将unix时间戳转换为“当前时间”格式
date_2 = datetime.datetime.fromtimestamp(int(now))
print(date_2)


if is_workday(date_2):
    print("{}是工作日".format(date_2))
else:
    print("{}是休息日".format(date_2))




import calendar
monthRange = calendar.monthrange(2022,7)
print (monthRange[1])





from threading import Timer
import datetime
# 每隔两秒执行一次任务
# def printHello():
#     print('TimeNow:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#     t = Timer(2, printHello)
#     t.start()
#
# if __name__ == "__main__":
#     printHello()




yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d 9:0:0")
# a = int(time.mktime(yesterday))
print(yesterday)
timeArray = time.strptime(yesterday, "%Y-%m-%d %H:0:0")
print(timeArray)
# 转换为时间戳:
timeStamp = int(time.mktime(timeArray))
print(timeStamp)#1381419600



today = datetime.datetime.now().strftime('%Y-%m-%d 16:0:0')
print(today)
# 将其转换为时间数组
timeArray = time.strptime(today, "%Y-%m-%d %H:0:0")
print(timeArray)
# 转换为时间戳:
timeStamp = int(time.mktime(timeArray))
print(timeStamp)#1381419600



