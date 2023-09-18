# -*- coding: utf-8 -*-
# @Time    : 2023/9/17 22:58
# @Author  : stone
# @File    : show_win.py
# @desc    :
import _thread
import sys
import time

import conversion
from wind import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtGui


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralwidget.setAutoFillBackground(True)
        # 调色板类
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(
            QtGui.QPixmap('img/bg.png')  # 设置背景图片
        ))
        # 设置调色板
        self.centralwidget.setPalette(palette)
        # 打开位图
        input_img = QtGui.QPixmap('img/input_test.png')
        self.input_img.setPixmap(input_img)

        # 打开位图
        export_img = QtGui.QPixmap('img/output_test.png')
        self.export_img.setPixmap(export_img)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName()
        if openfile_name[0] != '':
            self.input_img = openfile_name[0]
            self.show_input_img(self.input_img)

    # 显示导入图片
    def show_input_img(self, file_path):
        input_img = QtGui.QPixmap(file_path)
        self.input_img.setPixmap(input_img)

    def start_conversion(self):
        if hasattr(main, 'input_path'):
            self.gif = QtGui.QMovie('img/loding.gif')
            self.loding.setMovie(self.gif)
            # 启动图片下载动效显示出来
            self.gif.start()
            _thread.start_new_thread(lambda: self.is_conversion(main.input_path))
        else:
            print("没有选择指定的图片路径")

    # 转换方法
    def is_conversion(self, file_path):
        t = str(int(time.time()))
        # 转换后字符画显示路径
        export_path = ('export_img\\export_img' + t + 'png')
        #  获取输入的字符
        input_char = main.textEdit.toPlainText()
        # 获取选中的内容
        definition = main.comboBox.currentText()
        # 调用转换字符的方法(file_path),并将他指定为路径
        is_over = conversion.picture_conversion(file_path, export_path, input_char, definition)
        if is_over == False:
            self.loding.clear()
            main.show_export_img(export_path)

    # 显示转换后的图片
    def show_export_img(self, file_path):
        export_img = QtGui.QPixmap(file_path)
        self.export_img.setPixmap(export_img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    # 为导入图片按钮指定打开图片文件路径事件
    main.pushButton_input.clicked.connect(main.openfile)
    # 为转换按钮指定启动转换图片的方法
    main.show()
    sys.exit(app.exec_())
