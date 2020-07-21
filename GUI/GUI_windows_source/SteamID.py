# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SteamId.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 250)
        Dialog.setMinimumSize(QtCore.QSize(650, 250))
        Dialog.setMaximumSize(QtCore.QSize(650, 250))
        Dialog.setStyleSheet("background-color: rgb(127, 127, 127)")
        self.steam_logo = QtWidgets.QLabel(Dialog)
        self.steam_logo.setGeometry(QtCore.QRect(260, 50, 71, 61))
        self.steam_logo.setStyleSheet("background-color: none;\n"
"image: url(:/background/steam.png);\n"
"")
        self.steam_logo.setText("")
        self.steam_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo.setObjectName("steam_logo")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 687, 264))
        self.frame.setMinimumSize(QtCore.QSize(687, 264))
        self.frame.setMaximumSize(QtCore.QSize(10, 250))
        self.frame.setStyleSheet("background-image: url(:/background/choose_file.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(620, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 10);\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    color: rgb(199, 199, 199);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    color: rgb(255, 60, 63)\n"
"    }")
        self.ExitButton.setObjectName("ExitButton")
        self.RollUpButton = QtWidgets.QPushButton(Dialog)
        self.RollUpButton.setGeometry(QtCore.QRect(600, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.RollUpButton.setFont(font)
        self.RollUpButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 10);\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    color: rgb(199, 199, 199);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    color: #5abe41\n"
"    }")
        self.RollUpButton.setObjectName("RollUpButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 70, 321, 51))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 140, 571, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.LocalizeButton = QtWidgets.QPushButton(Dialog)
        self.LocalizeButton.setGeometry(QtCore.QRect(50, 190, 191, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.LocalizeButton.setFont(font)
        self.LocalizeButton.setStyleSheet("QPushButton{\n"
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
        self.LocalizeButton.setObjectName("LocalizeButton")
        self.frame.raise_()
        self.steam_logo.raise_()
        self.ExitButton.raise_()
        self.RollUpButton.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.LocalizeButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.label_2.setText(_translate("Dialog", "SteamWorkshop ID"))
        self.LocalizeButton.setText(_translate("Dialog", "Подтвердить"))
from GUI import background
