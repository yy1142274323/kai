# !/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :pyside2.py
# @Time      :2020/12/15 11:02
# @Editor    :python
# @Author    :阿斌

'''
import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World")
    label.show()
    sys.exit(app.exec_())

'''

from PySide2.QtWidgets import QApplication, QLabel
# 从PySide2.QtWidgets中导入QApplicarion和QLabel这两个类，一个是应用程序类，一个是标签类。
app = QApplication()
# 生成一个应该程序对象，这个就是整个应用程序实例。
label = QLabel('啥也不是!')
# 生成一个标签对象，内容是Hello world!
label.show()
# 显示这个标签对象
app.exec_()
# 开启事件循环。即启动程序，进行主事件循环中。
# 注意，运行结果显示的只是一个label对象，并且这个label对象实际上是QWidget的子类。
# 然后关于app.exec_()这个方法调用，这个方法在父类里面，是一个静态方法。上面说了这个方法是用于开启事件循环的。那么怎么主动停止事件循环呢，其实还有一个方法就是exit([retcode=0])，调用这个方法就会停止事件循环。很明显，默认传递了一个为0的参数值，表示程序是正常退出，当然你也可以传递其它整数值。当传递的参数值为0时，背后实际上会调用quit()这个方法。所以说exit(0)等同于quit()。为什么结束一个程序这么复杂，因为存在事件循环，需要保证所有事件执行完毕再结束程序。
# app.exec_()的返回值实际上就是exit()的返回值。




