# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contact.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 350)
        Dialog.setMinimumSize(QtCore.QSize(650, 350))
        Dialog.setMaximumSize(QtCore.QSize(650, 350))
        Dialog.setStyleSheet("background-color: transparent;")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 687, 360))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 360))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 250))
        self.BackgroundFrame.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/Contact.png);")
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
        self.InfoLabel_0 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_0.setGeometry(QtCore.QRect(20, 30, 611, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_0.setFont(font)
        self.InfoLabel_0.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_0.setObjectName("InfoLabel_0")
        self.ChengerLabel = QtWidgets.QLabel(Dialog)
        self.ChengerLabel.setGeometry(QtCore.QRect(350, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ChengerLabel.setFont(font)
        self.ChengerLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ChengerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ChengerLabel.setObjectName("ChengerLabel")
        self.InfoLabel_1 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_1.setGeometry(QtCore.QRect(20, 240, 611, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_1.setFont(font)
        self.InfoLabel_1.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_1.setObjectName("InfoLabel_1")
        self.LetisoEmailLine = QtWidgets.QLineEdit(Dialog)
        self.LetisoEmailLine.setGeometry(QtCore.QRect(30, 290, 211, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.LetisoEmailLine.setFont(font)
        self.LetisoEmailLine.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 0);\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #rgba(56, 57, 61, 10);\n"
"    }\n"
"")
        self.LetisoEmailLine.setFrame(False)
        self.LetisoEmailLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LetisoEmailLine.setReadOnly(True)
        self.LetisoEmailLine.setObjectName("LetisoEmailLine")
        self.ChengerEmailLine = QtWidgets.QLineEdit(Dialog)
        self.ChengerEmailLine.setGeometry(QtCore.QRect(400, 290, 221, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.ChengerEmailLine.setFont(font)
        self.ChengerEmailLine.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 0);\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #rgba(56, 57, 61, 10);\n"
"    }\n"
"")
        self.ChengerEmailLine.setFrame(False)
        self.ChengerEmailLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChengerEmailLine.setReadOnly(True)
        self.ChengerEmailLine.setObjectName("ChengerEmailLine")
        self.InfoLabel_2 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_2.setGeometry(QtCore.QRect(260, 290, 151, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_2.setFont(font)
        self.InfoLabel_2.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_2.setObjectName("InfoLabel_2")
        self.MidLineFrame = QtWidgets.QFrame(Dialog)
        self.MidLineFrame.setGeometry(QtCore.QRect(-20, 210, 700, 20))
        self.MidLineFrame.setMinimumSize(QtCore.QSize(700, 20))
        self.MidLineFrame.setMaximumSize(QtCore.QSize(700, 20))
        self.MidLineFrame.setStyleSheet("background-image: url(:/effects/effects/mid_line.png);")
        self.MidLineFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MidLineFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MidLineFrame.setObjectName("MidLineFrame")
        self.SteamChengerLink = QtWidgets.QLabel(Dialog)
        self.SteamChengerLink.setGeometry(QtCore.QRect(470, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SteamChengerLink.setFont(font)
        self.SteamChengerLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.SteamChengerLink.setAlignment(QtCore.Qt.AlignCenter)
        self.SteamChengerLink.setOpenExternalLinks(True)
        self.SteamChengerLink.setObjectName("SteamChengerLink")
        self.GitHubChengerLink = QtWidgets.QLabel(Dialog)
        self.GitHubChengerLink.setGeometry(QtCore.QRect(450, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.GitHubChengerLink.setFont(font)
        self.GitHubChengerLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.GitHubChengerLink.setAlignment(QtCore.Qt.AlignCenter)
        self.GitHubChengerLink.setOpenExternalLinks(True)
        self.GitHubChengerLink.setObjectName("GitHubChengerLink")
        self.TelegramChengerLink = QtWidgets.QLabel(Dialog)
        self.TelegramChengerLink.setGeometry(QtCore.QRect(470, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.TelegramChengerLink.setFont(font)
        self.TelegramChengerLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.TelegramChengerLink.setAlignment(QtCore.Qt.AlignCenter)
        self.TelegramChengerLink.setOpenExternalLinks(True)
        self.TelegramChengerLink.setObjectName("TelegramChengerLink")
        self.LetisoLabel = QtWidgets.QLabel(Dialog)
        self.LetisoLabel.setGeometry(QtCore.QRect(170, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LetisoLabel.setFont(font)
        self.LetisoLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.LetisoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LetisoLabel.setObjectName("LetisoLabel")
        self.git_logo_1 = QtWidgets.QLabel(Dialog)
        self.git_logo_1.setGeometry(QtCore.QRect(540, 70, 51, 51))
        self.git_logo_1.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/github.png);\n"
"")
        self.git_logo_1.setText("")
        self.git_logo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.git_logo_1.setObjectName("git_logo_1")
        self.steam_logo_1 = QtWidgets.QLabel(Dialog)
        self.steam_logo_1.setGeometry(QtCore.QRect(560, 110, 51, 51))
        self.steam_logo_1.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/steam.png);\n"
"")
        self.steam_logo_1.setText("")
        self.steam_logo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo_1.setObjectName("steam_logo_1")
        self.telegram_logo_1 = QtWidgets.QLabel(Dialog)
        self.telegram_logo_1.setGeometry(QtCore.QRect(580, 150, 51, 51))
        self.telegram_logo_1.setStyleSheet("background-color: none;\n"
"image:  url(:/icons/icons/telegram.png);\n"
"")
        self.telegram_logo_1.setText("")
        self.telegram_logo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.telegram_logo_1.setObjectName("telegram_logo_1")
        self.TelegramLetisoLink = QtWidgets.QLabel(Dialog)
        self.TelegramLetisoLink.setGeometry(QtCore.QRect(50, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.TelegramLetisoLink.setFont(font)
        self.TelegramLetisoLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.TelegramLetisoLink.setAlignment(QtCore.Qt.AlignCenter)
        self.TelegramLetisoLink.setOpenExternalLinks(True)
        self.TelegramLetisoLink.setObjectName("TelegramLetisoLink")
        self.telegram_logo_0 = QtWidgets.QLabel(Dialog)
        self.telegram_logo_0.setGeometry(QtCore.QRect(10, 150, 51, 51))
        self.telegram_logo_0.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/telegram.png);")
        self.telegram_logo_0.setText("")
        self.telegram_logo_0.setAlignment(QtCore.Qt.AlignCenter)
        self.telegram_logo_0.setObjectName("telegram_logo_0")
        self.SteamLetisoLink = QtWidgets.QLabel(Dialog)
        self.SteamLetisoLink.setGeometry(QtCore.QRect(70, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SteamLetisoLink.setFont(font)
        self.SteamLetisoLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.SteamLetisoLink.setAlignment(QtCore.Qt.AlignCenter)
        self.SteamLetisoLink.setOpenExternalLinks(True)
        self.SteamLetisoLink.setObjectName("SteamLetisoLink")
        self.steam_logo_0 = QtWidgets.QLabel(Dialog)
        self.steam_logo_0.setGeometry(QtCore.QRect(30, 110, 51, 51))
        self.steam_logo_0.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/steam.png);")
        self.steam_logo_0.setText("")
        self.steam_logo_0.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo_0.setObjectName("steam_logo_0")
        self.git_logo_0 = QtWidgets.QLabel(Dialog)
        self.git_logo_0.setGeometry(QtCore.QRect(50, 70, 51, 51))
        self.git_logo_0.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/github.png);\n"
"")
        self.git_logo_0.setText("")
        self.git_logo_0.setAlignment(QtCore.Qt.AlignCenter)
        self.git_logo_0.setObjectName("git_logo_0")
        self.GitHubLetisoLink = QtWidgets.QLabel(Dialog)
        self.GitHubLetisoLink.setGeometry(QtCore.QRect(90, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.GitHubLetisoLink.setFont(font)
        self.GitHubLetisoLink.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.GitHubLetisoLink.setAlignment(QtCore.Qt.AlignCenter)
        self.GitHubLetisoLink.setOpenExternalLinks(True)
        self.GitHubLetisoLink.setObjectName("GitHubLetisoLink")
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
        self.ExitButton.raise_()
        self.RollUpButton.raise_()
        self.InfoLabel_0.raise_()
        self.ChengerLabel.raise_()
        self.InfoLabel_1.raise_()
        self.LetisoEmailLine.raise_()
        self.ChengerEmailLine.raise_()
        self.InfoLabel_2.raise_()
        self.MidLineFrame.raise_()
        self.SteamChengerLink.raise_()
        self.GitHubChengerLink.raise_()
        self.TelegramChengerLink.raise_()
        self.LetisoLabel.raise_()
        self.git_logo_1.raise_()
        self.steam_logo_1.raise_()
        self.telegram_logo_1.raise_()
        self.TelegramLetisoLink.raise_()
        self.telegram_logo_0.raise_()
        self.SteamLetisoLink.raise_()
        self.steam_logo_0.raise_()
        self.git_logo_0.raise_()
        self.GitHubLetisoLink.raise_()
        self.ReferenceButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.InfoLabel_0.setText(_translate("Dialog", "Вы можете связаться с нами, если пользуетесь:"))
        self.ChengerLabel.setText(_translate("Dialog", "Chenger"))
        self.InfoLabel_1.setText(_translate("Dialog", "Также пишите свои вопросы на электронную почту:"))
        self.LetisoEmailLine.setText(_translate("Dialog", "letisodianta@gmail.com"))
        self.ChengerEmailLine.setText(_translate("Dialog", "chenger@gmail.com"))
        self.InfoLabel_2.setText(_translate("Dialog", "либо"))
        self.SteamChengerLink.setText(_translate("Dialog", "Steam"))
        self.GitHubChengerLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://github.com/Chenger1\"><span style=\" text-decoration: underline; color:#ffffff;\">GitHub</span></a></p></body></html>"))
        self.TelegramChengerLink.setText(_translate("Dialog", "Telegram"))
        self.LetisoLabel.setText(_translate("Dialog", "Letiso"))
        self.TelegramLetisoLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://t.me/Letiso_Dianta\"><span style=\" text-decoration: underline; color:#ffffff;\">Telegram</span></a></p></body></html>"))
        self.SteamLetisoLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"http://steamcommunity.com/id/letiso\"><span style=\" text-decoration: underline; color:#ffffff;\">Steam</span></a></p></body></html>"))
        self.GitHubLetisoLink.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://github.com/Letiso\"><span style=\" color:#ffffff;\">GitHub</span></a></p></body></html>"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
from GUI.pictures import resources
