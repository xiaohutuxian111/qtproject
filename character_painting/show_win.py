# -*- coding: utf-8 -*-
# @Time    : 2023/9/17 22:58
# @Author  : stone
# @File    : show_win.py
# @desc    :
import sys

from wind import Ui_MainWindow
from PyQt5.QtWidgets import  QMainWindow,QApplication
from PyQt5 import QtGui
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        # 调色板类
        palette =  QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(
            QtGui.QPixmap('img/bg.png')  # 设置背景图片
        ))
        # 设置调色板
        self.centralwidget.setPalette(palette)
        # 打开位图
        input_img =QtGui.QPixmap('img/input_test.png')
        self.input_img.setPixmap(input_img)

        # 打开位图
        export_img = QtGui.QPixmap('img/output_test.png')
        self.export_img.setPixmap(export_img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =Main()
    main.show()
    sys.exit(app.exec_())

