# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


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
        icon.addPixmap(QtGui.QPixmap("pictures/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #1f2533;\n"
"background-image: url(\'pictures/background.png\')")
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
        self.SteamButton = QtWidgets.QPushButton(self.centralwidget)
        self.SteamButton.setGeometry(QtCore.QRect(30, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SteamButton.setFont(font)
        self.SteamButton.setStyleSheet("QPushButton{\n"
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
        self.SteamButton.setObjectName("SteamButton")
        self.ModIDLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ModIDLine.setGeometry(QtCore.QRect(430, 290, 431, 21))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.ModIDLine.setFont(font)
        self.ModIDLine.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(31, 37, 51, 50);\n"
"    border: 1px solid #ffffff;\n"
"    color: #ffffff;\n"
"    }\n"
"QLineEdit:hover{\n"
"    background-color: #rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.ModIDLine.setAlignment(QtCore.Qt.AlignCenter)
        self.ModIDLine.setReadOnly(True)
        self.ModIDLine.setObjectName("ModIDLine")
        self.FileSelectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.FileSelectionButton.setGeometry(QtCore.QRect(560, 240, 171, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.FileSelectionButton.setFont(font)
        self.FileSelectionButton.setStyleSheet("QPushButton{\n"
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
        self.FileSelectionButton.setObjectName("FileSelectionButton")
        self.OriginalLabel = QtWidgets.QLabel(self.centralwidget)
        self.OriginalLabel.setGeometry(QtCore.QRect(80, 360, 501, 20))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(9)
        self.OriginalLabel.setFont(font)
        self.OriginalLabel.setStyleSheet("QLabel{\n"
"    background-color: none;\n"
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
"    background-color: none;\n"
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
"    background-color: none;\n"
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
        self.ToolLanguageButton = QtWidgets.QPushButton(self.centralwidget)
        self.ToolLanguageButton.setGeometry(QtCore.QRect(1060, 50, 211, 31))
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
        self.OutputLanguageButton = QtWidgets.QPushButton(self.centralwidget)
        self.OutputLanguageButton.setGeometry(QtCore.QRect(1030, 90, 241, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.OutputLanguageButton.setFont(font)
        self.OutputLanguageButton.setStyleSheet("QPushButton{\n"
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
        self.OutputLanguageButton.setObjectName("OutputLanguageButton")
        self.ReferenceButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReferenceButton.setGeometry(QtCore.QRect(1080, 780, 141, 41))
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
        self.SortModListButton = QtWidgets.QPushButton(self.centralwidget)
        self.SortModListButton.setGeometry(QtCore.QRect(30, 90, 241, 31))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SortModListButton.setFont(font)
        self.SortModListButton.setStyleSheet("QPushButton{\n"
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
"    background-color: #rgba(56, 57, 61, 50);\n"
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
"    background-color: #rgba(56, 57, 61, 50);\n"
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
"    background-color: #rgba(56, 57, 61, 50);\n"
"    }\n"
"")
        self.EditString.setObjectName("EditString")
        self.ShareButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShareButton.setGeometry(QtCore.QRect(280, 780, 181, 41))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ShareButton.setFont(font)
        self.ShareButton.setStyleSheet("QPushButton{\n"
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
        self.ShareButton.setObjectName("ShareButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(1270, 0, 21, 21))
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
        self.RollUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.RollUpButton.setGeometry(QtCore.QRect(1250, 0, 21, 21))
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
        self.BackgroundFrame = QtWidgets.QWidget(self.centralwidget)
        self.BackgroundFrame.setGeometry(QtCore.QRect(0, 0, 1300, 860))
        self.BackgroundFrame.setMinimumSize(QtCore.QSize(1300, 860))
        self.BackgroundFrame.setMaximumSize(QtCore.QSize(1300, 860))
        self.BackgroundFrame.setStyleSheet("background-color: none;\n"
"background-image: url(:/backgrounds/backgrounds/MainBackground.png);")
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.steam_logo = QtWidgets.QLabel(self.centralwidget)
        self.steam_logo.setGeometry(QtCore.QRect(250, 40, 41, 41))
        self.steam_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/steam.png);\n"
"")
        self.steam_logo.setText("")
        self.steam_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.steam_logo.setObjectName("steam_logo")
        self.lang_logo = QtWidgets.QLabel(self.centralwidget)
        self.lang_logo.setGeometry(QtCore.QRect(1010, 40, 41, 41))
        self.lang_logo.setStyleSheet("background-color: none;\n"
"image: url(:/icons/icons/lang.png);")
        self.lang_logo.setText("")
        self.lang_logo.setPixmap(QtGui.QPixmap(":/background/lang.png"))
        self.lang_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lang_logo.setObjectName("lang_logo")
        self.StringOrder = QtWidgets.QLineEdit(self.centralwidget)
        self.StringOrder.setGeometry(QtCore.QRect(580, 400, 131, 91))
        font = QtGui.QFont()
        font.setFamily("AnyNumber_Cyrillic")
        font.setPointSize(22)
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
        self.ProgressBarFrame.setGeometry(QtCore.QRect(0, 0, 1301, 861))
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
        self.TprogressBar_L.setProperty("value", 24)
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
        self.TprogressBar_R.setProperty("value", 24)
        self.TprogressBar_R.setTextVisible(False)
        self.TprogressBar_R.setInvertedAppearance(True)
        self.TprogressBar_R.setObjectName("TprogressBar_R")
        self.TopGridLayout.addWidget(self.TprogressBar_R, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 840, 1302, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.BottomGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.BottomGridLayout.setContentsMargins(0, 0, 0, 4)
        self.BottomGridLayout.setSpacing(0)
        self.BottomGridLayout.setObjectName("BottomGridLayout")
        self.BprogressBar_L = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.BprogressBar_L.setMinimumSize(QtCore.QSize(650, 2))
        self.BprogressBar_L.setMaximumSize(QtCore.QSize(650, 2))
        self.BprogressBar_L.setSizeIncrement(QtCore.QSize(0, 0))
        self.BprogressBar_L.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-height:3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.BprogressBar_L.setProperty("value", 24)
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
"    max-height: 3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 green , stop: 1 #05B8CC);\n"
"};")
        self.BprogressBar_R.setProperty("value", 24)
        self.BprogressBar_R.setTextVisible(False)
        self.BprogressBar_R.setInvertedAppearance(True)
        self.BprogressBar_R.setObjectName("BprogressBar_R")
        self.BottomGridLayout.addWidget(self.BprogressBar_R, 0, 1, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 16, 948))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.LeftGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.LeftGridLayout.setContentsMargins(0, 16, 12, 70)
        self.LeftGridLayout.setSpacing(0)
        self.LeftGridLayout.setObjectName("LeftGridLayout")
        self.LprogressBar_T = QtWidgets.QProgressBar(self.gridLayoutWidget_5)
        self.LprogressBar_T.setMinimumSize(QtCore.QSize(2, 400))
        self.LprogressBar_T.setMaximumSize(QtCore.QSize(2, 420))
        self.LprogressBar_T.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.LprogressBar_T.setProperty("value", 24)
        self.LprogressBar_T.setTextVisible(False)
        self.LprogressBar_T.setOrientation(QtCore.Qt.Vertical)
        self.LprogressBar_T.setInvertedAppearance(True)
        self.LprogressBar_T.setObjectName("LprogressBar_T")
        self.LeftGridLayout.addWidget(self.LprogressBar_T, 0, 0, 1, 1)
        self.LprogressBar_B = QtWidgets.QProgressBar(self.gridLayoutWidget_5)
        self.LprogressBar_B.setMinimumSize(QtCore.QSize(2, 400))
        self.LprogressBar_B.setMaximumSize(QtCore.QSize(2, 420))
        self.LprogressBar_B.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 green, stop: 1#05B8CC);\n"
"};")
        self.LprogressBar_B.setProperty("value", 24)
        self.LprogressBar_B.setTextVisible(False)
        self.LprogressBar_B.setOrientation(QtCore.Qt.Vertical)
        self.LprogressBar_B.setInvertedAppearance(False)
        self.LprogressBar_B.setObjectName("LprogressBar_B")
        self.LeftGridLayout.addWidget(self.LprogressBar_B, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.ProgressBarFrame)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(1283, 0, 20, 948))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.RightGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.RightGridLayout.setContentsMargins(12, 16, 0, 70)
        self.RightGridLayout.setSpacing(0)
        self.RightGridLayout.setObjectName("RightGridLayout")
        self.RprogressBar_T = QtWidgets.QProgressBar(self.gridLayoutWidget_4)
        self.RprogressBar_T.setMinimumSize(QtCore.QSize(2, 400))
        self.RprogressBar_T.setMaximumSize(QtCore.QSize(2, 420))
        self.RprogressBar_T.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 #05B8CC, stop: 1 green);\n"
"};")
        self.RprogressBar_T.setProperty("value", 24)
        self.RprogressBar_T.setTextVisible(False)
        self.RprogressBar_T.setOrientation(QtCore.Qt.Vertical)
        self.RprogressBar_T.setInvertedAppearance(True)
        self.RprogressBar_T.setObjectName("RprogressBar_T")
        self.RightGridLayout.addWidget(self.RprogressBar_T, 0, 0, 1, 1)
        self.RprogressBar_B = QtWidgets.QProgressBar(self.gridLayoutWidget_4)
        self.RprogressBar_B.setMinimumSize(QtCore.QSize(2, 400))
        self.RprogressBar_B.setMaximumSize(QtCore.QSize(2, 420))
        self.RprogressBar_B.setStyleSheet("QProgressBar {\n"
"    background-color: transparent;\n"
"    border: 0px solid gray; \n"
"    max-width: 3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 green, stop: 1#05B8CC);\n"
"};")
        self.RprogressBar_B.setProperty("value", 24)
        self.RprogressBar_B.setTextVisible(False)
        self.RprogressBar_B.setOrientation(QtCore.Qt.Vertical)
        self.RprogressBar_B.setInvertedAppearance(False)
        self.RprogressBar_B.setObjectName("RprogressBar_B")
        self.RightGridLayout.addWidget(self.RprogressBar_B, 1, 0, 1, 1)
        self.BackgroundFrame.raise_()
        self.ProgressBarFrame.raise_()
        self.LocalizeButton.raise_()
        self.SteamButton.raise_()
        self.ModIDLine.raise_()
        self.FileSelectionButton.raise_()
        self.OriginalLabel.raise_()
        self.TranslatedLabel.raise_()
        self.EditLabel.raise_()
        self.NextStringButton.raise_()
        self.PreviousString.raise_()
        self.stmtt_logo.raise_()
        self.ToolLanguageButton.raise_()
        self.OutputLanguageButton.raise_()
        self.ReferenceButton.raise_()
        self.SortModListButton.raise_()
        self.OriginalString.raise_()
        self.TranslateString.raise_()
        self.EditString.raise_()
        self.ShareButton.raise_()
        self.ExitButton.raise_()
        self.RollUpButton.raise_()
        self.steam_logo.raise_()
        self.lang_logo.raise_()
        self.StringOrder.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stellaris True Machine Translation Tool"))
        self.LocalizeButton.setText(_translate("MainWindow", "Локализировать"))
        self.SteamButton.setText(_translate("MainWindow", "Steam"))
        self.FileSelectionButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.OriginalLabel.setText(_translate("MainWindow", "Оригинальная строка"))
        self.TranslatedLabel.setText(_translate("MainWindow", "Машинный перевод"))
        self.EditLabel.setText(_translate("MainWindow", "Можно заменить машинный перевод на свой вариант"))
        self.NextStringButton.setText(_translate("MainWindow", "Следующая строка"))
        self.PreviousString.setText(_translate("MainWindow", "Предыдущая строка"))
        self.ToolLanguageButton.setText(_translate("MainWindow", "Язык утилиты"))
        self.OutputLanguageButton.setText(_translate("MainWindow", "Выходной язык"))
        self.ReferenceButton.setText(_translate("MainWindow", "Справка"))
        self.SortModListButton.setText(_translate("MainWindow", "Сортировать моды"))
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
        self.ShareButton.setText(_translate("MainWindow", "Опубликовать"))
        self.ExitButton.setText(_translate("MainWindow", "X"))
        self.RollUpButton.setText(_translate("MainWindow", "_"))
        self.StringOrder.setText(_translate("MainWindow", "0"))
from GUI.pictures import resources