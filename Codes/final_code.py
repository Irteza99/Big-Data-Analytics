from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
class Ui_create(object):
    def showMessage(self,title,message):
        u = self.lineEdit.text()
        e = self.lineEdit_2.text()
        ph = self.lineEdit_3.text()
        p = self.lineEdit_4.text()
        r= self.lineEdit_5.text()
        c = self.comboBox.currentText()
        if(u=="" or e=="" or ph=="" or p=="" or u==""or c==""):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Please fill all the fields!")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
        else:
            if(p!=r):
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Your passwords don't match ,retry!")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec_()
            else:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setWindowTitle(title)
                msgBox.setText(message)
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec_()
            
    def insertData(self):
        self.showMessage('Success','Account created please proceed to login window')
        
            
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        category = self.comboBox.currentText()
        if (username!="" and email !="" and password!="" and phone!="" and category!=""):
            
            connection = sqlite3.connect("login.db")
            connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",(username,email,phone,password,category))
            connection.commit()
            connection.close()
        
    def loginShow(self):
        self.loginWindow = QtWidgets.QDialog()
        self.ui = Ui_main0()
        self.ui.setupUi(self.loginWindow)
        self.loginWindow.show()
    def loginCheck(self):
        print("PLease Enter Details to login")
        self.loginShow()
    def setupUi(self, create):
        create.setObjectName("create")
        create.resize(533, 569)
        create.setStyleSheet("QWidget {\n"
"  background-color: black;\n"
"}")
        create.setSizeGripEnabled(False)
        self.label = QtWidgets.QLabel(create)
        self.label.setGeometry(QtCore.QRect(130, 20, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:white}")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(create)
        self.label_7.setGeometry(QtCore.QRect(30, 250, 261, 301))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("E:/Final/register.png"))
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(create)
        self.comboBox.setGeometry(QtCore.QRect(350, 120, 161, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: black;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(create)
        self.label_8.setGeometry(QtCore.QRect(370, 100, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{color:white}")
        self.label_8.setObjectName("label_8")
        self.splitter = QtWidgets.QSplitter(create)
        self.splitter.setGeometry(QtCore.QRect(10, 100, 141, 151))
        self.splitter.setStyleSheet("QLabel{color:white}")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter)
        self.splitter_3.setStyleSheet("QLabel{color:white}")
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color:white}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color:white}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{color:white}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{color:white}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{color:white}")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(create)
        self.pushButton.setGeometry(QtCore.QRect(210, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insertData)
        self.pushButton_2 = QtWidgets.QPushButton(create)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 330, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.loginCheck)
        self.label_9 = QtWidgets.QLabel(create)
        self.label_9.setGeometry(QtCore.QRect(300, 370, 211, 191))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("E:/Final/kk.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(create)
        self.label_10.setGeometry(QtCore.QRect(370, 330, 121, 31))
        self.label_10.setStyleSheet("QLabel{color:white}")
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(create)
        self.line.setGeometry(QtCore.QRect(320, 90, 3, 171))
        self.line.setStyleSheet("Line{background-color:white}")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(create)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 527, 3))
        self.line_2.setStyleSheet("Line{background-color:white}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(create)
        self.line_3.setGeometry(QtCore.QRect(0, 90, 527, 3))
        self.line_3.setStyleSheet("Line{background-color:white}")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.splitter_2 = QtWidgets.QSplitter(create)
        self.splitter_2.setGeometry(QtCore.QRect(160, 100, 133, 151))
        self.splitter_2.setStyleSheet("QLineEdit{background-color:white}")
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit.setStyleSheet("QLineEdit{background-color:white}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_2.setStyleSheet("QLineEdit{background-color:white}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_3.setStyleSheet("QLineEdit{background-color:white}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_4.setStyleSheet("QLineEdit{background-color:white}")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_5.setStyleSheet("QLineEdit{background-color:white}")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.lineEdit_4.raise_()
        self.label_6.raise_()
        self.lineEdit_5.raise_()
        self.comboBox.raise_()
        self.label_8.raise_()
        self.splitter.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()

        self.retranslateUi(create)
        QtCore.QMetaObject.connectSlotsByName(create)

    def retranslateUi(self, create):
        _translate = QtCore.QCoreApplication.translate
        create.setWindowTitle(_translate("create", "Create_Account"))
        self.label.setText(_translate("create", "Create Account"))
        self.comboBox.setWhatsThis(_translate("create", "Designation selector"))
        self.comboBox.setAccessibleDescription(_translate("create", "Open to chose"))
        self.comboBox.setItemText(0, _translate("create", "Select"))
        self.comboBox.setItemText(1, _translate("create", "Intern"))
        self.comboBox.setItemText(2, _translate("create", "Trainee"))
        self.comboBox.setItemText(3, _translate("create", "Scientist"))
        self.comboBox.setItemText(4, _translate("create", "Technical officer"))
        self.comboBox.setItemText(5, _translate("create", "Security officer"))
        self.comboBox.setItemText(6, _translate("create", "Network analyst"))
        self.comboBox.setItemText(7, _translate("create", "Director"))
        self.comboBox.setItemText(8, _translate("create", "Assistant"))
        self.label_8.setText(_translate("create", "Chose Designation"))
        self.label_2.setText(_translate("create", "Username :"))
        self.label_3.setText(_translate("create", "Email Id :"))
        self.label_4.setText(_translate("create", "Phone number :"))
        self.label_5.setText(_translate("create", "Password :"))
        self.label_6.setText(_translate("create", "Re Enter Password :"))
        self.pushButton.setText(_translate("create", "Create"))
        self.pushButton_2.setText(_translate("create", "Login"))
        self.label_10.setText(_translate("create", "Already registered?"))
        self.lineEdit.setPlaceholderText(_translate("create", "Chose an ID"))
        self.lineEdit_2.setPlaceholderText(_translate("create", "Valid Email address"))
        self.lineEdit_3.setPlaceholderText(_translate("create", "+91"))
        self.lineEdit_4.setPlaceholderText(_translate("create", "At least 5 charachters"))
        self.lineEdit_5.setPlaceholderText(_translate("create", "Confirm password"))
class Ui_device(object):
    def open2(self):
        self.win = QtWidgets.QDialog()
        self.ui = Ui_desktop2()
        self.ui.setupUi(self.win)
        self.win.show()
    
    def open(self):
        self.printer = QtWidgets.QDialog()
        self.ui = Ui_desktop()
        self.ui.setupUi(self.printer)
        self.printer.show()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 466)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setMouseTracking(False)
        Form.setStyleSheet("QWidget{background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))}\n"
"Line{background-color:black}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 461, 61))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 220, 271, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("E:/Final/PrintFaxIconX.png"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 281, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/Final/desktop-computer-keyboard-mouse.png"))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 90, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 3, 451))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 460, 601, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(610, 10, 3, 451))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(0, 0, 621, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(300, 100, 3, 361))
        self.line_6.setStyleSheet("Line{background-color:black}")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open2)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 120, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.open)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 180, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "main1"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">IT INFRASTRUCTURE ,DRDO KANPUR</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "DESKTOPS"))
        self.pushButton_4.setText(_translate("Form", "PRINTERS"))
        self.label_4.setText(_translate("Form", "Which device records   you want to access?"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 510)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Display = QtWidgets.QPushButton(Form)
        self.Display.setGeometry(QtCore.QRect(180, 270, 131, 41))
        self.Display.setObjectName("Display")
        self.Display.clicked.connect(self.Exel)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 91, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 280, 71, 16))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 50, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 330, 291, 171))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("E:/images.png"))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(143, 70, 201, 191))
        self.textEdit.setObjectName("textEdit")
        self.label_4.raise_()
        self.label.raise_()
        self.Display.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.textEdit.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Scientists At DMSRDE"))
        self.Display.setText(_translate("Form", "Display"))
        self.comboBox.setItemText(0, _translate("Form", "Select"))
        self.comboBox.setItemText(1, _translate("Form", "Director"))
        self.comboBox.setItemText(2, _translate("Form", "Scientist G"))
        self.comboBox.setItemText(3, _translate("Form", "Scientist F"))
        self.comboBox.setItemText(4, _translate("Form", "Scientist E"))
        self.comboBox.setItemText(5, _translate("Form", "Scientist D"))
        self.comboBox.setItemText(6, _translate("Form", "Scientist C"))
        self.comboBox.setItemText(7, _translate("Form", "Scientist B"))
        self.comboBox.setItemText(8, _translate("Form", "Scientist A"))
        self.label_2.setText(_translate("Form", "Category"))
        self.label_3.setText(_translate("Form", "Click to view "))

    def Exel(self):
        s = self.comboBox.currentText()

        self.df = pd.read_csv("E:/names.csv")

        if (s == "Director"):
            l = []
            l = 'Dr N Eswara Prasad.'
            self.textEdit.setText(l)
        elif(s=="Scientist G"):

            y="They are\n"+str(self.df.Names[0:5])
            self.textEdit.setText(y)
        elif (s == "Scientist F"):

            y = "They are\n" + str(self.df.Names[5:21])
            self.textEdit.setText(y)
        elif (s == "Scientist E"):

            y = "They are\n" + str(self.df.Names[22:38])
            self.textEdit.setText(y)
        elif (s == "Scientist D"):

            y = "They are\n" + str(self.df.Names[38:61])
            self.textEdit.setText(y)
        elif (s == "Scientist C"):

            y = "They are\n" + str(self.df.Names[61:99])
            self.textEdit.setText(y)
        elif (s == "Scientist B"):

            y = "They are\n" + str(self.df.Names[99:101])
            self.textEdit.setText(y)
        elif (s == "Scientist A"):

            y = "They are\n" + str(self.df.Names[161:206])
            self.textEdit.setText(y)




