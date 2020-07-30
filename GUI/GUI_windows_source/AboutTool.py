# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutTool.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from GUI.pictures import resources

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 250)
        Dialog.setMinimumSize(QtCore.QSize(650, 250))
        Dialog.setMaximumSize(QtCore.QSize(650, 250))
        Dialog.setStyleSheet("background-color: transparent;")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 867, 264))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(867, 264))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(867, 250))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/AboutTool.png);")
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
        self.InfoLabel_0.setGeometry(QtCore.QRect(50, 30, 561, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_0.setFont(font)
        self.InfoLabel_0.setStyleSheet("background-color: none;\n"
                                       "color: #ffffff;")
        self.InfoLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_0.setObjectName("InfoLabel_0")
        self.InfoLabel_2 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_2.setGeometry(QtCore.QRect(120, 120, 491, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_2.setFont(font)
        self.InfoLabel_2.setStyleSheet("background-color: none;\n"
                                       "color: #ffffff;")
        self.InfoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_2.setOpenExternalLinks(True)
        self.InfoLabel_2.setObjectName("InfoLabel_2")
        self.VersionLabel = QtWidgets.QLabel(Dialog)
        self.VersionLabel.setGeometry(QtCore.QRect(380, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.VersionLabel.setFont(font)
        self.VersionLabel.setStyleSheet("background-color: none;\n"
                                        "color: #ffffff;")
        self.VersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VersionLabel.setObjectName("VersionLabel")
        self.InfoLabel_1 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_1.setGeometry(QtCore.QRect(20, 80, 451, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_1.setFont(font)
        self.InfoLabel_1.setStyleSheet("background-color: none;\n"
                                       "color: #ffffff;")
        self.InfoLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_1.setObjectName("InfoLabel_1")
        self.ContactUsButton = QtWidgets.QPushButton(Dialog)
        self.ContactUsButton.setGeometry(QtCore.QRect(40, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ContactUsButton.setFont(font)
        self.ContactUsButton.setStyleSheet("QPushButton{\n"
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
        self.ContactUsButton.setObjectName("ContactUsButton")
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
        self.InfoLabel_2.raise_()
        self.VersionLabel.raise_()
        self.InfoLabel_1.raise_()
        self.ContactUsButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.InfoLabel_0.setText(_translate("Dialog", "О Stellaris True Machine Translation Tool"))
        self.InfoLabel_2.setText(_translate("Dialog", "<html><head/><body><p>при использовании Python 3 на основе <a "
                                                      "href=\"https://github.com/pacas/stellaris-trpack\"><span "
                                                      "style=\" text-decoration: underline; color:#ffffff;\">софта "
                                                      "Pacas</span></a><span style=\" "
                                                      "color:#ffffff;\">.</span></p></body></html>"))
        self.VersionLabel.setText(_translate("Dialog", "Версия ПО: 0.5.5"))
        self.InfoLabel_1.setText(_translate("Dialog", "Приложение разработано Letiso и Chenger"))
        self.ContactUsButton.setText(_translate("Dialog", "Связаться с разработчиками"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
