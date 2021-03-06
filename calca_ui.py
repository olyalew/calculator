# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 499)
        MainWindow.setMinimumSize(QtCore.QSize(403, 499))
        MainWindow.setMaximumSize(QtCore.QSize(403, 499))
        MainWindow.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.top_frame = QtWidgets.QFrame(self.frame)
        self.top_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.top_frame.setObjectName("top_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.top_frame)
        self.gridLayout_2.setContentsMargins(-1, -1, 11, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(176, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.top_frame)
        self.btn_clear.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 255);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 0, 1, 1, 1)
        self.btn_allclear = QtWidgets.QPushButton(self.top_frame)
        self.btn_allclear.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_allclear.setFont(font)
        self.btn_allclear.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 170, 255);")
        self.btn_allclear.setObjectName("btn_allclear")
        self.gridLayout_2.addWidget(self.btn_allclear, 0, 2, 1, 1)
        self.screen = QtWidgets.QLineEdit(self.top_frame)
        self.screen.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.screen.setFont(font)
        self.screen.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.screen.setObjectName("screen")
        self.gridLayout_2.addWidget(self.screen, 1, 0, 1, 3)
        self.gridLayout_3.addWidget(self.top_frame, 0, 0, 1, 1)
        self.bottom_frame = QtWidgets.QFrame(self.frame)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bottom_frame.setObjectName("bottom_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.bottom_frame)
        self.gridLayout.setContentsMargins(-1, -1, -1, 11)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_8 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_8.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_add.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_add.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 0, 3, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_2.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)
        self.btn_multiply = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_multiply.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_multiply.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.gridLayout.addWidget(self.btn_multiply, 2, 3, 1, 1)
        self.btn_decimal = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_decimal.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_decimal.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_decimal.setObjectName("btn_decimal")
        self.gridLayout.addWidget(self.btn_decimal, 3, 1, 1, 1)
        self.btn_equals = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_equals.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_equals.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.btn_equals.setObjectName("btn_equals")
        self.gridLayout.addWidget(self.btn_equals, 3, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_9.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)
        self.btn_divide = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_divide.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_divide.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.btn_divide.setObjectName("btn_divide")
        self.gridLayout.addWidget(self.btn_divide, 3, 3, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_7.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_4.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_5.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_sub.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_sub.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 170, 255);")
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout.addWidget(self.btn_sub, 1, 3, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_3.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_0.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 3, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_6.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.bottom_frame)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_1.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.bottom_frame, 1, 0, 1, 1)
        self.frame.raise_()
        self.bottom_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        MainWindow.setWindowIcon(QtGui.QIcon('calculator.png'))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_allclear.setText(_translate("MainWindow", "AC"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_decimal.setText(_translate("MainWindow", "."))
        self.btn_equals.setText(_translate("MainWindow", "="))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
