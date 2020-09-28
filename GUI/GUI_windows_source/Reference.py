# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reference.ui'
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 976, 3354))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 150, -1, 150)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.QLabel_1_Modification = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        self.QLabel_1_Modification.setFont(font)
        self.QLabel_1_Modification.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_1_Modification.setAlignment(QtCore.Qt.AlignCenter)
        self.QLabel_1_Modification.setObjectName("QLabel_1_Modification")
        self.verticalLayout_3.addWidget(self.QLabel_1_Modification)
        self.Description_1_0 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_1_0.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_1_0.setFont(font)
        self.Description_1_0.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_1_0.setReadOnly(True)
        self.Description_1_0.setObjectName("Description_1_0")
        self.verticalLayout_3.addWidget(self.Description_1_0)
        self.QLabel_1_1_Manually = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_1_1_Manually.setFont(font)
        self.QLabel_1_1_Manually.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_1_1_Manually.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_1_1_Manually.setObjectName("QLabel_1_1_Manually")
        self.verticalLayout_3.addWidget(self.QLabel_1_1_Manually)
        self.Description_1_1 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_1_1.setMinimumSize(QtCore.QSize(0, 165))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_1_1.setFont(font)
        self.Description_1_1.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_1_1.setReadOnly(True)
        self.Description_1_1.setObjectName("Description_1_1")
        self.verticalLayout_3.addWidget(self.Description_1_1)
        self.QLabel_1_2_Modification = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_1_2_Modification.setFont(font)
        self.QLabel_1_2_Modification.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_1_2_Modification.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_1_2_Modification.setObjectName("QLabel_1_2_Modification")
        self.verticalLayout_3.addWidget(self.QLabel_1_2_Modification)
        self.QLabel_1_3_Collection = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_1_3_Collection.setFont(font)
        self.QLabel_1_3_Collection.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_1_3_Collection.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_1_3_Collection.setObjectName("QLabel_1_3_Collection")
        self.verticalLayout_3.addWidget(self.QLabel_1_3_Collection)
        self.QLabel_2_Modifications = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_2_Modifications.setFont(font)
        self.QLabel_2_Modifications.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_2_Modifications.setAlignment(QtCore.Qt.AlignCenter)
        self.QLabel_2_Modifications.setObjectName("QLabel_2_Modifications")
        self.verticalLayout_3.addWidget(self.QLabel_2_Modifications)
        self.QLabel_2_1_General_Capabilities = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_2_1_General_Capabilities.setFont(font)
        self.QLabel_2_1_General_Capabilities.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_2_1_General_Capabilities.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_2_1_General_Capabilities.setObjectName("QLabel_2_1_General_Capabilities")
        self.verticalLayout_3.addWidget(self.QLabel_2_1_General_Capabilities)
        self.Description_2_1 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_2_1.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_2_1.setFont(font)
        self.Description_2_1.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_2_1.setReadOnly(True)
        self.Description_2_1.setObjectName("Description_2_1")
        self.verticalLayout_3.addWidget(self.Description_2_1)
        self.QLabel_2_2_Extended_Sorter = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_2_2_Extended_Sorter.setFont(font)
        self.QLabel_2_2_Extended_Sorter.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_2_2_Extended_Sorter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_2_2_Extended_Sorter.setObjectName("QLabel_2_2_Extended_Sorter")
        self.verticalLayout_3.addWidget(self.QLabel_2_2_Extended_Sorter)
        self.Description_2_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_2_3.setMinimumSize(QtCore.QSize(0, 170))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_2_3.setFont(font)
        self.Description_2_3.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_2_3.setReadOnly(True)
        self.Description_2_3.setObjectName("Description_2_3")
        self.verticalLayout_3.addWidget(self.Description_2_3)
        self.QLabel_2_2_DoNotSorting = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_2_2_DoNotSorting.setFont(font)
        self.QLabel_2_2_DoNotSorting.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_2_2_DoNotSorting.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_2_2_DoNotSorting.setObjectName("QLabel_2_2_DoNotSorting")
        self.verticalLayout_3.addWidget(self.QLabel_2_2_DoNotSorting)
        self.Description_2_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_2_2.setMinimumSize(QtCore.QSize(0, 115))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_2_2.setFont(font)
        self.Description_2_2.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_2_2.setReadOnly(True)
        self.Description_2_2.setObjectName("Description_2_2")
        self.verticalLayout_3.addWidget(self.Description_2_2)
        self.QLabel_3_Collection = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        self.QLabel_3_Collection.setFont(font)
        self.QLabel_3_Collection.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_3_Collection.setAlignment(QtCore.Qt.AlignCenter)
        self.QLabel_3_Collection.setObjectName("QLabel_3_Collection")
        self.verticalLayout_3.addWidget(self.QLabel_3_Collection)
        self.QLabel_3_1_Functional = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_3_1_Functional.setFont(font)
        self.QLabel_3_1_Functional.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_3_1_Functional.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_3_1_Functional.setObjectName("QLabel_3_1_Functional")
        self.verticalLayout_3.addWidget(self.QLabel_3_1_Functional)
        self.Description_3_1 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_3_1.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_3_1.setFont(font)
        self.Description_3_1.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_3_1.setReadOnly(True)
        self.Description_3_1.setObjectName("Description_3_1")
        self.verticalLayout_3.addWidget(self.Description_3_1)
        self.QLabel_3_2_ModCollection = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.QLabel_3_2_ModCollection.setFont(font)
        self.QLabel_3_2_ModCollection.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_3_2_ModCollection.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.QLabel_3_2_ModCollection.setObjectName("QLabel_3_2_ModCollection")
        self.verticalLayout_3.addWidget(self.QLabel_3_2_ModCollection)
        self.Description_3_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_3_2.setMinimumSize(QtCore.QSize(0, 170))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_3_2.setFont(font)
        self.Description_3_2.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_3_2.setReadOnly(True)
        self.Description_3_2.setObjectName("Description_3_2")
        self.verticalLayout_3.addWidget(self.Description_3_2)
        self.QLabel_4_InterfaceLanguage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        self.QLabel_4_InterfaceLanguage.setFont(font)
        self.QLabel_4_InterfaceLanguage.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_4_InterfaceLanguage.setAlignment(QtCore.Qt.AlignCenter)
        self.QLabel_4_InterfaceLanguage.setObjectName("QLabel_4_InterfaceLanguage")
        self.verticalLayout_3.addWidget(self.QLabel_4_InterfaceLanguage)
        self.Description_4 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_4.setMinimumSize(QtCore.QSize(0, 165))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_4.setFont(font)
        self.Description_4.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_4.setReadOnly(True)
        self.Description_4.setObjectName("Description_4")
        self.verticalLayout_3.addWidget(self.Description_4)
        self.QLabel_5_TranslationLanguage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        self.QLabel_5_TranslationLanguage.setFont(font)
        self.QLabel_5_TranslationLanguage.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    padding: 25px;\n"
