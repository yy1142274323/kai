# !/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :pyqt5.py
# @Time      :2020/12/15 12:22
# @Editor    :python
# @Author    :阿斌

import sys,requests,json
from  PyQt5 import QtGui,QtWidgets
# from PyQt5.Qt import *
import webbrowser
# from PyQt5 import QtWidgets   # 导入PyQt5部件
# app = QtWidgets.QApplication(sys.argv)  # 建立application对象
# first_window = QtWidgets.QWidget()  # 建立窗体对象
# first_window.resize(400, 300)  # 设置窗体大小
# first_window.setWindowTitle("我的第一个pyqt程序")  # 设置窗体标题
# first_window.show()  # 显示窗体
# sys.exit(app.exec())  # 运行程序





'''
# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()
    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(500, 150)
    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    w.move(1000, 200)
    # 设置窗口的标题
    w.setWindowTitle('Simple')
    # 显示在屏幕上
    w.show()

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())

'''




# QMessageBox  关闭按钮处调
# QDesktopWidget  控制窗口在中间引用

# from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox
# from PyQt5.QtGui import QFont,QIcon
#
#
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()  # 界面绘制交给InitUi方法
#
#     def initUI(self):
#
#         # 设置窗口的位置和大小
#         # self.setGeometry(300, 300, 300, 220)
#
#
#         # resize()方法调整窗口的大小。这离是250px宽150px高
#         self.resize(800, 600)
#
#         # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#         self.move(500, 200)
#
#
#         # 设置窗口的标题
#         self.setWindowTitle('这里啥也不是')
#         # 设置窗口的图标，引用当前目录下的web.png图片
#         self.setWindowIcon(QIcon('m1.ico'))
#
#
# # {
#         # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
#         QToolTip.setFont(QFont('SansSerif', 300))
#
#         # 创建一个PushButton并为他设置一个tooltip
#         btn = QPushButton('这是一个按钮,悬停试试看！', self)
#         btn.setToolTip('啥也不是？')
#
#         # btn.sizeHint()显示默认尺寸
#         # btn.resize(btn.sizeHint())``````````````````````````````````````````
#         btn.resize(200,200)
#
#
#         # 移动窗口的位置
#         btn.move(50, 100)
# # }
#
#
#
#
#
#
#
#
#
#
#
#
#
#         # 显示窗口
#         self.show()
#
#
# # {关闭窗口提示
#
#     def closeEvent(self, event):
#
#         reply = QMessageBox.question(self, '紧急提示',"你确定要关闭窗口吗？可能会有不好的事发生！", QMessageBox.Yes | QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
# # }
#










# if __name__ == '__main__':
#     # 创建应用程序和对象
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication,QLineEdit,QPushButton)

from PyQt5.QtGui import QPixmap,QIcon

# 重写QWidget类
class Window(QWidget):
    def __init__(self):
        # 初始化参数
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle('野驴短视频下载助手')

        self.setWindowIcon(QIcon('m1.ico'))
        # 设置窗口大小
        self.resize(650, 300)
        # 调用函数setup_ui()
        self.setup_ui()

    def setup_ui(self):



        #加图片
        pixmap = QPixmap("2.jpg")
        lbl = QLabel(self)
        lbl.move(490,150)
        lbl.setPixmap(pixmap)


        # 定义文本框内容判断的槽函数
        def text_cao(text):
            # 如果文本框内容不为空则按钮可用
            if text != '':
                button.setEnabled(True)
            # 否则按钮不可用
            else:
                button.setEnabled(False)

        # 定义鼠标点击函数;;
        def Button_Pressed():
            # 获取输入文本内容
            content = le.text()
            # print(content)
            url_jx = 'https://tenapi.cn/video/?url={}'.format(content)
            r = requests.get(url_jx).json()
            # print(r)
            # r = json.loads(r)
            write = r['url']
            name = r['title']
            print(write)
            print(name)
            # webbrowser.open(write)

            # label.setText(write)

            s = requests.get(url=write).content
            with open('视频\\{}.mp4'.format(name), 'wb') as l:
                l.write(s)

            #
            # # 判断输入文本内容是否为Sz
            # if content == 'Sz':
            #     # 更改标签显示内容
            #     label.setText('登录成功')
            # else:
            #     # 更改标签显示内容
            #     label.setText('登录失败')
            #


            # 展示标签
            label.show()
            # 根据内容调整标签大小
            label.adjustSize()

    # def initUI(self):


        # def Button_fw():
        #     webbrowser.open()














        # 创建一个标签
        label = QLabel(self)
        # 设置标签文本
        label.setText('公告：<a href = "https://jq.qq.com/?_wv=1027&k=7f5qzy63">痘印，筷手，屁屁搞笑，屁屁吓，西瓜等等等···点击入群：！</a>')
        label.setOpenExternalLinks(True)
        # 设置标签位置
        label.move(50, 50)
        # 把标签设置为隐藏
        # label.hide()




        # 创建一个标签
        label2 = QLabel(self)
        # 设置标签文本
        label2.setText('<a href = "wjb.koala8.cn">开源不易赏···个袁大头···行不行？       开源不易赏···个袁大头···行不行？</a>')
        label2.setOpenExternalLinks(True)
        # 设置标签位置
        label2.move(50, 280)
        # 把标签设置为隐藏
        # label.hide()




        # 创建一个文本框
        le = QLineEdit(self)
        # 设置文本内容
        # le.setText('输入分享链接：')
        le.setPlaceholderText('请输入分享链接：')

        # 设置文本位置
        le.move(50, 100)
        le.resize(400, 20)
        # 连接文本内容改变信号
        le.textChanged.connect(text_cao)

        # 创建一个按钮
        button = QPushButton(self)
        # 设置按钮内容
        button.setText('走你')
        # 设置按钮位置
        button.move(500, 100)
        # 把按钮设置为不可用
        button.setEnabled(False)
        # 连接鼠标点击函数
        button.pressed.connect(Button_Pressed)


        # # 创建一个按钮
        # button = QPushButton(self)
        # # 设置按钮内容
        # button.setText('访问')
        # # 设置按钮位置
        # button.move(600, 100)
        # # 把按钮设置为不可用
        # button.setEnabled(False)
        # # 连接鼠标点击函数
        # button.pressed.connect(Button_fw)







# 启动入口
if __name__ == '__main__':


    # 创建一个应用程序
    app = QApplication(sys.argv)
    # 创建一个窗口对象
    window = Window()
    # 展示窗口
    window.show()
    # 传递错误码 消息循环 无限循环 app.exec让程序进入循环

    sys.exit(app.exec_())
