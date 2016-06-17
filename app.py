from PyQt4 import QtGui, QtCore
import sys

import numpy as np
import login
import register
import train_data
import tpr
import time
import cloudpickle as cp
import smtplib
from time import sleep


class LoginLineEdit(QtGui.QLineEdit):
    def __init__(self, usr_line_edit, label, parent=None, outerclass=None):
        super(LoginLineEdit, self).__init__(parent)
        self.outerclass = outerclass
        self.outerclass.start_time = np.empty((0,), dtype=np.float64)
        self.outerclass.end_time = np.empty((0,), dtype=np.float64)
        self.outerclass.timing_vector = np.empty((0,), dtype=np.float64)
        self.user_line_edit = usr_line_edit
        self.label = label

    def keyPressEvent(self, event):
        self.outerclass.start_time = np.append(self.outerclass.start_time, time.time())
        #
        # print self.outerclass.start_time
        # print "Key pressed"
        QtGui.QLineEdit.keyPressEvent(self, event)

    def keyReleaseEvent(self, event):
        self.outerclass.end_time = np.append(self.outerclass.end_time, time.time())
        if event.key() == QtCore.Qt.Key_Return:
            self.outerclass.timing_vector = np.empty((0,), dtype=np.float64)
            i = 0
            # print self.outerclass.end_time.size
            while i < self.outerclass.end_time.size - 1:
                self.outerclass.timing_vector = np.append(self.outerclass.timing_vector, self.outerclass.start_time[i] - self.outerclass.end_time[i])
                self.outerclass.timing_vector = np.append(self.outerclass.timing_vector, self.outerclass.end_time[i+1] - self.outerclass.start_time[i])
                i += 1
            self.outerclass.timing_vector = np.append(self.outerclass.timing_vector, self.outerclass.start_time[i] - self.outerclass.end_time[i])
            print "St", self.outerclass.start_time
            print "Et", self.outerclass.end_time
            print "TV", self.outerclass.timing_vector

            sys.stdout.flush()
            usr_name = self.user_line_edit.displayText()
            usr = None

            with open('./profiles/' + usr_name + '.bin', 'r') as filename:
                usr = cp.load(filename)
            # print usr.tv_list
            # sleep(15)
            curr_timing_vector = self.outerclass.timing_vector
            anomaly_score = usr.detector.anomaly_score(curr_timing_vector)
            print anomaly_score * 1000.0
            if anomaly_score * 1000.0 > 4:
                self.label.setText("Processing...")
                gmail_user = "aayushigupta.noida@gmail.com"
                gmail_pwd = "123456@abcdef"

                TO = "abinashdakshana999@gmail.com"
                SUBJECT = "Unauthorised Access detected"
                TEXT = "We have detected an anomaly in your password input pattern. Please confirm if it's you."
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                BODY = '\r\n'.join(['To: %s' % TO,
                                    'From: %s' % gmail_user,
                                    'Subject: %s' % SUBJECT,
                                    '', TEXT])

                server.sendmail(gmail_user, [TO], BODY)
                print 'email sent'
                while True:
                    pass
            # self.outerclass.tv_list.append(np.array(self.outerclass.timing_vector))
            # self.outerclass.start_time = np.empty((0,), dtype=np.float64)
            # self.outerclass.end_time = np.empty((0,), dtype=np.float64)
            # self.outerclass.timing_vector = np.empty((0,), dtype=np.float64)
            # self.clear()
        # print "Key released"
        QtGui.QLineEdit.keyReleaseEvent(self, event)


class MyLineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None, outerclass=None):
        super(MyLineEdit, self).__init__(parent)
        self.outerclass = outerclass
        self.outerclass.start_time = np.empty((0,), dtype=np.float64)
        self.outerclass.end_time = np.empty((0,), dtype=np.float64)
        self.outerclass.tv_list = []

    def keyPressEvent(self, event):
        self.outerclass.start_time = np.append(self.outerclass.start_time, time.time())
        # print self.outerclass.start_time
        # print "Key pressed"
        QtGui.QLineEdit.keyPressEvent(self, event)

    def keyReleaseEvent(self, event):
        self.outerclass.end_time = np.append(self.outerclass.end_time, time.time())
        if event.key() == QtCore.Qt.Key_Return:
            self.outerclass.timing_vector = np.empty((0,), dtype=np.float64)
            i = 0
            # print self.outerclass.end_time.size
            while i < self.outerclass.end_time.size - 1:
                self.outerclass.timing_vector = np.append(self.outerclass.timing_vector, self.outerclass.start_time[i] - self.outerclass.end_time[i])
                self.outerclass.timing_vector = np.append(self.outerclass.timing_vector, self.outerclass.end_time[i+1] - self.outerclass.start_time[i])
                i += 1
            self.outerclass.timing_vector = np.append(self.outerclass.timing_vector, self.outerclass.start_time[i] - self.outerclass.end_time[i])
            print self.outerclass.start_time
            print self.outerclass.end_time
            print self.outerclass.timing_vector
            self.outerclass.tv_list.append(np.array(self.outerclass.timing_vector))
            self.outerclass.start_time = np.empty((0,), dtype=np.float64)
            self.outerclass.end_time = np.empty((0,), dtype=np.float64)
            self.outerclass.timing_vector = np.empty((0,), dtype=np.float64)
            self.clear()
        # print "Key released"
        QtGui.QLineEdit.keyReleaseEvent(self, event)

class User():
    def __init__(self, name, password, email, tv_list, detector):
        self.name = name
        self.password = password
        self.email = email
        self.tv_list = tv_list
        self.detector = detector

class TrainDataWindow(QtGui.QMainWindow, train_data.Ui_MainWindow):
    def __init__(self, usr_name, pwd, email, parent=None):
        super(TrainDataWindow, self).__init__(parent)
        self.setupUi(self)
        self.pwd_line_edit = MyLineEdit(self.pwd_line_edit, self)
        self.detector = None
        self.training_data = []
        self.usr_name = usr_name
        self.pwd = pwd
        self.email = email
        self.finish_button.clicked.connect(self.handleFinishButton)

    def handleFinishButton(self):
        self.training_data = self.tv_list
        self.detector = tpr.NNMDetector(np.array(self.tv_list))
        print "Yoyoyoyoy"
        self.close()

    def closeEvent(self, event):
        usr = User(self.usr_name, self.pwd, self.email, self.training_data, self.detector)
        with open('./profiles/' + self.usr_name + '.bin', 'w') as filename:
            cp.dump(usr, filename)
        event.accept()



class RegisterWindow(QtGui.QMainWindow, register.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        self.register_button.clicked.connect(self.handleRegisterButton)

    def handleRegisterButton(self):
        if self.usr_line_edit.displayText() == "":
            print "Username can't be empty"
        elif len(self.pwd_line_edit.displayText()) < 8:
            print "Length should be atleast 8"
        elif self.pwd_line_edit.text() != self.re_enter_pwd_line_edit.text():
            print "Please enter the same passwords"
        usr_name = self.usr_line_edit.displayText()
        pwd = self.pwd_line_edit.text()
        print pwd
        email = str(self.re_enter_pwd_line_edit_2.displayText())
        window = TrainDataWindow(usr_name, pwd, email, self)
        window.show()
        self.close()


class LoginScreen(QtGui.QMainWindow, login.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)
        self.register_button.clicked.connect(self.handleRegisterButton)
        # self.login_button.clicked.connect(self.handleLoginButton)
        self.pwd_line_edit = LoginLineEdit(self.usr_line_edit, self.message_label, self.pwd_line_edit, self)
        # self.pwd_line_edit.returnPressed.connect(self.login_button.click)
        # self.login_button.clicked.connect(self.handleLoginButton)
        self.reset_button.clicked.connect(self.reset)

    def reset(self):
        form = LoginScreen()
        form.show()
        self.close()

    def handleRegisterButton(self):
        window = RegisterWindow(self)
        window.show()

    # def handleLoginButton(self):
    #     usr_name = self.usr_line_edit.displayText()
    #     usr = None
    #
    #     with open('./profiles/' + usr_name + '.bin', 'r') as filename:
    #         usr = cp.load(filename)
    #     # print usr.tv_list
    #     # sleep(15)
    #     curr_timing_vector = self.timing_vector
    #     anomaly_score = usr.detector.anomaly_score(curr_timing_vector)
    #     print anomaly_score



def main():
    app = QtGui.QApplication(sys.argv)
    form = LoginScreen()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()