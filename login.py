# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        MainWindow.resize(490, 424)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.login_button = QtGui.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(190, 240, 171, 32))
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.notuser_label = QtGui.QLabel(self.centralwidget)
        self.notuser_label.setGeometry(QtCore.QRect(180, 290, 71, 20))
        self.notuser_label.setObjectName(_fromUtf8("notuser_label"))
        self.register_button = QtGui.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(260, 280, 121, 32))
        self.register_button.setObjectName(_fromUtf8("register_button"))
        self.usr_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.usr_line_edit.setGeometry(QtCore.QRect(200, 140, 181, 21))
        self.usr_line_edit.setText(_fromUtf8(""))
        self.usr_line_edit.setObjectName(_fromUtf8("usr_line_edit"))
        self.pwd_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.pwd_line_edit.setGeometry(QtCore.QRect(200, 180, 181, 21))
        self.pwd_line_edit.setText(_fromUtf8(""))
        self.pwd_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd_line_edit.setObjectName(_fromUtf8("pwd_line_edit"))
        self.usr_name_label = QtGui.QLabel(self.centralwidget)
        self.usr_name_label.setGeometry(QtCore.QRect(120, 140, 61, 16))
        self.usr_name_label.setObjectName(_fromUtf8("usr_name_label"))
        self.pwd_label = QtGui.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(125, 183, 61, 20))
        self.pwd_label.setObjectName(_fromUtf8("pwd_label"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Login", None))
        self.login_button.setText(_translate("MainWindow", "Login", None))
        self.notuser_label.setText(_translate("MainWindow", "Not a user?", None))
        self.register_button.setText(_translate("MainWindow", "Register", None))
        self.usr_name_label.setText(_translate("MainWindow", "Username", None))
        self.pwd_label.setText(_translate("MainWindow", "Password", None))

