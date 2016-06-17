# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(454, 413)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.usr_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.usr_line_edit.setGeometry(QtCore.QRect(150, 130, 181, 21))
        self.usr_line_edit.setObjectName(_fromUtf8("usr_line_edit"))
        self.pwd_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.pwd_line_edit.setGeometry(QtCore.QRect(150, 170, 181, 21))
        self.pwd_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd_line_edit.setObjectName(_fromUtf8("pwd_line_edit"))
        self.re_enter_pwd_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.re_enter_pwd_line_edit.setGeometry(QtCore.QRect(150, 210, 181, 21))
        self.re_enter_pwd_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.re_enter_pwd_line_edit.setObjectName(_fromUtf8("re_enter_pwd_line_edit"))
        self.reenter_pwd_label = QtGui.QLabel(self.centralwidget)
        self.reenter_pwd_label.setGeometry(QtCore.QRect(20, 210, 111, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reenter_pwd_label.sizePolicy().hasHeightForWidth())
        self.reenter_pwd_label.setSizePolicy(sizePolicy)
        self.reenter_pwd_label.setObjectName(_fromUtf8("reenter_pwd_label"))
        self.pwd_label = QtGui.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(70, 170, 71, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd_label.sizePolicy().hasHeightForWidth())
        self.pwd_label.setSizePolicy(sizePolicy)
        self.pwd_label.setObjectName(_fromUtf8("pwd_label"))
        self.usr_name_label = QtGui.QLabel(self.centralwidget)
        self.usr_name_label.setGeometry(QtCore.QRect(70, 130, 71, 20))
        self.usr_name_label.setObjectName(_fromUtf8("usr_name_label"))
        self.register_label = QtGui.QLabel(self.centralwidget)
        self.register_label.setGeometry(QtCore.QRect(170, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.register_label.setFont(font)
        self.register_label.setAlignment(QtCore.Qt.AlignCenter)
        self.register_label.setObjectName(_fromUtf8("register_label"))
        self.register_button = QtGui.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(150, 310, 181, 41))
        self.register_button.setObjectName(_fromUtf8("register_button"))
        self.reenter_pwd_label_2 = QtGui.QLabel(self.centralwidget)
        self.reenter_pwd_label_2.setGeometry(QtCore.QRect(80, 250, 61, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reenter_pwd_label_2.sizePolicy().hasHeightForWidth())
        self.reenter_pwd_label_2.setSizePolicy(sizePolicy)
        self.reenter_pwd_label_2.setObjectName(_fromUtf8("reenter_pwd_label_2"))
        self.re_enter_pwd_line_edit_2 = QtGui.QLineEdit(self.centralwidget)
        self.re_enter_pwd_line_edit_2.setGeometry(QtCore.QRect(150, 250, 181, 21))
        self.re_enter_pwd_line_edit_2.setEchoMode(QtGui.QLineEdit.Normal)
        self.re_enter_pwd_line_edit_2.setObjectName(_fromUtf8("re_enter_pwd_line_edit_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.reenter_pwd_label.setText(_translate("MainWindow", "Re enter Password", None))
        self.pwd_label.setText(_translate("MainWindow", "Password", None))
        self.usr_name_label.setText(_translate("MainWindow", "Username", None))
        self.register_label.setText(_translate("MainWindow", "Register", None))
        self.register_button.setText(_translate("MainWindow", "Register", None))
        self.reenter_pwd_label_2.setText(_translate("MainWindow", "Email ID", None))

