# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reference.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from GUI.pictures import resources

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 650)
        Dialog.setMinimumSize(QtCore.QSize(1000, 650))
        Dialog.setMaximumSize(QtCore.QSize(1000, 650))
        Dialog.setStyleSheet("background-color: transparent;\n"
                             "")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(0, -10, 1050, 700))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(1050, 700))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(1050, 700))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/Reference.png);")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(970, 0, 21, 21))
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
        self.RollUpButton.setGeometry(QtCore.QRect(950, 0, 21, 21))
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
        self.ReferenceLabel = QtWidgets.QLabel(Dialog)
        self.ReferenceLabel.setGeometry(QtCore.QRect(50, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ReferenceLabel.setFont(font)
        self.ReferenceLabel.setStyleSheet("background-color: none;\n"
                                          "color: #ffffff;")
        self.ReferenceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ReferenceLabel.setObjectName("ReferenceLabel")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 90, 981, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
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
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 976, 561))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 150, -1, 150)
        self.verticalLayout_3.setSpacing(149)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.SearchLine = QtWidgets.QLineEdit(Dialog)
        self.SearchLine.setGeometry(QtCore.QRect(380, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.SearchLine.setFont(font)
        self.SearchLine.setStyleSheet("QLineEdit{\n"
                                      "    background-color: #5abe41;\n"
                                      "    border: 2px solid #5abe41;\n"
                                      "    border-radius: 15px;\n"
                                      "    color: #1f2533;\n"
                                      "    }\n"
                                      "QLineEdit:hover{\n"
                                      "    background-color: #438e30;\n"
                                      "    border: #438e30;\n"
                                      "    color: #ffffff;\n"
                                      "    }")
        self.SearchLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SearchLine.setReadOnly(False)
        self.SearchLine.setObjectName("SearchLine")
        self.BottomShadowFrame = QtWidgets.QFrame(Dialog)
        self.BottomShadowFrame.setGeometry(QtCore.QRect(-10, 580, 1050, 80))
        self.BottomShadowFrame.setMinimumSize(QtCore.QSize(1050, 80))
        self.BottomShadowFrame.setMaximumSize(QtCore.QSize(1050, 80))
        self.BottomShadowFrame.setMouseTracking(False)
        self.BottomShadowFrame.setAcceptDrops(False)
        self.BottomShadowFrame.setStyleSheet("background-image: url(:/background/bottom_shadow.png);")
        self.BottomShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomShadowFrame.setObjectName("BottomShadowFrame")
        self.AboutToolButton = QtWidgets.QPushButton(Dialog)
        self.AboutToolButton.setGeometry(QtCore.QRect(770, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.AboutToolButton.setFont(font)
        self.AboutToolButton.setStyleSheet("QPushButton{\n"
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
        self.AboutToolButton.setObjectName("AboutToolButton")
        self.WindowMoveButton = QtWidgets.QPushButton(Dialog)
        self.WindowMoveButton.setGeometry(QtCore.QRect(0, 0, 1001, 21))
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
        self.scrollArea.raise_()
        self.ReferenceButton.raise_()
        self.RollUpButton.raise_()
        self.ExitButton.raise_()
        self.ReferenceLabel.raise_()
        self.SearchLine.raise_()
        self.BottomShadowFrame.raise_()
        self.AboutToolButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.ReferenceLabel.setText(_translate("Dialog", "Справка"))
        self.SearchLine.setText(_translate("Dialog", "Поиск"))
        self.AboutToolButton.setText(_translate("Dialog", "Об утилите"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
