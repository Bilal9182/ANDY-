# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'andygui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ANDY(object):
    def setupUi(self, ANDY):
        ANDY.setObjectName("ANDY")
        ANDY.resize(661, 531)
        self.centralwidget = QtWidgets.QWidget(ANDY)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 2, 671, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/sndy12.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 480, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 480, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 30, 256, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;""color:white;\n")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(320, 30, 256, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;""color:white;\n")
        self.textBrowser_2.setObjectName("textBrowser_2")
        ANDY.setCentralWidget(self.centralwidget)

        self.retranslateUi(ANDY)
        QtCore.QMetaObject.connectSlotsByName(ANDY)

    def retranslateUi(self, ANDY):
        _translate = QtCore.QCoreApplication.translate
        ANDY.setWindowTitle(_translate("ANDY", "MainWindow"))
        self.pushButton.setText(_translate("ANDY", "RUN"))
        self.pushButton_2.setText(_translate("ANDY", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ANDY = QtWidgets.QMainWindow()
    ui = Ui_ANDY()
    ui.setupUi(ANDY)
    ANDY.show()
    sys.exit(app.exec_())
