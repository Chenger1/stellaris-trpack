# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModsList.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 380)
        Dialog.setMinimumSize(QtCore.QSize(650, 380))
        Dialog.setMaximumSize(QtCore.QSize(650, 380))
        Dialog.setStyleSheet("background-color: transparent;\n"
"")
        self.lang_logo = QtWidgets.QLabel(Dialog)
        self.lang_logo.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.lang_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/lang.png);\n"
"")
        self.lang_logo.setText("")
        self.lang_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lang_logo.setObjectName("lang_logo")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(0, -10, 687, 387))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(687, 387))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 387))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/MoreOutputLanguage.png);")
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
        self.ReferenceButton = QtWidgets.QPushButton(Dialog)
        self.ReferenceButton.setGeometry(QtCore.QRect(10, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ReferenceButton.setFont(font)
        self.ReferenceButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(31, 37, 51, 0);\n"
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
        self.LanguagesListLabel = QtWidgets.QLabel(Dialog)
        self.LanguagesListLabel.setGeometry(QtCore.QRect(50, 20, 231, 61))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.LanguagesListLabel.setFont(font)
        self.LanguagesListLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.LanguagesListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LanguagesListLabel.setObjectName("LanguagesListLabel")
        self.LandingArea = QtWidgets.QScrollArea(Dialog)
        self.LandingArea.setGeometry(QtCore.QRect(10, 100, 631, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LandingArea.sizePolicy().hasHeightForWidth())
        self.LandingArea.setSizePolicy(sizePolicy)
        self.LandingArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LandingArea.setStyleSheet("QScrollBar:vertical{\n"
"    background: transparent;\n"
"    width: 5px;\n"
"    margin: 0;\n"
"    }\n"
"QScrollBar::handle:vertical{\n"
"    background-color: #5abe41;\n"
"    min-height: 20px;\n"
"    }\n"
"QScrollBar::add-line:vertical{\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    }\n"
"QScrollBar::sub-line:vertical{\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    }\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    }")
        self.LandingArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LandingArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LandingArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.LandingArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LandingArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.LandingArea.setWidgetResizable(True)
        self.LandingArea.setAlignment(QtCore.Qt.AlignCenter)
        self.LandingArea.setObjectName("LandingArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 626, 261))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, 150)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)
        self.LandingArea.setWidget(self.scrollAreaWidgetContents)
        self.BottomShadowFrame = QtWidgets.QFrame(Dialog)
        self.BottomShadowFrame.setGeometry(QtCore.QRect(-20, 300, 687, 100))
        self.BottomShadowFrame.setMinimumSize(QtCore.QSize(687, 100))
        self.BottomShadowFrame.setMaximumSize(QtCore.QSize(687, 100))
        self.BottomShadowFrame.setMouseTracking(False)
        self.BottomShadowFrame.setAcceptDrops(False)
        self.BottomShadowFrame.setStyleSheet("background-image: url(:/effects/effects/bottom_shadow.png);")
        self.BottomShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomShadowFrame.setObjectName("BottomShadowFrame")
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
        self.LandingArea.raise_()
        self.ReferenceButton.raise_()
        self.lang_logo.raise_()
        self.RollUpButton.raise_()
        self.ExitButton.raise_()
        self.LanguagesListLabel.raise_()
        self.BottomShadowFrame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.LanguagesListLabel.setText(_translate("Dialog", "Список модов"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
from GUI.pictures import resources
