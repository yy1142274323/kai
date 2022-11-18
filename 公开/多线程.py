# -*- coding:utf-8 -*-
# 线程使用的方式一
import threading

# 需要多线程运行的函数
def fun(args):
    for i in range(10):
        print(i)
    print("我是线程%s" % args)
    print("线程%s运行结束" % args)


# 创建线程
t1 = threading.Thread(target=fun(1))
t2 = threading.Thread(target=fun, args=(2,))
t3 = threading.Thread(target=fun, args=(3,))
t4 = threading.Thread(target=fun, args=(4,))
t5 = threading.Thread(target=fun, args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print("主线程结束")
