# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseFile.ui'
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
        Dialog.setStyleSheet("background-color: transparent;")
        self.ManualButton = QtWidgets.QPushButton(Dialog)
        self.ManualButton.setGeometry(QtCore.QRect(30, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ManualButton.setFont(font)
        self.ManualButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 20px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    }")
        self.ManualButton.setObjectName("ManualButton")
        self.SteamButton = QtWidgets.QPushButton(Dialog)
        self.SteamButton.setGeometry(QtCore.QRect(360, 190, 261, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SteamButton.setFont(font)
        self.SteamButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 20px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    }")
        self.SteamButton.setObjectName("SteamButton")
        self.steam_logo = QtWidgets.QLabel(Dialog)
        self.steam_logo.setGeometry(QtCore.QRect(560, 180, 71, 61))
        self.steam_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/steam.png);\n"
"")
        self.steam_logo.setText("")
        self.steam_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo.setObjectName("steam_logo")
        self.file_explorer_logo = QtWidgets.QLabel(Dialog)
        self.file_explorer_logo.setGeometry(QtCore.QRect(130, 180, 61, 61))
        self.file_explorer_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/explorer.png);")
        self.file_explorer_logo.setText("")
        self.file_explorer_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.file_explorer_logo.setObjectName("file_explorer_logo")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 687, 264))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 264))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 250))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/ChooseFile.png);")
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
        self.ChooseFileLabel = QtWidgets.QLabel(Dialog)
        self.ChooseFileLabel.setGeometry(QtCore.QRect(200, 70, 441, 51))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.ChooseFileLabel.setFont(font)
        self.ChooseFileLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ChooseFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChooseFileLabel.setObjectName("ChooseFileLabel")
        self.ReferenceButton = QtWidgets.QPushButton(Dialog)
        self.ReferenceButton.setGeometry(QtCore.QRect(10, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ReferenceButton.setFont(font)
        self.ReferenceButton.setStyleSheet("QPushButton{\n"
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
        self.ReferenceButton.setObjectName("ReferenceButton")
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
        self.WindowMoveButton.setObjectName("WindowMoveButton")
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.ManualButton.raise_()
        self.SteamButton.raise_()
        self.steam_logo.raise_()
        self.file_explorer_logo.raise_()
        self.ExitButton.raise_()
        self.RollUpButton.raise_()
        self.ChooseFileLabel.raise_()
        self.ReferenceButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ManualButton.setText(_translate("Dialog", "Вручную    "))
        self.SteamButton.setText(_translate("Dialog", "SteamWorkshop ID    "))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.ChooseFileLabel.setText(_translate("Dialog", "Выбрать файл"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
from GUI.pictures import resources
