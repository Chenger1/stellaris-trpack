# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from GUI.pictures import resources

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 860)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 860))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 860))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: #1f2533;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: transparent;")
        self.centralwidget.setObjectName("centralwidget")
        self.LocalizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.LocalizeButton.setGeometry(QtCore.QRect(20, 780, 231, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.LocalizeButton.setFont(font)
        self.LocalizeButton.setStyleSheet("QPushButton{\n"
"    background-color: #5abe41;\n"
"    border: 3px solid #5abe41;\n"
"    border-radius: 20px;\n"
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
        self.LocalizeButton.setObjectName("LocalizeButton")
        self.ModIDLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ModIDLine.setGeometry(QtCore.QRect(70, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.ModIDLine.setFont(font)
        self.ModIDLine.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    }")
        self.ModIDLine.setAlignment(QtCore.Qt.AlignCenter)
        self.ModIDLine.setReadOnly(True)
        self.ModIDLine.setObjectName("ModIDLine")
        self.OriginalLabel = QtWidgets.QLabel(self.centralwidget)
        self.OriginalLabel.setGeometry(QtCore.QRect(80, 360, 501, 20))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.OriginalLabel.setFont(font)
        self.OriginalLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"")
        self.OriginalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OriginalLabel.setObjectName("OriginalLabel")
        self.TranslatedLabel = QtWidgets.QLabel(self.centralwidget)
        self.TranslatedLabel.setGeometry(QtCore.QRect(710, 360, 501, 20))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.TranslatedLabel.setFont(font)
        self.TranslatedLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"")
        self.TranslatedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TranslatedLabel.setObjectName("TranslatedLabel")
        self.EditLabel = QtWidgets.QLabel(self.centralwidget)
        self.EditLabel.setGeometry(QtCore.QRect(370, 520, 551, 20))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.EditLabel.setFont(font)
        self.EditLabel.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    }")
        self.EditLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EditLabel.setObjectName("EditLabel")
        self.NextStringButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextStringButton.setGeometry(QtCore.QRect(940, 590, 231, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.NextStringButton.setFont(font)
        self.NextStringButton.setStyleSheet("QPushButton{\n"
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
        self.NextStringButton.setObjectName("NextStringButton")
        self.PreviousString = QtWidgets.QPushButton(self.centralwidget)
        self.PreviousString.setGeometry(QtCore.QRect(120, 590, 231, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.PreviousString.setFont(font)
        self.PreviousString.setStyleSheet("QPushButton{\n"
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
        self.PreviousString.setObjectName("PreviousString")
        self.stmtt_logo = QtWidgets.QLabel(self.centralwidget)
        self.stmtt_logo.setGeometry(QtCore.QRect(320, 60, 661, 121))
        self.stmtt_logo.setStyleSheet("background-color: none;\n"
"background-image: url(:/icons/icons/stmtt.png);")
        self.stmtt_logo.setText("")
        self.stmtt_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.stmtt_logo.setObjectName("stmtt_logo")
        self.TranslationLanguageButton = QtWidgets.QPushButton(self.centralwidget)
        self.TranslationLanguageButton.setGeometry(QtCore.QRect(1010, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.TranslationLanguageButton.setFont(font)
        self.TranslationLanguageButton.setStyleSheet("QPushButton{\n"
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
        self.TranslationLanguageButton.setObjectName("TranslationLanguageButton")
        self.SortModListButton = QtWidgets.QPushButton(self.centralwidget)
        self.SortModListButton.setGeometry(QtCore.QRect(270, 780, 181, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SortModListButton.setFont(font)
        self.SortModListButton.setStyleSheet("QPushButton{\n"
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
        self.SortModListButton.setObjectName("SortModListButton")
        self.OriginalString = QtWidgets.QTextEdit(self.centralwidget)
        self.OriginalString.setGeometry(QtCore.QRect(80, 400, 501, 91))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.OriginalString.setFont(font)
        self.OriginalString.setStyleSheet("QTextEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.OriginalString.setReadOnly(True)
        self.OriginalString.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.OriginalString.setObjectName("OriginalString")
        self.TranslateString = QtWidgets.QTextEdit(self.centralwidget)
        self.TranslateString.setGeometry(QtCore.QRect(710, 400, 501, 91))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.TranslateString.setFont(font)
        self.TranslateString.setStyleSheet("QTextEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.TranslateString.setReadOnly(True)
        self.TranslateString.setObjectName("TranslateString")
        self.EditString = QtWidgets.QTextEdit(self.centralwidget)
        self.EditString.setGeometry(QtCore.QRect(400, 560, 491, 91))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.EditString.setFont(font)
        self.EditString.setStyleSheet("QTextEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QTextEdit:hover{\n"
"    background-color: rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.EditString.setObjectName("EditString")
        self.BackgroundFrame = QtWidgets.QWidget(self.centralwidget)
        self.BackgroundFrame.setGeometry(QtCore.QRect(0, 0, 1300, 860))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(1300, 860))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(1300, 860))
        self.BackgroundFrame.setStyleSheet("background-color: none;\n"
"background-image: url(:/backgrounds/backgrounds/MainBackground.png);")
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.lang_logo = QtWidgets.QLabel(self.centralwidget)
        self.lang_logo.setGeometry(QtCore.QRect(1220, 30, 61, 51))
        self.lang_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/lang.png);")
        self.lang_logo.setText("")
        self.lang_logo.setPixmap(QtGui.QPixmap(":/background/lang.png"))
        self.lang_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lang_logo.setObjectName("lang_logo")
        self.StringOrder = QtWidgets.QLineEdit(self.centralwidget)
        self.StringOrder.setGeometry(QtCore.QRect(580, 400, 131, 91))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(20)
        self.StringOrder.setFont(font)
        self.StringOrder.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: transparent;\n"
"    }\n"
"")
        self.StringOrder.setAlignment(QtCore.Qt.AlignCenter)
        self.StringOrder.setReadOnly(True)
        self.StringOrder.setObjectName("StringOrder")
        self.ProgressBarFrame = QtWidgets.QFrame(self.centralwidget)
        self.ProgressBarFrame.setGeometry(QtCore.QRect(0, 0, 1300, 860))
        self.ProgressBarFrame.setMinimumSize(QtCore.QSize(1300, 860))
        self.ProgressBarFrame.setMaximumSize(QtCore.QSize(1300, 860))
        self.ProgressBarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProgressBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressBarFrame.setObjectName("ProgressBarFrame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1302, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.TopGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.TopGridLayout.setContentsMargins(0, 18, 0, 0)
        self.TopGridLayout.setSpacing(0)
        self.TopGridLayout.setObjectName("TopGridLayout")
        self.TprogressBar_L = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.TprogressBar_L.setMinimumSize(QtCore.QSize(650, 2))
        self.TprogressBar_L.setMaximumSize(QtCore.QSize(650, 2))
        self.TprogressBar_L.setSizeIncrement(QtCore.QSize(0, 0))
        self.TprogressBar_L.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-height:2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.TprogressBar_L.setProperty("value", 0)
        self.TprogressBar_L.setTextVisible(False)
        self.TprogressBar_L.setInvertedAppearance(False)
        self.TprogressBar_L.setObjectName("TprogressBar_L")
        self.TopGridLayout.addWidget(self.TprogressBar_L, 0, 0, 1, 1)
        self.TprogressBar_R = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.TprogressBar_R.setMinimumSize(QtCore.QSize(650, 2))
        self.TprogressBar_R.setMaximumSize(QtCore.QSize(650, 2))
        self.TprogressBar_R.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-height:2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 green , stop: 1 #05B8CC);\n"
"};")
        self.TprogressBar_R.setProperty("value", 0)
        self.TprogressBar_R.setTextVisible(False)
        self.TprogressBar_R.setInvertedAppearance(True)
        self.TprogressBar_R.setObjectName("TprogressBar_R")
        self.TopGridLayout.addWidget(self.TprogressBar_R, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 840, 1302, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.BottomGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.BottomGridLayout.setContentsMargins(0, 0, 0, 3)
        self.BottomGridLayout.setSpacing(0)
        self.BottomGridLayout.setObjectName("BottomGridLayout")
        self.BprogressBar_L = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.BprogressBar_L.setMinimumSize(QtCore.QSize(650, 2))
        self.BprogressBar_L.setMaximumSize(QtCore.QSize(650, 2))
        self.BprogressBar_L.setSizeIncrement(QtCore.QSize(0, 0))
        self.BprogressBar_L.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-height:2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.BprogressBar_L.setProperty("value", 0)
        self.BprogressBar_L.setTextVisible(False)
        self.BprogressBar_L.setInvertedAppearance(False)
        self.BprogressBar_L.setObjectName("BprogressBar_L")
        self.BottomGridLayout.addWidget(self.BprogressBar_L, 0, 0, 1, 1)
        self.BprogressBar_R = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.BprogressBar_R.setMinimumSize(QtCore.QSize(650, 2))
        self.BprogressBar_R.setMaximumSize(QtCore.QSize(650, 2))
        self.BprogressBar_R.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-height:2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 green , stop: 1 #05B8CC);\n"
"};")
        self.BprogressBar_R.setProperty("value", 0)
        self.BprogressBar_R.setTextVisible(False)
        self.BprogressBar_R.setInvertedAppearance(True)
        self.BprogressBar_R.setObjectName("BprogressBar_R")
        self.BottomGridLayout.addWidget(self.BprogressBar_R, 0, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 16, 948))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.LeftGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.LeftGridLayout.setContentsMargins(0, 24, 13, 88)
        self.LeftGridLayout.setSpacing(0)
        self.LeftGridLayout.setObjectName("LeftGridLayout")
        self.LprogressBar_T = QtWidgets.QProgressBar(self.gridLayoutWidget_5)
        self.LprogressBar_T.setMinimumSize(QtCore.QSize(2, 400))
        self.LprogressBar_T.setMaximumSize(QtCore.QSize(2, 417))
        self.LprogressBar_T.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.LprogressBar_T.setProperty("value", 0)
        self.LprogressBar_T.setTextVisible(False)
        self.LprogressBar_T.setOrientation(QtCore.Qt.Vertical)
        self.LprogressBar_T.setInvertedAppearance(True)
        self.LprogressBar_T.setObjectName("LprogressBar_T")
        self.LeftGridLayout.addWidget(self.LprogressBar_T, 0, 0, 1, 1)
        self.LprogressBar_B = QtWidgets.QProgressBar(self.gridLayoutWidget_5)
        self.LprogressBar_B.setMinimumSize(QtCore.QSize(2, 400))
        self.LprogressBar_B.setMaximumSize(QtCore.QSize(2, 417))
        self.LprogressBar_B.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 green, stop: 1#05B8CC);\n"
"};")
        self.LprogressBar_B.setProperty("value", 0)
        self.LprogressBar_B.setTextVisible(False)
        self.LprogressBar_B.setOrientation(QtCore.Qt.Vertical)
        self.LprogressBar_B.setInvertedAppearance(False)
        self.LprogressBar_B.setObjectName("LprogressBar_B")
        self.LeftGridLayout.addWidget(self.LprogressBar_B, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(1283, 0, 20, 948))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.RightGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.RightGridLayout.setContentsMargins(12, 24, 0, 88)
        self.RightGridLayout.setSpacing(0)
        self.RightGridLayout.setObjectName("RightGridLayout")
        self.RprogressBar_T = QtWidgets.QProgressBar(self.gridLayoutWidget_4)
        self.RprogressBar_T.setMinimumSize(QtCore.QSize(2, 400))
        self.RprogressBar_T.setMaximumSize(QtCore.QSize(2, 417))
        self.RprogressBar_T.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.RprogressBar_T.setProperty("value", 0)
        self.RprogressBar_T.setTextVisible(False)
        self.RprogressBar_T.setOrientation(QtCore.Qt.Vertical)
        self.RprogressBar_T.setInvertedAppearance(True)
        self.RprogressBar_T.setObjectName("RprogressBar_T")
        self.RightGridLayout.addWidget(self.RprogressBar_T, 0, 0, 1, 1)
        self.RprogressBar_B = QtWidgets.QProgressBar(self.gridLayoutWidget_4)
        self.RprogressBar_B.setMinimumSize(QtCore.QSize(2, 400))
        self.RprogressBar_B.setMaximumSize(QtCore.QSize(2, 417))
        self.RprogressBar_B.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 2px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 green, stop: 1#05B8CC);\n"
"};")
        self.RprogressBar_B.setProperty("value", 0)
        self.RprogressBar_B.setTextVisible(False)
        self.RprogressBar_B.setOrientation(QtCore.Qt.Vertical)
        self.RprogressBar_B.setInvertedAppearance(False)
        self.RprogressBar_B.setObjectName("RprogressBar_B")
        self.RightGridLayout.addWidget(self.RprogressBar_B, 1, 0, 1, 1)
        self.WindowMoveButton = QtWidgets.QPushButton(self.centralwidget)
        self.WindowMoveButton.setGeometry(QtCore.QRect(-10, 0, 1311, 21))
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
        self.RollUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.RollUpButton.setGeometry(QtCore.QRect(1250, 0, 20, 21))
        self.RollUpButton.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
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
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(1270, 0, 21, 21))
        self.ExitButton.setMinimumSize(QtCore.QSize(20, 20))
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
        self.ReferenceButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReferenceButton.setGeometry(QtCore.QRect(1100, 780, 171, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ReferenceButton.setFont(font)
        self.ReferenceButton.setStyleSheet("QPushButton{\n"
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
        self.ReferenceButton.setObjectName("ReferenceButton")
        self.paradox_logo = QtWidgets.QLabel(self.centralwidget)
        self.paradox_logo.setGeometry(QtCore.QRect(20, 30, 61, 51))
        self.paradox_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/paradox.png);")
        self.paradox_logo.setText("")
        self.paradox_logo.setPixmap(QtGui.QPixmap(":/background/lang.png"))
        self.paradox_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.paradox_logo.setObjectName("paradox_logo")
        self.ToolLanguageButton = QtWidgets.QPushButton(self.centralwidget)
        self.ToolLanguageButton.setGeometry(QtCore.QRect(1090, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ToolLanguageButton.setFont(font)
        self.ToolLanguageButton.setStyleSheet("QPushButton{\n"
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
        self.ToolLanguageButton.setObjectName("ToolLanguageButton")
        self.ModNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ModNameLine.setGeometry(QtCore.QRect(0, 200, 1301, 121))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(14)
        self.ModNameLine.setFont(font)
        self.ModNameLine.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    }")
        self.ModNameLine.setText("")
        self.ModNameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.ModNameLine.setReadOnly(True)
        self.ModNameLine.setObjectName("ModNameLine")
        self.FinishButton = QtWidgets.QPushButton(self.centralwidget)
        self.FinishButton.setGeometry(QtCore.QRect(20, 780, 231, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.FinishButton.setFont(font)
        self.FinishButton.setStyleSheet("QPushButton{\n"
"    background-color: #5abe41;\n"
"    border: 3px solid #5abe41;\n"
"    border-radius: 20px;\n"
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
        self.FinishButton.setObjectName("FinishButton")
        self.CollectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.CollectionButton.setGeometry(QtCore.QRect(40, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.CollectionButton.setFont(font)
        self.CollectionButton.setStyleSheet("QPushButton{\n"
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
        self.CollectionButton.setObjectName("CollectionButton")
        self.ManualButton = QtWidgets.QPushButton(self.centralwidget)
        self.ManualButton.setGeometry(QtCore.QRect(50, 151, 121, 27))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ManualButton.setFont(font)
        self.ManualButton.setStyleSheet("QPushButton{\n"
"    background-color: rgba(194, 194, 194, 50);\n"
"    border: #c2c2c2;\n"
"    border-radius: 13px;\n"
"    min-height: 27px;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #31858f;\n"
"    border: #31858f;\n"
"    color: #ffffff;\n"
"    }\n"
"QPushButton:pressed{\n"
"    background-color: #05B8CC;\n"
"    border: 2px solid #05B8CC;\n"
"    }")
        self.ManualButton.setObjectName("ManualButton")
        self.FileNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.FileNameLine.setGeometry(QtCore.QRect(490, 810, 561, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        self.FileNameLine.setFont(font)
        self.FileNameLine.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    border: transparent;\n"
"    color: #ffffff;\n"
"    }")
        self.FileNameLine.setText("")
        self.FileNameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.FileNameLine.setReadOnly(True)
        self.FileNameLine.setObjectName("FileNameLine")
        self.steam_logo = QtWidgets.QLabel(self.centralwidget)
        self.steam_logo.setGeometry(QtCore.QRect(20, 30, 61, 51))
        self.steam_logo.setStyleSheet("background-color: none;")
        self.steam_logo.setText("")
        self.steam_logo.setPixmap(QtGui.QPixmap(":/icons/icons/steam.png"))
        self.steam_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo.setObjectName("steam_logo")
        self.BackgroundFrame.raise_()
        self.lang_logo.raise_()
        self.ProgressBarFrame.raise_()
        self.ModIDLine.raise_()
        self.OriginalLabel.raise_()
        self.TranslatedLabel.raise_()
        self.EditLabel.raise_()
        self.NextStringButton.raise_()
        self.PreviousString.raise_()
        self.stmtt_logo.raise_()
        self.TranslationLanguageButton.raise_()
        self.SortModListButton.raise_()
        self.OriginalString.raise_()
        self.TranslateString.raise_()
        self.EditString.raise_()
        self.StringOrder.raise_()
        self.WindowMoveButton.raise_()
        self.RollUpButton.raise_()
        self.ExitButton.raise_()
        self.ReferenceButton.raise_()
        self.paradox_logo.raise_()
        self.ToolLanguageButton.raise_()
        self.ModNameLine.raise_()
        self.FinishButton.raise_()
        self.LocalizeButton.raise_()
        self.CollectionButton.raise_()
        self.ManualButton.raise_()
        self.steam_logo.raise_()
        self.FileNameLine.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stellaris True Machine Translation Tool"))
        self.LocalizeButton.setText(_translate("MainWindow", "Локализировать"))
        self.ModIDLine.setText(_translate("MainWindow", "SteamWorkshop ID"))
        self.OriginalLabel.setText(_translate("MainWindow", "Оригинальная строка"))
        self.TranslatedLabel.setText(_translate("MainWindow", "Машинный перевод"))
        self.EditLabel.setText(_translate("MainWindow", "Можно заменить машинный перевод на свой вариант"))
        self.NextStringButton.setText(_translate("MainWindow", "Следующая строка"))
        self.PreviousString.setText(_translate("MainWindow", "Предыдущая строка"))
        self.TranslationLanguageButton.setText(_translate("MainWindow", "Язык перевода"))
        self.SortModListButton.setText(_translate("MainWindow", "Модификации"))
        self.OriginalString.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.TranslateString.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.EditString.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'KB Astrolyte\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.StringOrder.setText(_translate("MainWindow", "0"))
        self.WindowMoveButton.setText(_translate("MainWindow", "Steam"))
        self.RollUpButton.setText(_translate("MainWindow", "_"))
        self.ExitButton.setText(_translate("MainWindow", "X"))
        self.ReferenceButton.setText(_translate("MainWindow", "Справка"))
        self.ToolLanguageButton.setText(_translate("MainWindow", "Интерфейс"))
        self.FinishButton.setText(_translate("MainWindow", "Сохранить перевод"))
        self.CollectionButton.setText(_translate("MainWindow", "Коллекция"))
        self.ManualButton.setText(_translate("MainWindow", "Вручную"))
