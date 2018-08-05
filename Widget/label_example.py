# -*- coding=utf-8 -*-
import sys
import os

# pylint: disable=E0611
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton, QDialog, QLineEdit, QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette

class LoginDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')
        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                  Qt.Horizontal, self)
        self.setLayout(QGridLayout())
        self.layout().addWidget(nameLabel, 0, 0)
        self.layout().addWidget(nameLineEdit, 0, 1, 1, 2)

        self.layout().addWidget(passwordLabel, 1, 0)
        self.layout().addWidget(passwordLineEdit, 1, 1, 1, 2)

        self.layout().addWidget(btnBox, 2, 1, 1, 2)

class Demo(QWidget):

    def __init__(self):
        super().__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        btn = QPushButton('login', self)
        login = LoginDialog()

        # 1. 初始化标签控件
        label1.setText("This is a text label")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>welcome to use Python GUI Application </a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('This is a photo label')

        # 有时工作目录并非在当前py文件所在目录，故使用绝对路径来定位资源文件
        dirName, fileName = os.path.split(os.path.abspath(__file__))
        relativePixmap = "../images/python.jpg"
        label3.setPixmap(QPixmap(os.path.join(dirName, relativePixmap)))

        label4.setText("<a href='http://www.cnblogs.com/wangshuo1/'> welcome to visit xinping`s house </a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('This is a hyperlink label')

        #2 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        vbox.addWidget(btn)

        #3 允许label1控件访问超链接
        label1.setOpenExternalLinks(True)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        label4.setOpenExternalLinks(False)
        label4.linkActivated.connect(self.link_clicked)

        label2.linkHovered.connect(self.link_hovered)

        btn.clicked.connect(self.login_clicked)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel Demo")

    def link_hovered(self):
        print("when mouse hovered label-2")

    def link_clicked(self):
        print("when mouse clicked label-4")

    def login_clicked(self):
        login = LoginDialog()
        login.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Demo()
    d.show()
    sys.exit(app.exec())