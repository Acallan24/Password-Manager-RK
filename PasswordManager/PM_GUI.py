
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PasswordManager import storeCredentials
from PasswordManager import getCredentials



class Ui_MainWindow(object):   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setSizeIncrement(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 170, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 130, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 230, 121, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 180, 121, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 130, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 230, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 300, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 350, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(330, 350, 121, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 290, 771, 20))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 340, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Defining the txt files 1st part
        global websitetxt
        global Usernametxt
        global Passwordtxt
        websitetxt = self.textEdit
        Usernametxt = self.textEdit_2
        Passwordtxt = self.textEdit_3

        #Defining the txt files 1st part
        global getwebsitetxt
        getwebsitetxt = self.textEdit_4

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RKPasswordManager"))
        self.pushButton.setText(_translate("MainWindow", "SetCredentials"))
        self.label.setText(_translate("MainWindow", "Set Credentials"))
        self.label_2.setText(_translate("MainWindow", "Website"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Get Credentials"))
        self.label_6.setText(_translate("MainWindow", "Website"))
        self.pushButton_2.setText(_translate("MainWindow", "GetCredentials"))
        self.pushButton.clicked.connect(clicked) #first button
        self.pushButton_2.clicked.connect(clicked2) #second button


#Button 1
def clicked():
    w = (websitetxt.toPlainText())
    u = (Usernametxt.toPlainText())
    p = (Passwordtxt.toPlainText())
    storeCredentials(w,u,p)
    msg = QMessageBox()
    msg.setText("Credentials Sent")
    msg.exec()
    print("All done")
    websitetxt.clear()
    Usernametxt.clear()
    Passwordtxt.clear() 

#Button 2
def clicked2():
    global get_w
    get_w = (getwebsitetxt.toPlainText())
    a = getCredentials(get_w)
    msg2 = QMessageBox()
    msg2.setText(a)
    msg2.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
