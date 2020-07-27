# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MoreOutputLanguage.ui'
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 626, 1122))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 150, -1, 150)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.SlovakButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SlovakButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SlovakButton.setFont(font)
        self.SlovakButton.setStyleSheet("QPushButton{\n"
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
        self.SlovakButton.setObjectName("SlovakButton")
        self.gridLayout.addWidget(self.SlovakButton, 9, 2, 1, 1)
        self.KoreanButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.KoreanButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.KoreanButton.setFont(font)
        self.KoreanButton.setStyleSheet("QPushButton{\n"
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
        self.KoreanButton.setObjectName("KoreanButton")
        self.gridLayout.addWidget(self.KoreanButton, 7, 0, 1, 1)
        self.RussianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.RussianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.RussianButton.setFont(font)
        self.RussianButton.setStyleSheet("QPushButton{\n"
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
        self.RussianButton.setObjectName("RussianButton")
        self.gridLayout.addWidget(self.RussianButton, 9, 0, 1, 1)
        self.PolishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.PolishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PolishButton.setFont(font)
        self.PolishButton.setStyleSheet("QPushButton{\n"
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
        self.PolishButton.setObjectName("PolishButton")
        self.gridLayout.addWidget(self.PolishButton, 8, 0, 1, 1)
        self.PortugueseButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.PortugueseButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.PortugueseButton.setFont(font)
        self.PortugueseButton.setStyleSheet("QPushButton{\n"
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
        self.PortugueseButton.setObjectName("PortugueseButton")
        self.gridLayout.addWidget(self.PortugueseButton, 8, 1, 1, 1)
        self.SpanishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SpanishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SpanishButton.setFont(font)
        self.SpanishButton.setStyleSheet("QPushButton{\n"
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
        self.SpanishButton.setObjectName("SpanishButton")
        self.gridLayout.addWidget(self.SpanishButton, 10, 1, 1, 1)
        self.CzechButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CzechButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CzechButton.setFont(font)
        self.CzechButton.setStyleSheet("QPushButton{\n"
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
        self.CzechButton.setObjectName("CzechButton")
        self.gridLayout.addWidget(self.CzechButton, 3, 1, 1, 1)
        self.FinnishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.FinnishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.FinnishButton.setFont(font)
        self.FinnishButton.setStyleSheet("QPushButton{\n"
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
        self.FinnishButton.setObjectName("FinnishButton")
        self.gridLayout.addWidget(self.FinnishButton, 4, 1, 1, 1)
        self.ItalianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ItalianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ItalianButton.setFont(font)
        self.ItalianButton.setStyleSheet("QPushButton{\n"
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
        self.ItalianButton.setObjectName("ItalianButton")
        self.gridLayout.addWidget(self.ItalianButton, 6, 1, 1, 1)
        self.FrenchButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.FrenchButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.FrenchButton.setFont(font)
        self.FrenchButton.setStyleSheet("QPushButton{\n"
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
        self.FrenchButton.setObjectName("FrenchButton")
        self.gridLayout.addWidget(self.FrenchButton, 4, 2, 1, 1)
        self.DanishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.DanishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DanishButton.setFont(font)
        self.DanishButton.setStyleSheet("QPushButton{\n"
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
        self.DanishButton.setObjectName("DanishButton")
        self.gridLayout.addWidget(self.DanishButton, 0, 2, 1, 1)
        self.ArmenianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ArmenianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ArmenianButton.setFont(font)
        self.ArmenianButton.setStyleSheet("QPushButton{\n"
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
        self.ArmenianButton.setObjectName("ArmenianButton")
        self.gridLayout.addWidget(self.ArmenianButton, 0, 1, 1, 1)
        self.EnglishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.EnglishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.EnglishButton.setFont(font)
        self.EnglishButton.setStyleSheet("QPushButton{\n"
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
        self.EnglishButton.setObjectName("EnglishButton")
        self.gridLayout.addWidget(self.EnglishButton, 2, 2, 1, 1)
        self.UkrainianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.UkrainianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.UkrainianButton.setFont(font)
        self.UkrainianButton.setStyleSheet("QPushButton{\n"
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
        self.UkrainianButton.setObjectName("UkrainianButton")
        self.gridLayout.addWidget(self.UkrainianButton, 11, 1, 1, 1)
        self.EstonianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.EstonianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.EstonianButton.setFont(font)
        self.EstonianButton.setStyleSheet("QPushButton{\n"
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
        self.EstonianButton.setObjectName("EstonianButton")
        self.gridLayout.addWidget(self.EstonianButton, 3, 2, 1, 1)
        self.LithuanianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.LithuanianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LithuanianButton.setFont(font)
        self.LithuanianButton.setStyleSheet("QPushButton{\n"
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
        self.LithuanianButton.setObjectName("LithuanianButton")
        self.gridLayout.addWidget(self.LithuanianButton, 7, 1, 1, 1)
        self.ChineseButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ChineseButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ChineseButton.setFont(font)
        self.ChineseButton.setStyleSheet("QPushButton{\n"
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
        self.ChineseButton.setObjectName("ChineseButton")
        self.gridLayout.addWidget(self.ChineseButton, 2, 1, 1, 1)
        self.HungarianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.HungarianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.HungarianButton.setFont(font)
        self.HungarianButton.setStyleSheet("QPushButton{\n"
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
        self.HungarianButton.setObjectName("HungarianButton")
        self.gridLayout.addWidget(self.HungarianButton, 5, 2, 1, 1)
        self.GreekButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.GreekButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.GreekButton.setFont(font)
        self.GreekButton.setStyleSheet("QPushButton{\n"
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
        self.GreekButton.setObjectName("GreekButton")
        self.gridLayout.addWidget(self.GreekButton, 5, 1, 1, 1)
        self.TurkishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.TurkishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TurkishButton.setFont(font)
        self.TurkishButton.setStyleSheet("QPushButton{\n"
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
        self.TurkishButton.setObjectName("TurkishButton")
        self.gridLayout.addWidget(self.TurkishButton, 11, 0, 1, 1)
        self.DutchButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.DutchButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DutchButton.setFont(font)
        self.DutchButton.setStyleSheet("QPushButton{\n"
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
        self.DutchButton.setObjectName("DutchButton")
        self.gridLayout.addWidget(self.DutchButton, 1, 2, 1, 1)
        self.IcelandicButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.IcelandicButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.IcelandicButton.setFont(font)
        self.IcelandicButton.setStyleSheet("QPushButton{\n"
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
        self.IcelandicButton.setObjectName("IcelandicButton")
        self.gridLayout.addWidget(self.IcelandicButton, 6, 0, 1, 1)
        self.BelarusianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.BelarusianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BelarusianButton.setFont(font)
        self.BelarusianButton.setStyleSheet("QPushButton{\n"
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
        self.BelarusianButton.setObjectName("BelarusianButton")
        self.gridLayout.addWidget(self.BelarusianButton, 1, 1, 1, 1)
        self.AzerbaijaniButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.AzerbaijaniButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AzerbaijaniButton.setFont(font)
        self.AzerbaijaniButton.setStyleSheet("QPushButton{\n"
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
        self.AzerbaijaniButton.setObjectName("AzerbaijaniButton")
        self.gridLayout.addWidget(self.AzerbaijaniButton, 1, 0, 1, 1)
        self.SlovenianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SlovenianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SlovenianButton.setFont(font)
        self.SlovenianButton.setStyleSheet("QPushButton{\n"
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
        self.SlovenianButton.setObjectName("SlovenianButton")
        self.gridLayout.addWidget(self.SlovenianButton, 10, 0, 1, 1)
        self.FilipinoButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.FilipinoButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.FilipinoButton.setFont(font)
        self.FilipinoButton.setStyleSheet("QPushButton{\n"
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
        self.FilipinoButton.setObjectName("FilipinoButton")
        self.gridLayout.addWidget(self.FilipinoButton, 11, 2, 1, 1)
        self.NorwegianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.NorwegianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.NorwegianButton.setFont(font)
        self.NorwegianButton.setStyleSheet("QPushButton{\n"
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
        self.NorwegianButton.setObjectName("NorwegianButton")
        self.gridLayout.addWidget(self.NorwegianButton, 7, 2, 1, 1)
        self.ArabicButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ArabicButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ArabicButton.setFont(font)
        self.ArabicButton.setStyleSheet("QPushButton{\n"
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
        self.ArabicButton.setObjectName("ArabicButton")
        self.gridLayout.addWidget(self.ArabicButton, 0, 0, 1, 1)
        self.BulgarianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.BulgarianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BulgarianButton.setFont(font)
        self.BulgarianButton.setStyleSheet("QPushButton{\n"
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
        self.BulgarianButton.setObjectName("BulgarianButton")
        self.gridLayout.addWidget(self.BulgarianButton, 2, 0, 1, 1)
        self.JapaneseButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.JapaneseButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.JapaneseButton.setFont(font)
        self.JapaneseButton.setStyleSheet("QPushButton{\n"
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
        self.JapaneseButton.setObjectName("JapaneseButton")
        self.gridLayout.addWidget(self.JapaneseButton, 6, 2, 1, 1)
        self.GermanButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.GermanButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.GermanButton.setFont(font)
        self.GermanButton.setStyleSheet("QPushButton{\n"
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
        self.GermanButton.setObjectName("GermanButton")
        self.gridLayout.addWidget(self.GermanButton, 5, 0, 1, 1)
        self.SwedishButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SwedishButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SwedishButton.setFont(font)
        self.SwedishButton.setStyleSheet("QPushButton{\n"
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
        self.SwedishButton.setObjectName("SwedishButton")
        self.gridLayout.addWidget(self.SwedishButton, 10, 2, 1, 1)
        self.RomanianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.RomanianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.RomanianButton.setFont(font)
        self.RomanianButton.setStyleSheet("QPushButton{\n"
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
        self.RomanianButton.setObjectName("RomanianButton")
        self.gridLayout.addWidget(self.RomanianButton, 8, 2, 1, 1)
        self.CroatianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CroatianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.CroatianButton.setFont(font)
        self.CroatianButton.setStyleSheet("QPushButton{\n"
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
        self.CroatianButton.setObjectName("CroatianButton")
        self.gridLayout.addWidget(self.CroatianButton, 3, 0, 1, 1)
        self.SerbianButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SerbianButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SerbianButton.setFont(font)
        self.SerbianButton.setStyleSheet("QPushButton{\n"
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
        self.SerbianButton.setObjectName("SerbianButton")
        self.gridLayout.addWidget(self.SerbianButton, 9, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.LandingArea.setWidget(self.scrollAreaWidgetContents)
        self.SearchLine = QtWidgets.QLineEdit(Dialog)
        self.SearchLine.setGeometry(QtCore.QRect(340, 50, 261, 31))
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
        self.SearchLine.raise_()
        self.BottomShadowFrame.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ExitButton.setText(_translate("Dialog", "X"))
        self.RollUpButton.setText(_translate("Dialog", "_"))
        self.ReferenceButton.setText(_translate("Dialog", "?"))
        self.LanguagesListLabel.setText(_translate("Dialog", "Список языков"))
        self.SlovakButton.setText(_translate("Dialog", "Словацкий"))
        self.KoreanButton.setText(_translate("Dialog", "Корейский"))
        self.RussianButton.setText(_translate("Dialog", "Русский"))
        self.PolishButton.setText(_translate("Dialog", "Польский"))
        self.PortugueseButton.setText(_translate("Dialog", "Португальский"))
        self.SpanishButton.setText(_translate("Dialog", "Испанский"))
        self.CzechButton.setText(_translate("Dialog", "Чешский"))
        self.FinnishButton.setText(_translate("Dialog", "Финский"))
        self.ItalianButton.setText(_translate("Dialog", "Итальянский"))
        self.FrenchButton.setText(_translate("Dialog", "Французский"))
        self.DanishButton.setText(_translate("Dialog", "Датский"))
        self.ArmenianButton.setText(_translate("Dialog", "Армянский"))
        self.EnglishButton.setText(_translate("Dialog", "Английский"))
        self.UkrainianButton.setText(_translate("Dialog", "Украинский"))
        self.EstonianButton.setText(_translate("Dialog", "Эстонский"))
        self.LithuanianButton.setText(_translate("Dialog", "Литовский"))
        self.ChineseButton.setText(_translate("Dialog", "Китайский"))
        self.HungarianButton.setText(_translate("Dialog", "Венгерский"))
        self.GreekButton.setText(_translate("Dialog", "Греческий"))
        self.TurkishButton.setText(_translate("Dialog", "Турецкий"))
        self.DutchButton.setText(_translate("Dialog", "Нидерландский"))
        self.IcelandicButton.setText(_translate("Dialog", "Исландский"))
        self.BelarusianButton.setText(_translate("Dialog", "Белорусский"))
        self.AzerbaijaniButton.setText(_translate("Dialog", "Азербайджанский"))
        self.SlovenianButton.setText(_translate("Dialog", "Словенский"))
        self.FilipinoButton.setText(_translate("Dialog", "Филиппинский"))
        self.NorwegianButton.setText(_translate("Dialog", "Норвежский"))
        self.ArabicButton.setText(_translate("Dialog", "Арабский"))
        self.BulgarianButton.setText(_translate("Dialog", "Болгарский"))
        self.JapaneseButton.setText(_translate("Dialog", "Японский"))
        self.GermanButton.setText(_translate("Dialog", "Немецкий"))
        self.SwedishButton.setText(_translate("Dialog", "Шведский"))
        self.RomanianButton.setText(_translate("Dialog", "Румынский"))
        self.CroatianButton.setText(_translate("Dialog", "Хорватский"))
        self.SerbianButton.setText(_translate("Dialog", "Сербский"))
        self.SearchLine.setText(_translate("Dialog", "Поиск"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
from GUI.pictures import resources