class Ui_desktop2(object):
    def graph(self):
        url="E:/desk.csv"
        self.df=pd.read_csv(url)
        s = self.comboBox_2.currentText()
        b = self.comboBox_3.currentText()
        if(s=='Make' and b=='Bar' ):
            k=self.df['Make']
            pd.value_counts(k).plot(title="Printers Installed",kind='barh')
            plt.xlabel("NUMBER OF Desktops")
            plt.ylabel("Make")
            plt.show()
        
        if(s=='Processor' and b=='Bar' ):
            k=self.df['Processor']
            pd.value_counts(k).plot(title="Processors ",kind='barh')
            plt.xlabel("NUMBER OF Desktops")
            plt.ylabel("Make")
            plt.show()
        if(s=='RAM' and b=='Bar' ):
            k=self.df['Ram']
            pd.value_counts(k).plot(title="RAM",kind='barh')
            plt.xlabel("NUMBER OF DESKTOPS")
            plt.ylabel("RAM AVAILABLE")
            plt.show()    
        if(s=='Group' and b=='Bar' ):
            k=self.df['Group Name']
            pd.value_counts(k).plot(title="Group Vise Distribution",kind='barh')
            plt.xlabel("NUMBER OF DESKTOPS")
            plt.ylabel("Group")
            plt.show()
        if(s=='Remark' and b=='Bar' ):
            k=self.df['Remarks']
            pd.value_counts(k).plot(title="Corresponding HOD's",kind='barh')
            plt.xlabel("NUMBER OF DESKTOP")
            plt.ylabel("Remark")
            plt.show()
        if(s=='Make' and b=='Pie' ):
            k=self.df['Make']
            pd.value_counts(k).plot.pie(title="DESKTOPS Installed",legend=True)
            plt.show()
        if(s=='Processor' and b=='Pie' ):
            k=self.df['Processor']
            pd.value_counts(k).plot.pie(title="DESKTOPS Installed",legend=True)
            plt.show()
        if(s=='RAM' and b=='Pie' ):
            k=self.df['Ram']
            pd.value_counts(k).plot.pie(title="RAM AVAILABLE",legend=True)
            plt.show()    
        if(s=='Group' and b=='Pie' ):
            k=self.df['Group Name']
            pd.value_counts(k).plot.pie(title="Group Vise Distribution",legend=True)
            plt.show()
        if(s=='Remark' and b=='Pie' ):
            k=self.df['Remarks']
            pd.value_counts(k).plot.pie(title="Corresponding HOD's",legend=True)
            plt.show()
        if(s=='Make' and b=='Line' ):
            k=self.df['Make']
            pd.value_counts(k).plot.line(title="Printers Installed",legend=True)
            plt.show()
        if(s=='RAM' and b=='Line' ):
            k=self.df['Ram']
            pd.value_counts(k).plot.line(title="RAM AVAILABLE",legend=True)
            plt.show()
        if(s=='Processor' and b=='Line' ):
            k=self.df['Processor']
            pd.value_counts(k).plot.line(title="Processor",legend=True)
            plt.show()
        if(s=='Group' and b=='Line' ):
            k=self.df['Group Name']
            pd.value_counts(k).plot.line(title="Group Vise Distribution")
            plt.show()
        if(s=='Remark' and b=='Line' ):
            k=self.df['Remarks']
            pd.value_counts(k).plot.line(title="Corresponding HOD's")
            plt.show()
    def lives(self):
        url="E:/desk.csv"
        self.df=pd.read_csv(url)
        s = self.comboBox.currentText()
        if(s=="LENOVO" or s=="HCL" or s=="Samsung" or s=="Core to duo" ):
