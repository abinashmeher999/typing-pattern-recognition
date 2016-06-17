# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_data.ui'
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
        MainWindow.resize(554, 470)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pwd_label = QtGui.QLabel(self.centralwidget)
        self.pwd_label.setGeometry(QtCore.QRect(130, 140, 61, 16))
        self.pwd_label.setObjectName(_fromUtf8("pwd_label"))
        self.pwd_line_edit = QtGui.QLineEdit(self.centralwidget)
        self.pwd_line_edit.setGeometry(QtCore.QRect(200, 140, 181, 21))
        self.pwd_line_edit.setText(_fromUtf8(""))
        self.pwd_line_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd_line_edit.setObjectName(_fromUtf8("pwd_line_edit"))
        self.finish_button = QtGui.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(290, 200, 110, 32))
        self.finish_button.setObjectName(_fromUtf8("finish_button"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Train Data", None))
        self.pwd_label.setText(_translate("MainWindow", "Password", None))
        self.finish_button.setText(_translate("MainWindow", "Finish", None))