"    }\n"
"")
        self.QLabel_5_TranslationLanguage.setAlignment(QtCore.Qt.AlignCenter)
        self.QLabel_5_TranslationLanguage.setObjectName("QLabel_5_TranslationLanguage")
        self.verticalLayout_3.addWidget(self.QLabel_5_TranslationLanguage)
        self.Description_5 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.Description_5.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.Description_5.setFont(font)
        self.Description_5.setStyleSheet("QTextEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    padding: 10px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(50, 50, 50, 90);\n"
"    border-radius: 25px;\n"
"    }\n"
"")
        self.Description_5.setReadOnly(True)
        self.Description_5.setObjectName("Description_5")
        self.verticalLayout_3.addWidget(self.Description_5)
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
        self.BottomShadowFrame = QtWidgets.QFrame(Dialog)
        self.BottomShadowFrame.setGeometry(QtCore.QRect(-50, 610, 1100, 80))
        self.BottomShadowFrame.setMinimumSize(QtCore.QSize(1100, 80))
        self.BottomShadowFrame.setMaximumSize(QtCore.QSize(1100, 200))
        self.BottomShadowFrame.setMouseTracking(False)
        self.BottomShadowFrame.setAcceptDrops(False)
        self.BottomShadowFrame.setStyleSheet("image: url(:/effects/effects/large_bottom_shadow.png);")
        self.BottomShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomShadowFrame.setObjectName("BottomShadowFrame")
        self.BackgroundFrame.raise_()
        self.WindowMoveButton.raise_()
        self.scrollArea.raise_()
        self.ExitButton.raise_()
        self.ReferenceLabel.raise_()
        self.SearchLine.raise_()
        self.AboutToolButton.raise_()
        self.BottomShadowFrame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.ReferenceLabel.setText(_translate("Dialog", "Справка"))
        self.QLabel_1_Modification.setText(_translate("Dialog", "1. Перевод"))
        self.Description_1_0.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Кнопка &quot;Локализировать&quot; - ваш лучший друг в процессе перевода, но он полезен только когда выбран мод.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Пункты про выбор модов:</p></body></html>"))
        self.QLabel_1_1_Manually.setText(_translate("Dialog", "1.1. Вручную"))
        self.Description_1_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Данная функция позволяет найти в файловом менеджере нужный вам файл локализации, обычно имеющий вид *mod_name*_l_english.yml или *name*_name_list.txt</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Утилита переводит только английские исходники</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Локализации хранятся среди файлов мода в папке localisation</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Где лежит сам мод, думаю, объяснять не требуется</p></body></html>"))
        self.QLabel_1_2_Modification.setText(_translate("Dialog", "1.2. Модификации (Смотри пункт 2.)"))
        self.QLabel_1_3_Collection.setText(_translate("Dialog", "1.3. Коллекция (Смотри пункт 3.)"))
        self.QLabel_2_Modifications.setText(_translate("Dialog", "2. Модификации"))
        self.QLabel_2_1_General_Capabilities.setText(_translate("Dialog", "2.1 Общие возможности"))
        self.Description_2_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Клик по названию нужной модификации откроет папку с одноименным модом, что позволит выбрать нужный файл, а также открыть архив в папке мода</p></body></html>"))
        self.QLabel_2_2_Extended_Sorter.setText(_translate("Dialog", "2.2. Расширенный функционал сортировщика"))
        self.Description_2_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Эта функция начала разрабатываться еще до появления сортировки в лаунчере игры, но, все же, свое преимущество она имеет</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Довольно часто, особенно при большом количестве модов, возникает потребность изменить порядок модов не совсем по алфавиту, чтобы избежать конфликтов</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В частности, игра принимает только первый одноименный файл с локализацией, а потому при неправильном расположении модов с списке загрузки переводы могут не работать</p></body></html>"))
        self.QLabel_2_2_DoNotSorting.setText(_translate("Dialog", "Не сортировать"))
        self.Description_2_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Важно помещать моды с локализациями в самом низу списка загрузки, при этом не хочется каждый раз двигать моды вручную, а потому в Сортировщике есть функция &quot;Не сортировать&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если отметить мод как &quot;Не сортировать&quot; то он сохранит свой порядок относительно аналогично выделенных модов и все они будут помещены ПОД остальными модицикациями, что будут сортироваться по алфавиту</p></body></html>"))
        self.QLabel_3_Collection.setText(_translate("Dialog", "3. Коллекция"))
        self.QLabel_3_1_Functional.setText(_translate("Dialog", "3.1. Функционал внутри утилиты"))
        self.Description_3_1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Окно не требует повторного ручного выбора файлов уже добавленных в коллекцию модификаций и содержит в себе основные данные, такие как:</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">имя мода, идентификатор, имена всех файлов локализации и нейм-листов, которые связаны с сохраняемым модом, а также процент завершения локализаций</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если перевод еще не завершен, есть возможность продолжить процесс с последней активной строки или начать новый перевод</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Чтобы сделать это, достаточно нажать на ID для открытия папки с модом, имя файла локализации или нейм-листа для продолжения или начала нового перевода</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Также можно переключать режимы отображения информации кликом по &quot;Steam ID&quot;</p></body></html>"))
        self.QLabel_3_2_ModCollection.setText(_translate("Dialog", "3.2. Локальный мод-сборник из локализаций"))
        self.Description_3_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">В целом, Коллецкция - самостоятельный мод, генерируемый утилитой и расположенный в документах Stellaris, который состоит из вышеупомянутых локализаций, то есть содержит в себе все переводы из данной утилиты</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Коллекцию можно опубликовать в мастерской Steam, используя лаунчер Stellaris, как обычный мод</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Стандартным именем является &quot;Stellaris True Machine Translation Tool&quot;, но вы всегда можете его изменить, нажав кнопку &quot;Переименовать&quot;</p></body></html>"))
        self.QLabel_4_InterfaceLanguage.setText(_translate("Dialog", "4. Язык интерфейса"))
        self.Description_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Все просто - нажимаем на кнопочку с нужным языком и магия в деле</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">К выбору доступно 5 языков:</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Английский, Русский, Украинский, Польский и Китайский</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Просьба обращаться к разработчикам, если заметите неточности в переводе, т.к. перевод, в большинстве своем, машинный</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.QLabel_5_TranslationLanguage.setText(_translate("Dialog", "5. Язык перевода"))
        self.Description_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тут все аналогично пункту 3, только есть возможность использовать поиск</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Нужно два раза кликнуть и удалить текст поиска, затем __ на языке интерфейса __ ввести искомый язык</p></body></html>"))
        self.SearchLine.setText(_translate("Dialog", "Поиск"))
        self.AboutToolButton.setText(_translate("Dialog", "Об утилите"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
