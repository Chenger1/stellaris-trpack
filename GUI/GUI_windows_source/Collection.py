# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Collection.ui'
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
        Dialog.resize(880, 580)
        Dialog.setMinimumSize(QtCore.QSize(880, 580))
        Dialog.setMaximumSize(QtCore.QSize(880, 580))
        Dialog.setStyleSheet("background-color: transparent;\n"
"")
        self.BackgroundFrame = QtWidgets.QFrame(Dialog)
        self.BackgroundFrame.setGeometry(QtCore.QRect(-20, -10, 900, 600))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(900, 60))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(900, 600))
        self.BackgroundFrame.setStyleSheet("background-image: url(:/backgrounds/backgrounds/Collection.png);")
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
        self.LandingArea.setGeometry(QtCore.QRect(10, 80, 860, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LandingArea.sizePolicy().hasHeightForWidth())
        self.LandingArea.setSizePolicy(sizePolicy)
        self.LandingArea.setMinimumSize(QtCore.QSize(860, 360))
        self.LandingArea.setMaximumSize(QtCore.QSize(860, 500))
        self.LandingArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LandingArea.setStyleSheet("QScrollBar:vertical{\n"
"    background: transparent;\n"
"    width: 5px;\n"
"    margin: 0;\n"
"    }\n"
"QScrollBar::handle:vertical{\n"
"    background-color: #05B8CC;\n"
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -221, 855, 652))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 15, -1, 150)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(60)
        self.gridLayout.setObjectName("gridLayout")
        self.ModDescriptionText = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.ModDescriptionText.setMinimumSize(QtCore.QSize(0, 250))
        self.ModDescriptionText.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        self.ModDescriptionText.setFont(font)
        self.ModDescriptionText.setAccessibleName("")
        self.ModDescriptionText.setStyleSheet("QTextEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #05B8CC;\n"
"    border-radius: 40px;\n"
"    color: #ffffff;\n"
"    padding: 15px;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.ModDescriptionText.setReadOnly(False)
        self.ModDescriptionText.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.ModDescriptionText.setObjectName("ModDescriptionText")
        self.gridLayout.addWidget(self.ModDescriptionText, 2, 0, 1, 1)
        self.NewNameText = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.NewNameText.setMinimumSize(QtCore.QSize(0, 40))
        self.NewNameText.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        self.NewNameText.setFont(font)
        self.NewNameText.setStyleSheet("QTextEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 1px solid transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.NewNameText.setReadOnly(False)
        self.NewNameText.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.NewNameText.setObjectName("NewNameText")
        self.gridLayout.addWidget(self.NewNameText, 0, 0, 1, 1)
        self.ModListLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.ModListLabel.setFont(font)
        self.ModListLabel.setStyleSheet("QLabel{    background-color: rgba(31, 37, 51, 50);\n"
"    border: 2px solid #05B8CC;\n"
"    border-radius: 45px;\n"
"    color: #ffffff;\n"
"    padding: 15px;\n"
"    }\n"
"QLabel:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.ModListLabel.setText("")
        self.ModListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ModListLabel.setObjectName("ModListLabel")
        self.gridLayout.addWidget(self.ModListLabel, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.LandingArea.setWidget(self.scrollAreaWidgetContents)
        self.BottomShadowFrame = QtWidgets.QFrame(Dialog)
        self.BottomShadowFrame.setGeometry(QtCore.QRect(0, 481, 900, 100))
        self.BottomShadowFrame.setMinimumSize(QtCore.QSize(900, 100))
        self.BottomShadowFrame.setMaximumSize(QtCore.QSize(900, 120))
        self.BottomShadowFrame.setMouseTracking(False)
        self.BottomShadowFrame.setAcceptDrops(False)
        self.BottomShadowFrame.setStyleSheet("background-image: url(:/effects/effects/bottom_shadow.png);")
        self.BottomShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomShadowFrame.setObjectName("BottomShadowFrame")
        self.WindowMoveButton = QtWidgets.QPushButton(Dialog)
        self.WindowMoveButton.setGeometry(QtCore.QRect(0, 0, 881, 21))
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
        self.OptionsListComboBox = QtWidgets.QComboBox(Dialog)
        self.OptionsListComboBox.setGeometry(QtCore.QRect(470, 40, 271, 51))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.OptionsListComboBox.setFont(font)
        self.OptionsListComboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.OptionsListComboBox.setStyleSheet(" QComboBox {\n"
"    padding-bottom: 30px;\n"
"    color: white;\n"
"    border: transparent;\n"
"    margin: 26px;\n"
"}\n"
" QComboBox::hover {\n"
"    background-color: #05B8CC;\n"
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
        self.OptionsListComboBox.setEditable(False)
        self.OptionsListComboBox.setObjectName("OptionsListComboBox")
        self.OptionsListComboBox.addItem("")
        self.OptionsListComboBox.addItem("")
        self.OptionsListComboBox.addItem("")
        self.OptionsListComboBox.addItem("")
        self.ContinueButton = QtWidgets.QPushButton(Dialog)
        self.ContinueButton.setGeometry(QtCore.QRect(30, 530, 241, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ContinueButton.setFont(font)
        self.ContinueButton.setStyleSheet("QPushButton{\n"
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
        self.ContinueButton.setText("")
        self.ContinueButton.setObjectName("ContinueButton")
        self.StatusLabel = QtWidgets.QLabel(Dialog)
        self.StatusLabel.setGeometry(QtCore.QRect(690, 40, 171, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"")
        self.StatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLabel.setObjectName("StatusLabel")
        self.CollectionLabel = QtWidgets.QLabel(Dialog)
        self.CollectionLabel.setGeometry(QtCore.QRect(70, 29, 231, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        self.CollectionLabel.setFont(font)
        self.CollectionLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"")
        self.CollectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CollectionLabel.setObjectName("CollectionLabel")
        self.ExitButton = QtWidgets.QPushButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(850, 0, 21, 21))
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
        self.CollectionNameLabel = QtWidgets.QLabel(Dialog)
        self.CollectionNameLabel.setGeometry(QtCore.QRect(300, 530, 561, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(12)
        self.CollectionNameLabel.setFont(font)
        self.CollectionNameLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"")
        self.CollectionNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CollectionNameLabel.setObjectName("CollectionNameLabel")
        self.mod_list_logo = QtWidgets.QLabel(Dialog)
        self.mod_list_logo.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.mod_list_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/collection.png);")
        self.mod_list_logo.setText("")
        self.mod_list_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.mod_list_logo.setObjectName("mod_list_logo")
        self.StringsList = QtWidgets.QLabel(Dialog)
        self.StringsList.setGeometry(QtCore.QRect(280, 40, 191, 20))
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
        self.StatusLabel.raise_()
        self.CollectionLabel.raise_()
        self.ExitButton.raise_()
        self.CollectionNameLabel.raise_()
        self.ContinueButton.raise_()
        self.mod_list_logo.raise_()
        self.OptionsListComboBox.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Коллекция"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.ModDescriptionText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.NewNameText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
        self.OptionsListComboBox.setItemText(0, _translate("Dialog", "SteamWorkshop ID"))
        self.OptionsListComboBox.setItemText(1, _translate("Dialog", "Локализации"))
        self.OptionsListComboBox.setItemText(2, _translate("Dialog", "Нейм-листы"))
        self.OptionsListComboBox.setItemText(3, _translate("Dialog", "Настройки"))
        self.StatusLabel.setText(_translate("Dialog", "Статус"))
        self.CollectionLabel.setText(_translate("Dialog", "Коллекция"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.CollectionNameLabel.setText(_translate("Dialog", "Stellaris True Machine Translation Tool"))
        self.StringsList.setText(_translate("Dialog", "Продолжить последний перевод.Переименовать Коллекцию.Введите желаемое имя Коллекции"))
