
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
class Ui_desktop(object):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QDialog()
    ui = Ui_desktop()
    ui.setupUi(desktop)
    desktop.show()
    sys.exit(app.exec_())

