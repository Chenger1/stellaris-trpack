# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuccessMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from GUI.pictures import resources

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 250)
        Dialog.setMinimumSize(QtCore.QSize(650, 250))
        Dialog.setMaximumSize(QtCore.QSize(650, 250))
        Dialog.setStyleSheet("background-color: transparent;")
        self.AcceptButton = QtWidgets.QPushButton(Dialog)
        self.AcceptButton.setGeometry(QtCore.QRect(250, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.AcceptButton.setFont(font)
        self.AcceptButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    }")
        self.AcceptButton.setObjectName("AcceptButton")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 687, 264))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 264))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 250))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/SuccessMessage.png);")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
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
        self.ExitButton.setText("X")
        self.ExitButton.setObjectName("ExitButton")
        self.SuccessLabel = QtWidgets.QLabel(Dialog)
        self.SuccessLabel.setGeometry(QtCore.QRect(20, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.SuccessLabel.setFont(font)
        self.SuccessLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.SuccessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SuccessLabel.setObjectName("SuccessLabel")
        self.WindowMoveButton = QtWidgets.QPushButton(Dialog)
        self.WindowMoveButton.setGeometry(QtCore.QRect(0, 0, 651, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.WindowMoveButton.setFont(font)
        self.WindowMoveButton.setStyleSheet("QPushButton{\n"
"    color: transparent;\n"
"}")
        self.WindowMoveButton.setText("")
        self.WindowMoveButton.setObjectName("WindowMoveButton")
        self.InfoLabel = QtWidgets.QLabel(Dialog)
        self.InfoLabel.setGeometry(QtCore.QRect(30, 70, 591, 91))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel.setText("Информация")
        self.InfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel.setObjectName("InfoLabel")
        self.StringsList = QtWidgets.QLabel(Dialog)
        self.StringsList.setGeometry(QtCore.QRect(230, 110, 271, 20))
        self.StringsList.setObjectName("StringsList")
        self.StringsList.raise_()
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.AcceptButton.raise_()
        self.ExitButton.raise_()
        self.SuccessLabel.raise_()
        self.InfoLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Успех"))
        self.AcceptButton.setText(_translate("Dialog", "Отлично"))
        self.SuccessLabel.setText(_translate("Dialog", "Успех"))
        self.StringsList.setText(_translate("Dialog", "Файл перевода успешно записан.Файл сохранен.Мод успешно добавлен в коллекцию.Моды успешно отсортированы.Язык интерфейса был изменен\n"
"\n"
"Перезапустите утилиту, чтобы увидеть изменения.Неверный ключ [Для разработчиков]"))
