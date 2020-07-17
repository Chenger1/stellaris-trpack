# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STMTT.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QtCore.QSize(840, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 800))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: #1f2533;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 690, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: #5abe41;\n"
"    border: 3px solid #5abe41;\n"
"    border-radius: 20px;\n"
"    color: #1f2533;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #438e30;\n"
"    border: #438e30;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 280, 451, 21))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: #1f2533;\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(730, 280, 451, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background-color: #1f2533;\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(740, 240, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(950, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 330, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    background-color: #1f2533;\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"    }\n"
"QQLabel:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 370, 491, 91))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    background-color: #1f2533;\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 330, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    background-color: #1f2533;\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"    }\n"
"QQLabel:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(700, 370, 501, 91))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    background-color: #1f2533;\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 490, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"    background-color: #1f2533;\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"    }\n"
"QQLabel:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(410, 530, 451, 91))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    background-color: #1f2533;\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #38393d;\n"
"    }")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(930, 560, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 560, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 50, 651, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("pictures/stmtt.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 180, 41, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("pictures/steam.png"))
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1050, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1020, 60, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 60, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background-color: #1f2533;\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #38393d;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #c2c2c2;\n"
"    border: #c2c2c2;\n"
"    color: #1f2533;\n"
"    }")
        self.pushButton_12.setObjectName("pushButton_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stellaris True Machine Translation Tool"))
        self.pushButton_2.setText(_translate("MainWindow", "Локализировать модификацию"))
        self.pushButton_3.setText(_translate("MainWindow", "STEAM LIBRARY PATH"))
        self.pushButton_4.setText(_translate("MainWindow", "STEAM WORKSHOP ID"))
        self.pushButton_5.setText(_translate("MainWindow", "CHOOSE FILE MANUALLY"))
        self.label_2.setText(_translate("MainWindow", "Оригинальная строка"))
        self.label_3.setText(_translate("MainWindow", "Машинный перевод"))
        self.label_4.setText(_translate("MainWindow", "Можно заменить машинный перевод на свой вариант"))
        self.pushButton_6.setText(_translate("MainWindow", "Следующая строка"))
        self.pushButton_7.setText(_translate("MainWindow", "Предыдущая строка"))
        self.pushButton_8.setText(_translate("MainWindow", "Язык утилиты: RUS"))
        self.pushButton_9.setText(_translate("MainWindow", "Перевод на: RUS"))
        self.pushButton_11.setText(_translate("MainWindow", "Справка"))
        self.pushButton_12.setText(_translate("MainWindow", "Дополнительные функции"))
