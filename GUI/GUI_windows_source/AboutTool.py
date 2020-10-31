# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutTool.ui'
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
        self.InfoLabel_2 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_2.setGeometry(QtCore.QRect(10, 70, 511, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_2.setFont(font)
        self.InfoLabel_2.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_2.setOpenExternalLinks(True)
        self.InfoLabel_2.setObjectName("InfoLabel_2")
        self.InfoLabel_1 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_1.setGeometry(QtCore.QRect(30, 30, 591, 41))
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
        self.ContactUsButton.setGeometry(QtCore.QRect(170, 200, 311, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ContactUsButton.setFont(font)
        self.ContactUsButton.setStyleSheet("QPushButton{\n"
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
        self.InfoLabel_3 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_3.setGeometry(QtCore.QRect(30, 150, 591, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_3.setFont(font)
        self.InfoLabel_3.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_3.setOpenExternalLinks(True)
        self.InfoLabel_3.setObjectName("InfoLabel_3")
        self.InfoLabel_4 = QtWidgets.QLabel(Dialog)
        self.InfoLabel_4.setGeometry(QtCore.QRect(130, 100, 521, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.InfoLabel_4.setFont(font)
        self.InfoLabel_4.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.InfoLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel_4.setOpenExternalLinks(True)
        self.InfoLabel_4.setObjectName("InfoLabel_4")
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.ExitButton.raise_()
        self.InfoLabel_2.raise_()
        self.InfoLabel_1.raise_()
        self.ContactUsButton.raise_()
        self.InfoLabel_3.raise_()
        self.InfoLabel_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Об утилите"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.InfoLabel_2.setText(_translate("Dialog", "<html><head/><body><p>на основе скриптов <a href=\"https://github.com/pacas/stellaris-trpack\"><span style=\" text-decoration: none; color:#ffffff;\">Pacas</span></a> и <a href=\"https://github.com/haifengkao/StellairsLoadOrderFixer24/blob/master/load_order_stellaris24.py\"><span style=\" text-decoration: none; color:#ffffff;\">haifengkao</span></a></p></body></html>"))
        self.InfoLabel_1.setText(_translate("Dialog", "Приложение разработано Letiso и Chenger1"))
        self.ContactUsButton.setText(_translate("Dialog", "Связаться с разработчиками"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
        self.InfoLabel_3.setText(_translate("Dialog", "<html><head/><body><p>для упрощения процесса локализации</p></body></html>"))
        self.InfoLabel_4.setText(_translate("Dialog", "<html><head/><body><p>при использовании <a href=\"https://python.org/download\"><span style=\" text-decoration: none; color:#ffffff;\">Python 3<\\a> и <a href=\"https://qt.io/download\"><span style=\" text-decoration: none; color:#ffffff;\">QT5<\\a></p></body></html>\n"
""))
