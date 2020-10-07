# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_windows_source\ModsList.ui'
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
        Dialog.resize(900, 580)
        Dialog.setMinimumSize(QtCore.QSize(900, 580))
        Dialog.setMaximumSize(QtCore.QSize(900, 580))
        Dialog.setStyleSheet("background-color: transparent;\n"
"")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(0, -10, 900, 610))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(900, 610))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(687, 387))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/ModList.png);")
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
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
        self.LandingArea = QtWidgets.QScrollArea(Dialog)
        self.LandingArea.setGeometry(QtCore.QRect(10, 101, 880, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LandingArea.sizePolicy().hasHeightForWidth())
        self.LandingArea.setSizePolicy(sizePolicy)
        self.LandingArea.setMinimumSize(QtCore.QSize(880, 360))
        self.LandingArea.setMaximumSize(QtCore.QSize(880, 400))
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 875, 391))
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
        self.BottomShadowFrame.setGeometry(QtCore.QRect(0, 481, 900, 100))
        self.BottomShadowFrame.setMinimumSize(QtCore.QSize(900, 100))
        self.BottomShadowFrame.setMaximumSize(QtCore.QSize(900, 100))
        self.BottomShadowFrame.setMouseTracking(False)
        self.BottomShadowFrame.setAcceptDrops(False)
        self.BottomShadowFrame.setStyleSheet("background-image: url(:/effects/effects/bottom_shadow.png);")
        self.BottomShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomShadowFrame.setObjectName("BottomShadowFrame")
        self.WindowMoveButton = QtWidgets.QPushButton(Dialog)
        self.WindowMoveButton.setGeometry(QtCore.QRect(0, 0, 901, 21))
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
        self.SortButton = QtWidgets.QPushButton(Dialog)
        self.SortButton.setGeometry(QtCore.QRect(30, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SortButton.setFont(font)
        self.SortButton.setStyleSheet("QPushButton{\n"
"    background-color: #05B8CC;\n"
"    border: 2px solid #05B8CC;\n"
"    border-radius: 15px;\n"
"    color: #1f2533;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #31858f;\n"
"    border: #31858f;\n"
"    color: #ffffff;    }\n"
"QPushButton:pressed{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    }")
        self.SortButton.setObjectName("SortButton")
        self.PlaysetsList = QtWidgets.QComboBox(Dialog)
        self.PlaysetsList.setGeometry(QtCore.QRect(520, 40, 301, 51))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        self.PlaysetsList.setFont(font)
        self.PlaysetsList.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PlaysetsList.setStyleSheet(" QComboBox {\n"
"    padding-bottom: 30px;\n"
"    color: white;\n"
"    border: transparent;\n"
"    margin: 30px;\n"
"}\n"
"\n"
" QAbstractItemView {\n"
"    background-color: #141821;\n"
"    border: 1px solid #141821;\n"
"    border-radius: 15px;\n"
"    selection-background-color: transparent;\n"
"    selection-color: #05B8CC;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    outline: 0px;\n"
"}")
        self.PlaysetsList.setEditable(False)
        self.PlaysetsList.setObjectName("PlaysetsList")
        self.ReverseSortingButton = QtWidgets.QPushButton(Dialog)
        self.ReverseSortingButton.setGeometry(QtCore.QRect(30, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ReverseSortingButton.setFont(font)
        self.ReverseSortingButton.setStyleSheet("QPushButton{\n"
"    background-color: #5abe41;\n"
"    border: 3px solid #5abe41;\n"
"    border-radius: 10px;\n"
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
        self.ReverseSortingButton.setObjectName("ReverseSortingButton")
        self.ResetButton = QtWidgets.QPushButton(Dialog)
        self.ResetButton.setGeometry(QtCore.QRect(760, 520, 111, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ResetButton.setFont(font)
        self.ResetButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #31858f;\n"
"    border: #31858f;\n"
"    color: #ffffff;    }\n"
"QPushButton:pressed{\n"
"    background-color: #05B8CC;\n"
"    border: 2px solid #05B8CC;\n"
"    }r")
        self.ResetButton.setObjectName("ResetButton")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(870, 0, 21, 21))
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
        self.ModListLabel = QtWidgets.QLabel(Dialog)
        self.ModListLabel.setGeometry(QtCore.QRect(10, 30, 491, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ModListLabel.setFont(font)
        self.ModListLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ModListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ModListLabel.setObjectName("ModListLabel")
        self.ActivateSortLabel = QtWidgets.QLabel(Dialog)
        self.ActivateSortLabel.setGeometry(QtCore.QRect(620, 81, 251, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ActivateSortLabel.setFont(font)
        self.ActivateSortLabel.setStyleSheet("background-color: none;\n"
"color: #ffffff;")
        self.ActivateSortLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ActivateSortLabel.setObjectName("ActivateSortLabel")
        self.ActivationSwticherButton = QtWidgets.QPushButton(Dialog)
        self.ActivationSwticherButton.setGeometry(QtCore.QRect(570, 520, 171, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ActivationSwticherButton.setFont(font)
        self.ActivationSwticherButton.setStyleSheet("QPushButton{\n"
"    background-color: #5abe41;\n"
"    border: 3px solid #5abe41;\n"
"    border-radius: 15px;\n"
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
        self.ActivationSwticherButton.setText("")
        self.ActivationSwticherButton.setObjectName("ActivationSwticherButton")
        self.SearchLine = QtWidgets.QLineEdit(Dialog)
        self.SearchLine.setGeometry(QtCore.QRect(220, 520, 221, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.SearchLine.setFont(font)
        self.SearchLine.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #ffffff;\n"
"    border-radius: 15px;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }")
        self.SearchLine.setAlignment(QtCore.Qt.AlignCenter)
        self.SearchLine.setReadOnly(False)
        self.SearchLine.setObjectName("SearchLine")
        self.StringsList = QtWidgets.QLabel(Dialog)
        self.StringsList.setGeometry(QtCore.QRect(230, 40, 241, 20))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.StringsList.setFont(font)
        self.StringsList.setAlignment(QtCore.Qt.AlignCenter)
        self.StringsList.setObjectName("StringsList")
        self.StringsList.raise_()
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.LandingArea.raise_()
        self.ReferenceButton.raise_()
        self.BottomShadowFrame.raise_()
        self.SortButton.raise_()
        self.PlaysetsList.raise_()
        self.ResetButton.raise_()
        self.ExitButton.raise_()
        self.ModListLabel.raise_()
        self.ActivateSortLabel.raise_()
        self.ActivationSwticherButton.raise_()
        self.ReverseSortingButton.raise_()
        self.SearchLine.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Модификации"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
        self.SortButton.setText(_translate("Dialog", "Сортировать"))
        self.ReverseSortingButton.setText(_translate("Dialog", "A-Z"))
        self.ResetButton.setText(_translate("Dialog", "Сбросить"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.ModListLabel.setText(_translate("Dialog", "Список модов"))
        self.ActivateSortLabel.setText(_translate("Dialog", "Активация и сортировка"))
        self.SearchLine.setText(_translate("Dialog", "Поиск"))
        self.StringsList.setText(_translate("Dialog", "Отключить.Активировать"))
