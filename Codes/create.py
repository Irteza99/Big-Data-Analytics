# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_create(object):
    def insertData(self):
        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        category = self.comboBox.currentText()

        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?,?,?)",(username,email,phone,password,category))
        connection.commit()
        connection.close()
   
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create = QtWidgets.QDialog()
    ui = Ui_create()
    ui.setupUi(create)
    create.show()
    sys.exit(app.exec_())