##checkboxes are enabled or disabled with toggle            
            self.checkBox_3.toggle()
        elif(s=="ACER" or s=="HP" or s=="DELL"):
            self.checkBox_4.toggle()
        elif(s=="WIPRO" or s=="COMPAQ" or s=="HCL Infinity Pro" or s=="HCL infinity" or s=="Wipro Super Genious" or s=="Dell i7"):
            self.checkBox_2.toggle()    
        elif(s=="ACER" or s=="DELL-90TXFY1" or s=="DELL-5JSXFY1"):
            self.checkBox_4.toggle()
        elif(s=="Dell Xeon" or s=="HCL EC2" or s=="HP Compaq" or s=="HP (Drona)" or s=="Lenovo W/vista"):
            self.checkBox_7.toggle()
        elif(s=="Data Mini" or s=="Zenith" or s=="HP Compaq 8100 Elite" or s=="Frontech passion"):
            self.checkBox_5.toggle()
        elif(s=="IBM" or s=="HP SERVER(MODEL NO. DL.180)" or s=="Lenovo Think vision"):
            self.checkBox.toggle()




            
    def views(self):
        url="E:/desk.csv"
        self.df=pd.read_csv(url)
        s = self.comboBox.currentText()
        m=int(self.lineEdit.text())
        a=m-1
        l=str(self.df.loc[a])
