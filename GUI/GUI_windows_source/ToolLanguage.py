# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolLanguage.ui'
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
        self.lang_logo = QtWidgets.QLabel(Dialog)
        self.lang_logo.setGeometry(QtCore.QRect(10, 30, 61, 51))
        self.lang_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/lang.png);\n"
"")
        self.lang_logo.setText("")
        self.lang_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lang_logo.setObjectName("lang_logo")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 687, 264))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 264))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 250))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/ToolLanguage.png);")
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
        self.ToolLanguageLabel = QtWidgets.QLabel(Dialog)
        self.ToolLanguageLabel.setGeometry(QtCore.QRect(20, 90, 271, 61))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.ToolLanguageLabel.setFont(font)
        self.ToolLanguageLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ToolLanguageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ToolLanguageLabel.setObjectName("ToolLanguageLabel")
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
        self.RussianButton = QtWidgets.QPushButton(Dialog)
        self.RussianButton.setGeometry(QtCore.QRect(470, 60, 131, 26))
        self.RussianButton.setMinimumSize(QtCore.QSize(0, 26))
        self.RussianButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.RussianButton.setFont(font)
        self.RussianButton.setStyleSheet("    QPushButton{\n"
"        background-color: rgba(31, 37, 51, 50);\n"
"        border: 2px solid #ffffff;\n"
"        border-radius: 13px;\n"
"        min-height: 22px;\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton:hover{\n"
"        background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"    QPushButton:pressed{\n"
"        background-color: rgba(194, 194, 194, 50);\n"
"        border: #c2c2c2;\n"
"    }")
        self.RussianButton.setObjectName("RussianButton")
        self.UkrainianButton = QtWidgets.QPushButton(Dialog)
        self.UkrainianButton.setGeometry(QtCore.QRect(310, 120, 131, 26))
        self.UkrainianButton.setMinimumSize(QtCore.QSize(0, 26))
        self.UkrainianButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.UkrainianButton.setFont(font)
        self.UkrainianButton.setStyleSheet("    QPushButton{\n"
"        background-color: rgba(31, 37, 51, 50);\n"
"        border: 2px solid #ffffff;\n"
"        border-radius: 13px;\n"
"        min-height: 22px;\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton:hover{\n"
"        background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"    QPushButton:pressed{\n"
"        background-color: rgba(194, 194, 194, 50);\n"
"        border: #c2c2c2;\n"
"    }")
        self.UkrainianButton.setObjectName("UkrainianButton")
        self.PolishButton = QtWidgets.QPushButton(Dialog)
        self.PolishButton.setGeometry(QtCore.QRect(470, 120, 131, 26))
        self.PolishButton.setMinimumSize(QtCore.QSize(0, 26))
        self.PolishButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PolishButton.setFont(font)
        self.PolishButton.setStyleSheet("    QPushButton{\n"
"        background-color: rgba(31, 37, 51, 50);\n"
"        border: 2px solid #ffffff;\n"
"        border-radius: 13px;\n"
"        min-height: 22px;\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton:hover{\n"
"        background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"    QPushButton:pressed{\n"
"        background-color: rgba(194, 194, 194, 50);\n"
"        border: #c2c2c2;\n"
"    }")
        self.PolishButton.setObjectName("PolishButton")
        self.EnglishButton = QtWidgets.QPushButton(Dialog)
        self.EnglishButton.setGeometry(QtCore.QRect(310, 60, 131, 26))
        self.EnglishButton.setMinimumSize(QtCore.QSize(0, 26))
        self.EnglishButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.EnglishButton.setFont(font)
        self.EnglishButton.setStyleSheet("    QPushButton{\n"
"        background-color: rgba(31, 37, 51, 50);\n"
"        border: 2px solid #ffffff;\n"
"        border-radius: 13px;\n"
"        min-height: 22px;\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton:hover{\n"
"        background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"    QPushButton:pressed{\n"
"        background-color: rgba(194, 194, 194, 50);\n"
"        border: #c2c2c2;\n"
"    }")
        self.EnglishButton.setObjectName("EnglishButton")
        self.ChineseButton = QtWidgets.QPushButton(Dialog)
        self.ChineseButton.setGeometry(QtCore.QRect(390, 180, 131, 26))
        self.ChineseButton.setMinimumSize(QtCore.QSize(0, 26))
        self.ChineseButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ChineseButton.setFont(font)
        self.ChineseButton.setStyleSheet("    QPushButton{\n"
"        background-color: rgba(31, 37, 51, 50);\n"
"        border: 2px solid #ffffff;\n"
"        border-radius: 13px;\n"
"        min-height: 22px;\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton:hover{\n"
"        background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"    QPushButton:pressed{\n"
"        background-color: rgba(194, 194, 194, 50);\n"
"        border: #c2c2c2;\n"
"    }")
        self.ChineseButton.setObjectName("ChineseButton")
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
        self.lang_logo.raise_()
        self.ExitButton.raise_()
        self.ToolLanguageLabel.raise_()
        self.ReferenceButton.raise_()
        self.RussianButton.raise_()
        self.UkrainianButton.raise_()
        self.PolishButton.raise_()
        self.EnglishButton.raise_()
        self.ChineseButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.ToolLanguageLabel.setText(_translate("Dialog", "Язык утилиты"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.RussianButton.setText(_translate("Dialog", "Русский"))
        self.UkrainianButton.setText(_translate("Dialog", "Українська"))
        self.PolishButton.setText(_translate("Dialog", "Polski"))
        self.EnglishButton.setText(_translate("Dialog", "English"))
        self.ChineseButton.setText(_translate("Dialog", "中文"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