##textEdit only takes string values nothing else type conversion is necessary
         
        self.textEdit.setText(l)
    
    def counts(self):
        print("hi")
        url="E:/desk.csv"
        self.df=pd.read_csv(url)
        
        
##it counts the total values in every column
        x = self.df.count(axis =0,level=None,numeric_only=False)
##y counts the length of inserted df
        y= len(self.df.index)
        self.spinBox.setValue(y)
    def setupUi(self, desktop):
        desktop.setObjectName("desktop")
        desktop.resize(760, 618)
        self.label = QtWidgets.QLabel(desktop)
        self.label.setGeometry(QtCore.QRect(230, 30, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(desktop)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(desktop)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: white }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.counts)
        self.spinBox = QtWidgets.QSpinBox(desktop)
        self.spinBox.setGeometry(QtCore.QRect(310, 100, 81, 31))
        self.spinBox.setReadOnly(True)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_3 = QtWidgets.QPushButton(desktop)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(desktop)
        self.label_3.setGeometry(QtCore.QRect(450, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(desktop)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(desktop)
        self.comboBox.setGeometry(QtCore.QRect(260, 170, 161, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.lives)
        self.pushButton_4 = QtWidgets.QPushButton(desktop)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: white }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.views)
        self.label_5 = QtWidgets.QLabel(desktop)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(desktop)
        self.textEdit.setGeometry(QtCore.QRect(370, 230, 321, 131))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(desktop)
        self.line.setGeometry(QtCore.QRect(0, 370, 901, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(desktop)
        self.label_6.setGeometry(QtCore.QRect(320, 380, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(desktop)
        self.label_7.setGeometry(QtCore.QRect(460, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(desktop)
        self.lineEdit.setGeometry(QtCore.QRect(190, 230, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(desktop)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 450, 161, 31))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(15)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(desktop)
        self.comboBox_3.setGeometry(QtCore.QRect(440, 450, 161, 31))
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(15)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_8 = QtWidgets.QLabel(desktop)
        self.label_8.setGeometry(QtCore.QRect(340, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(desktop)
        self.label_9.setGeometry(QtCore.QRect(10, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(desktop)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 510, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: white }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.graph)
        self.line_2 = QtWidgets.QFrame(desktop)
        self.line_2.setGeometry(QtCore.QRect(-70, 80, 921, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox = QtWidgets.QCheckBox(desktop)
        self.checkBox.setGeometry(QtCore.QRect(510, 180, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_10 = QtWidgets.QLabel(desktop)
        self.label_10.setGeometry(QtCore.QRect(40, 270, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.checkBox_2 = QtWidgets.QCheckBox(desktop)
        self.checkBox_2.setGeometry(QtCore.QRect(570, 180, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(desktop)
        self.checkBox_3.setGeometry(QtCore.QRect(620, 180, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(desktop)
        self.checkBox_4.setGeometry(QtCore.QRect(670, 180, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(desktop)
        self.checkBox_5.setGeometry(QtCore.QRect(510, 200, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(desktop)
        self.checkBox_6.setGeometry(QtCore.QRect(570, 200, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(desktop)
        self.checkBox_7.setGeometry(QtCore.QRect(620, 200, 70, 17))
        self.checkBox_7.setObjectName("checkBox_7")

        self.retranslateUi(desktop)
        QtCore.QMetaObject.connectSlotsByName(desktop)

    def retranslateUi(self, desktop):
        _translate = QtCore.QCoreApplication.translate
        desktop.setWindowTitle(_translate("desktop", "Printers"))
        self.label.setText(_translate("desktop", "Desktops Database Accessed"))
        self.label_2.setText(_translate("desktop", "Number of devices:"))
        self.pushButton_2.setText(_translate("desktop", "View"))
        self.pushButton_3.setText(_translate("desktop", "ADD"))
        self.label_3.setText(_translate("desktop", "Add or append  the data :"))
        self.label_4.setText(_translate("desktop", "Chose the desktop  from make :"))
        self.comboBox.setAccessibleDescription(_translate("desktop", "Open to chose"))
        self.comboBox.setItemText(0, _translate("desktop", "Select"))
        self.comboBox.setItemText(1, _translate("desktop", "LENOVO"))
        self.comboBox.setItemText(2, _translate("desktop", "HCL"))
        self.comboBox.setItemText(3, _translate("desktop", "WIPRO"))
        self.comboBox.setItemText(4, _translate("desktop", "ACER"))
        self.comboBox.setItemText(5, _translate("desktop", "COMPAQ"))
        self.comboBox.setItemText(6, _translate("desktop", "HP"))
        self.comboBox.setItemText(7, _translate("desktop", "DELL"))
        self.comboBox.setItemText(8, _translate("desktop", "DELL-90TXFY1"))
        self.comboBox.setItemText(9, _translate("desktop", "DELL-5JSXFY1"))
        self.comboBox.setItemText(10, _translate("desktop", "Core to duo"))
        self.comboBox.setItemText(11, _translate("desktop", "Samsung"))
        self.comboBox.setItemText(12, _translate("desktop", "WIPRO ACER"))
        self.comboBox.setItemText(13, _translate("desktop", "Dell Xeon"))
        self.comboBox.setItemText(14, _translate("desktop", "HCL EC2"))
        self.comboBox.setItemText(15, _translate("desktop", "HP Compaq"))
        self.comboBox.setItemText(16, _translate("desktop", "Wipro Super Genious"))
        self.comboBox.setItemText(17, _translate("desktop", "HCL Infinity "))
        self.comboBox.setItemText(18, _translate("desktop", "HCL Infinity Pro"))
        self.comboBox.setItemText(19, _translate("desktop", "Data Mini"))
        self.comboBox.setItemText(20, _translate("desktop", "Dell i7"))
        self.comboBox.setItemText(21, _translate("desktop", "IBM"))
        self.comboBox.setItemText(22, _translate("desktop", "Zenith"))
        self.comboBox.setItemText(23, _translate("desktop", "HP Compaq 8100 Elite"))
        self.comboBox.setItemText(24, _translate("desktop", "HP (Drona)"))
        self.comboBox.setItemText(25, _translate("desktop", "Lenovo W/vista"))
        self.comboBox.setItemText(26, _translate("desktop", "HP SERVER(MODEL NO. DL.180)"))
        self.comboBox.setItemText(27, _translate("desktop", "Lenovo Think vision"))
        self.comboBox.setItemText(28, _translate("desktop", "Frontech passion"))
        self.pushButton_4.setText(_translate("desktop", "View"))
        self.label_5.setText(_translate("desktop", "Enter Serial number:"))
        self.label_6.setText(_translate("desktop", "Graph plotting:"))
        self.label_7.setText(_translate("desktop", "RAM"))
        self.comboBox_2.setAccessibleDescription(_translate("desktop", "Open to chose"))
        self.comboBox_2.setItemText(0, _translate("desktop", "Select"))
        self.comboBox_2.setItemText(1, _translate("desktop", "Make"))
        self.comboBox_2.setItemText(2, _translate("desktop", "Processor"))
        self.comboBox_2.setItemText(3, _translate("desktop", "Group"))
        self.comboBox_2.setItemText(4, _translate("desktop", "Remark"))
        self.comboBox_2.setItemText(5, _translate("desktop", "RAM"))
        self.comboBox_3.setAccessibleDescription(_translate("desktop", "Open to chose"))
        self.comboBox_3.setItemText(0, _translate("desktop", "Line"))
        self.comboBox_3.setItemText(1, _translate("desktop", "Bar"))
        self.comboBox_3.setItemText(2, _translate("desktop", "Pie"))
        self.comboBox_3.setItemText(3, _translate("desktop", "Scatter"))
        self.label_8.setText(_translate("desktop", "Chart Type:"))
        self.label_9.setText(_translate("desktop", "Chose entity:"))
        self.pushButton_5.setText(_translate("desktop", "Plot View"))
        self.checkBox.setText(_translate("desktop", "512 MB"))
        self.label_10.setText(_translate("desktop", "Click to view data :"))
        self.checkBox_2.setText(_translate("desktop", "1 GB"))
        self.checkBox_3.setText(_translate("desktop", "2 GB"))
        self.checkBox_4.setText(_translate("desktop", "4 GB"))
        self.checkBox_5.setText(_translate("desktop", "256 MB"))
        self.checkBox_6.setText(_translate("desktop", "DDR3"))
        self.checkBox_7.setText(_translate("desktop", "1526 MB"))



class Ui_main0(object):
##Message box is an attribute of QtWidgets not QtGui after the latest update thats why its different on the internet    
    def showMessageBox(self,title,message):
        
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def loginCheck(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        connection = sqlite3.connect("login.db")
        result= connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if (username=="" and password ==""):
            
        
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.setText("Please enter relevant details")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
    
            
##The concept behind login check is the query above ^ ,itself acts as an if statement it selects all and fetches only those username and password that are alike
##to our line edit inserted texts and this result is stored in form of rows now if there will be no match then there will exist no row and also
##if there will be irteza named ten times then it will simply have multiple rows
##so in next step we simply count the number of rows i its 0 it means no match more than 0 means user exists doesnt matter how many times he exists
        if(len(result.fetchall())> 0 and username!="" and password!=""):
            print("User Found")
            self.deviceWindow = QtWidgets.QWidget()
            self.ui = Ui_device()
            self.ui.setupUi(self.deviceWindow)
            self.deviceWindow.show()
        else:
            self.showMessageBox('Warning','Invalid Username And Password')
            print("user not found")
    def signUpShow(self):
        print("Welcome To Account Creation Panel\n")
        print("Please fill all the details")
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = Ui_create()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
    def signUpCheck(self):
        print("Hi New User ")
        self.signUpShow()
    def setupUi(self, main0):
        main0.setObjectName("main0")
        main0.resize(392, 518)
        self.label = QtWidgets.QLabel(main0)
        self.label.setGeometry(QtCore.QRect(90, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(main0)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(26)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color:darkblue}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(main0)
        self.lineEdit.setGeometry(QtCore.QRect(90, 160, 211, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
"QLineEdit {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: blue;\n"
"}")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(main0)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(main0)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: blue;\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(main0)
        self.pushButton.setGeometry(QtCore.QRect(90, 280, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{ background-color:rgb(84, 190, 255) }\n"
"QPushButton:pressed{background-color: rgb(200,200, 200);border:2px solid darkblue; }\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid red;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginCheck)
        self.pushButton_2 = QtWidgets.QPushButton(main0)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 280, 91, 21))
        self.pushButton_2.clicked.connect(self.signUpCheck)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{ background-color:rgb(84, 190, 255) }\n"
"QPushButton:pressed{background-color: rgb(200,200, 200);border:2px solid darkblue; }\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 2px solid red;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(main0)
        self.label_5.setGeometry(QtCore.QRect(250, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(main0)
        self.label_6.setGeometry(QtCore.QRect(200, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.label_6.setStyleSheet("QLabel{color:darkblue}")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(main0)
        self.label_4.setGeometry(QtCore.QRect(200, 50, 111, 101))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("E:/Final/12022018edu3a_T.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(main0)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(main0)
        self.label_8.setGeometry(QtCore.QRect(50, 180, 281, 281))
        self.label_8.setStyleSheet("QLabel{rgb(222, 226, 255)}")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("E:Final/rogelio-munoz.png"))
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(main0)
        self.line.setGeometry(QtCore.QRect(20, 470, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(main0)
        self.line_2.setGeometry(QtCore.QRect(13, 30, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(main0)
        self.line_3.setGeometry(QtCore.QRect(20, 20, 351, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(main0)
        self.line_4.setGeometry(QtCore.QRect(360, 30, 20, 451))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.buttonBox = QtWidgets.QDialogButtonBox(main0)
        self.buttonBox.setGeometry(QtCore.QRect(210, 490, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.buttonBox.raise_()

        self.retranslateUi(main0)
        QtCore.QMetaObject.connectSlotsByName(main0)
    
    
    def retranslateUi(self, main0):
        _translate = QtCore.QCoreApplication.translate
        main0.setWindowTitle(_translate("main0", "login_window"))
        self.label.setText(_translate("main0", "Username :"))
        self.label_2.setText(_translate("main0", "LOGIN"))
        self.lineEdit.setWhatsThis(_translate("main0", "Registered Id"))
        self.lineEdit.setPlaceholderText(_translate("main0", "Registered Id?"))
        self.label_3.setText(_translate("main0", "Password :"))
        self.lineEdit_2.setPlaceholderText(_translate("main0", "*********"))
        self.pushButton.setText(_translate("main0", "Sign In"))
        self.pushButton_2.setText(_translate("main0", "Register"))
        self.label_5.setText(_translate("main0", "New User?"))
        self.label_6.setText(_translate("main0", "Forgot Password?"))

class Ui_Dialog(object):
    def logged(self):
        self.login = QtWidgets.QDialog()
        self.ui = Ui_main0()
        self.ui.setupUi(self.login)
        self.login.show()
    def log(self):
        print("PLease Enter Details to login")
        self.logged()
    def emp(self):
        self.object = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.object)
        self.object.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Welcome")
        Dialog.resize(624, 491)
        Dialog.setStyleSheet("QWidget{background-color:rgb(85, 0, 127)}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 341, 111))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:white}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 300, 291, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/Final/images.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 120, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color:white}")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.log)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 210, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{color:white}")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.emp)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome to Database of DRDO"))
        self.label_3.setText(_translate("Dialog", "IT Infrastructure is only for authorized personnel please login"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Guests can view Employee database"))
        self.pushButton_2.setText(_translate("Dialog", "Employees"))

        
class Ui_desktop(object):
    def graph(self):
        url="E:/printer.csv"
        self.df=pd.read_csv(url)
        s = self.comboBox_2.currentText()
        b = self.comboBox_3.currentText()
        if(s=='Make' and b=='Bar' ):
            k=self.df['Make']
            pd.value_counts(k).plot(title="Printers Installed",kind='barh')
            plt.xlabel("NUMBER OF PRINTERS")
            plt.ylabel("Make")
            plt.show()
        if(s=='Type' and b=='Bar' ):
            k=self.df['Type']
            pd.value_counts(k).plot(title="B&W vs Colored Printers installed",kind='barh')
            plt.xlabel("NUMBER OF PRINTERS")
            plt.ylabel("Type")
            plt.show()    
        if(s=='Group' and b=='Bar' ):
            k=self.df['Group Name']
            pd.value_counts(k).plot(title="Group Vise Distribution",kind='bar')
            plt.xlabel("NUMBER OF PRINTER")
            plt.ylabel("Group")
            plt.show()
        if(s=='Remark' and b=='Bar' ):
            k=self.df['Remark']
            pd.value_counts(k).plot(title="Corresponding HOD's",kind='area')
            plt.xlabel("NUMBER OF PRINTER")
            plt.ylabel("Remark")
            plt.show()
        if(s=='Make' and b=='Pie' ):
            k=self.df['Make']
            pd.value_counts(k).plot.pie(title="Printers Installed",legend=True)
            plt.show()
        if(s=='Type' and b=='Pie' ):
            k=self.df['Type']
            pd.value_counts(k).plot.pie(title="B&W vs Colored Printers installed",legend=True)
            plt.show()    
        if(s=='Group' and b=='Pie' ):
            k=self.df['Group Name']
            pd.value_counts(k).plot.pie(title="Group Vise Distribution",legend=True)
            plt.show()
        if(s=='Remark' and b=='Pie' ):
            k=self.df['Remark']
            pd.value_counts(k).plot.pie(title="Corresponding HOD's",legend=True)
            plt.show()
        if(s=='Make' and b=='Line' ):
            k=self.df['Make']
            pd.value_counts(k).plot.line(title="Printers Installed",legend=True)
            plt.show()
        if(s=='Type' and b=='Line' ):
            k=self.df['Type']
            pd.value_counts(k).plot.line(title="B&W vs Colored Printers installed",legend=True)
            plt.show()    
        if(s=='Group' and b=='Line' ):
            k=self.df['Group Name']
            pd.value_counts(k).plot.line(title="Group Vise Distribution")
            plt.show()
        if(s=='Remark' and b=='Line' ):
            k=self.df['Remark']
            pd.value_counts(k).plot.line(title="Corresponding HOD's")
            plt.show()
    def live(self):
        url="E:/printer.csv"
        self.df=pd.read_csv(url)
        s = self.comboBox.currentText()
        if(s=="HP Laser Jet"):
##checkboxes are enabled or disabled with toggle            
            self.checkBox.toggle()
        else:
            self.checkBox_2.toggle()
        
        
    def view(self):
        url="E:/printer.csv"
        self.df=pd.read_csv(url)
        s = self.comboBox.currentText()
        m=int(self.lineEdit.text())
        a=m-1
        l=str(self.df.loc[a])
##textEdit only takes string values nothing else type conversion is necessary
         
        self.textEdit.setText(l)
    
    def count(self):
        print("hi")
        url="E:/printer.csv"
        self.df=pd.read_csv(url)
##it counts the total values in every column
        x = self.df.count(axis =0,level=None,numeric_only=False)
##y counts the length of inserted df
        y= len(self.df.index)
        self.spinBox.setValue(y)
    def setupUi(self, desktop):
        desktop.setObjectName("desktop")
        desktop.resize(760, 618)
        self.label = QtWidgets.QLabel(desktop)
        self.label.setGeometry(QtCore.QRect(230, 30, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(desktop)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(desktop)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: white }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.count)
        self.spinBox = QtWidgets.QSpinBox(desktop)
        self.spinBox.setGeometry(QtCore.QRect(310, 100, 81, 31))
        self.spinBox.setReadOnly(True)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName("spinBox")
        self.pushButton_3 = QtWidgets.QPushButton(desktop)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"QPushButton:hover { color: white }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(desktop)
        self.label_3.setGeometry(QtCore.QRect(450, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(desktop)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(desktop)
        self.comboBox.setGeometry(QtCore.QRect(260, 170, 161, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(18, "")
        self.comboBox.currentIndexChanged.connect(self.live)
        self.pushButton_4 = QtWidgets.QPushButton(desktop)
        
        self.pushButton_4.setGeometry(QtCore.QRect(200, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: white }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.view)
        self.label_5 = QtWidgets.QLabel(desktop)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(desktop)
        self.textEdit.setGeometry(QtCore.QRect(370, 230, 321, 131))
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(desktop)
        self.line.setGeometry(QtCore.QRect(0, 370, 901, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(desktop)
        self.label_6.setGeometry(QtCore.QRect(320, 380, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(desktop)
        self.label_7.setGeometry(QtCore.QRect(460, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(desktop)
        self.lineEdit.setGeometry(QtCore.QRect(190, 230, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(desktop)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 450, 161, 31))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(15)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(desktop)
        self.comboBox_3.setGeometry(QtCore.QRect(440, 450, 161, 31))
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.comboBox_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: lightblue;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: white;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color:white;\n"
"    border:1px solid white;\n"
"    selection-background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(15)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        
        self.label_8 = QtWidgets.QLabel(desktop)
        self.label_8.setGeometry(QtCore.QRect(340, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(desktop)
        self.label_9.setGeometry(QtCore.QRect(10, 450, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(desktop)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 510, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.429599, y1:0.648, x2:0.440678, y2:0, stop:0 rgba(126, 126, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"\n"
"QPushButton:hover { color: white }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.graph)
        self.line_2 = QtWidgets.QFrame(desktop)
        self.line_2.setGeometry(QtCore.QRect(-70, 80, 921, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox = QtWidgets.QCheckBox(desktop)
        self.checkBox.setGeometry(QtCore.QRect(510, 180, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(desktop)
        self.checkBox_2.setGeometry(QtCore.QRect(560, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_10 = QtWidgets.QLabel(desktop)
        self.label_10.setGeometry(QtCore.QRect(40, 270, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(desktop)
        QtCore.QMetaObject.connectSlotsByName(desktop)

    def retranslateUi(self, desktop):
        _translate = QtCore.QCoreApplication.translate
        desktop.setWindowTitle(_translate("desktop", "Printers"))
        self.label.setText(_translate("desktop", "Printers Database Accessed"))
        self.label_2.setText(_translate("desktop", "Number of devices:"))
        self.pushButton_2.setText(_translate("desktop", "View"))
        self.pushButton_3.setText(_translate("desktop", "ADD"))
        self.label_3.setText(_translate("desktop", "Add or append  the data :"))
        self.label_4.setText(_translate("desktop", "Chose the printer from make :"))
        self.comboBox.setAccessibleDescription(_translate("desktop", "Open to chose"))
        self.comboBox.setItemText(0, _translate("desktop", "Select"))
        self.comboBox.setItemText(1, _translate("desktop", "HP-1007"))
        self.comboBox.setItemText(2, _translate("desktop", "HP-1505"))
        self.comboBox.setItemText(3, _translate("desktop", "HP-1022"))
        self.comboBox.setItemText(4, _translate("desktop", "HP Laser jet"))
        self.comboBox.setItemText(5, _translate("desktop", "Laser jet cp 1025"))
        self.comboBox.setItemText(6, _translate("desktop", "Samsung Scx-4300"))
        self.comboBox.setItemText(7, _translate("desktop", "HP Laser 1020"))
        self.comboBox.setItemText(8, _translate("desktop", "HP Laser jet P1505"))
        self.comboBox.setItemText(9, _translate("desktop", "HP Laser jet P 1007"))
        self.comboBox.setItemText(10, _translate("desktop", "Laser jet "))
        self.comboBox.setItemText(11, _translate("desktop", "DMP"))
        self.comboBox.setItemText(12, _translate("desktop", "HP"))
        self.comboBox.setItemText(13, _translate("desktop", "Canon"))
        self.comboBox.setItemText(14, _translate("desktop", "Xerox"))
        self.comboBox.setItemText(15, _translate("desktop", "Samsung"))
        self.comboBox.setItemText(16, _translate("desktop", "LUXER Dot matrix"))
        self.comboBox.setItemText(17, _translate("desktop", "HP psc1315"))
        self.pushButton_4.setText(_translate("desktop", "View"))
        self.label_5.setText(_translate("desktop", "Enter Serial number:"))
        self.label_6.setText(_translate("desktop", "Graph plotting:"))
        self.label_7.setText(_translate("desktop", "Type:"))
        self.comboBox_2.setAccessibleDescription(_translate("desktop", "Open to chose"))
        self.comboBox_2.setItemText(0, _translate("desktop", "Select"))
        self.comboBox_2.setItemText(1, _translate("desktop", "Make"))
        self.comboBox_2.setItemText(2, _translate("desktop", "Type"))
        self.comboBox_2.setItemText(3, _translate("desktop", "Group"))
        self.comboBox_2.setItemText(4, _translate("desktop", "Remark"))
        self.comboBox_3.setAccessibleDescription(_translate("desktop", "Open to chose"))
        self.comboBox_3.setItemText(0, _translate("desktop", "Select"))
        self.comboBox_3.setItemText(1, _translate("desktop", "Bar"))
        self.comboBox_3.setItemText(2, _translate("desktop", "Pie"))
        self.comboBox_3.setItemText(3, _translate("desktop", "Scatter"))
        self.label_8.setText(_translate("desktop", "Chart Type:"))
        self.label_9.setText(_translate("desktop", "Chose entity:"))
        self.pushButton_5.setText(_translate("desktop", "Plot View"))
        self.checkBox.setText(_translate("desktop", "Color"))
        self.checkBox_2.setText(_translate("desktop", "Black n White"))
        self.label_10.setText(_translate("desktop", "Click to view data :"))




##this will be executed first it should be main page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_device()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main0 = QtWidgets.QDialog()
    msgBox=QtWidgets.QMessageBox()
    ui = Ui_main0()
    ui.setupUi(main0)
    main0.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create = QtWidgets.QDialog()
    ui = Ui_create()
    ui.setupUi(create)
    create.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QDialog()
    ui = Ui_desktop2()
    ui.setupUi(desktop)
    desktop.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QDialog()
    ui = Ui_desktop()
    ui.setupUi(desktop)
    desktop.show()
    sys.exit(app.exec_())
##whichever of these will be at top will be executed first
