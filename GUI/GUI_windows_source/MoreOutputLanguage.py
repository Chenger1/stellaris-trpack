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
        Dialog.resize(650, 376)
        Dialog.setMinimumSize(QtCore.QSize(650, 375))
        Dialog.setMaximumSize(QtCore.QSize(650, 380))
        Dialog.setStyleSheet("background-color: transparent;\n"
"")
        self.lang_logo = QtWidgets.QLabel(Dialog)
        self.lang_logo.setGeometry(QtCore.QRect(10, 20, 61, 51))
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
        self.LanguagesListLabel.setGeometry(QtCore.QRect(50, 40, 231, 41))
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
        self.tl = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tl.setFont(font)
        self.tl.setStyleSheet("QPushButton{\n"
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
        self.tl.setObjectName("tl")
        self.gridLayout.addWidget(self.tl, 4, 0, 1, 1)
        self.et = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.et.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.et.setFont(font)
        self.et.setStyleSheet("QPushButton{\n"
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
        self.et.setObjectName("et")
        self.gridLayout.addWidget(self.et, 3, 2, 1, 1)
        self.cn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cn.setFont(font)
        self.cn.setStyleSheet("QPushButton{\n"
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
        self.cn.setObjectName("cn")
        self.gridLayout.addWidget(self.cn, 2, 1, 1, 1)
        self.ro = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ro.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ro.setFont(font)
        self.ro.setStyleSheet("QPushButton{\n"
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
        self.ro.setObjectName("ro")
        self.gridLayout.addWidget(self.ro, 8, 2, 1, 1)
        self.be = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.be.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.be.setFont(font)
        self.be.setStyleSheet("QPushButton{\n"
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
        self.be.setObjectName("be")
        self.gridLayout.addWidget(self.be, 1, 1, 1, 1)
        self.fil = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.fil.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fil.setFont(font)
        self.fil.setStyleSheet("QPushButton{\n"
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
        self.fil.setObjectName("fil")
        self.gridLayout.addWidget(self.fil, 11, 2, 1, 1)
        self.el = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.el.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.el.setFont(font)
        self.el.setStyleSheet("QPushButton{\n"
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
        self.el.setObjectName("el")
        self.gridLayout.addWidget(self.el, 5, 1, 1, 1)
        self.de = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.de.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.de.setFont(font)
        self.de.setStyleSheet("QPushButton{\n"
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
        self.de.setObjectName("de")
        self.gridLayout.addWidget(self.de, 5, 0, 1, 1)
        self.ar = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ar.setFont(font)
        self.ar.setStyleSheet("QPushButton{\n"
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
        self.ar.setObjectName("ar")
        self.gridLayout.addWidget(self.ar, 0, 0, 1, 1)
        self.cs = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cs.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cs.setFont(font)
        self.cs.setStyleSheet("QPushButton{\n"
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
        self.cs.setObjectName("cs")
        self.gridLayout.addWidget(self.cs, 3, 1, 1, 1)
        self.pt = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pt.setFont(font)
        self.pt.setStyleSheet("QPushButton{\n"
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
        self.pt.setObjectName("pt")
        self.gridLayout.addWidget(self.pt, 8, 1, 1, 1)
        self.hu = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.hu.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hu.setFont(font)
        self.hu.setStyleSheet("QPushButton{\n"
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
        self.hu.setObjectName("hu")
        self.gridLayout.addWidget(self.hu, 5, 2, 1, 1)
        self.pl = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pl.setFont(font)
        self.pl.setStyleSheet("QPushButton{\n"
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
        self.pl.setObjectName("pl")
        self.gridLayout.addWidget(self.pl, 8, 0, 1, 1)
        self.uk = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.uk.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.uk.setFont(font)
        self.uk.setStyleSheet("QPushButton{\n"
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
        self.uk.setObjectName("uk")
        self.gridLayout.addWidget(self.uk, 11, 1, 1, 1)
        self.es = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.es.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.es.setFont(font)
        self.es.setStyleSheet("QPushButton{\n"
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
        self.es.setObjectName("es")
        self.gridLayout.addWidget(self.es, 10, 1, 1, 1)
        self.bg = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.bg.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bg.setFont(font)
        self.bg.setStyleSheet("QPushButton{\n"
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
        self.bg.setObjectName("bg")
        self.gridLayout.addWidget(self.bg, 2, 0, 1, 1)
        self.lt = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.lt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lt.setFont(font)
        self.lt.setStyleSheet("QPushButton{\n"
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
        self.lt.setObjectName("lt")
        self.gridLayout.addWidget(self.lt, 7, 1, 1, 1)
        self.tr = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.tr.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tr.setFont(font)
        self.tr.setStyleSheet("QPushButton{\n"
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
        self.tr.setObjectName("tr")
        self.gridLayout.addWidget(self.tr, 11, 0, 1, 1)
        self.hr = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.hr.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hr.setFont(font)
        self.hr.setStyleSheet("QPushButton{\n"
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
        self.hr.setObjectName("hr")
        self.gridLayout.addWidget(self.hr, 3, 0, 1, 1)
        self.da = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.da.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.da.setFont(font)
        self.da.setStyleSheet("QPushButton{\n"
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
        self.da.setObjectName("da")
        self.gridLayout.addWidget(self.da, 0, 2, 1, 1)
        self.ru = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ru.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ru.setFont(font)
        self.ru.setStyleSheet("QPushButton{\n"
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
        self.ru.setObjectName("ru")
        self.gridLayout.addWidget(self.ru, 9, 0, 1, 1)
        self.no = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.no.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.no.setFont(font)
        self.no.setStyleSheet("QPushButton{\n"
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
        self.no.setObjectName("no")
        self.gridLayout.addWidget(self.no, 7, 2, 1, 1)
        self.ja = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ja.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ja.setFont(font)
        self.ja.setStyleSheet("QPushButton{\n"
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
        self.ja.setObjectName("ja")
        self.gridLayout.addWidget(self.ja, 6, 2, 1, 1)
        self.nl = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nl.setFont(font)
        self.nl.setStyleSheet("QPushButton{\n"
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
        self.nl.setObjectName("nl")
        self.gridLayout.addWidget(self.nl, 1, 2, 1, 1)
        self.isl = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.isl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.isl.setFont(font)
        self.isl.setStyleSheet("QPushButton{\n"
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
        self.isl.setObjectName("isl")
        self.gridLayout.addWidget(self.isl, 6, 0, 1, 1)
        self.fr = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.fr.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fr.setFont(font)
        self.fr.setStyleSheet("QPushButton{\n"
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
        self.fr.setObjectName("fr")
        self.gridLayout.addWidget(self.fr, 4, 2, 1, 1)
        self.sl = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.sl.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sl.setFont(font)
        self.sl.setStyleSheet("QPushButton{\n"
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
        self.sl.setObjectName("sl")
        self.gridLayout.addWidget(self.sl, 10, 0, 1, 1)
        self.az = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.az.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.az.setFont(font)
        self.az.setStyleSheet("QPushButton{\n"
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
        self.az.setObjectName("az")
        self.gridLayout.addWidget(self.az, 1, 0, 1, 1)
        self.sk = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.sk.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sk.setFont(font)
        self.sk.setStyleSheet("QPushButton{\n"
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
        self.sk.setObjectName("sk")
        self.gridLayout.addWidget(self.sk, 9, 2, 1, 1)
        self.sv = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.sv.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sv.setFont(font)
        self.sv.setStyleSheet("QPushButton{\n"
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
        self.sv.setObjectName("sv")
        self.gridLayout.addWidget(self.sv, 10, 2, 1, 1)
        self.ko = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ko.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ko.setFont(font)
        self.ko.setStyleSheet("QPushButton{\n"
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
        self.ko.setObjectName("ko")
        self.gridLayout.addWidget(self.ko, 7, 0, 1, 1)
        self.it = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.it.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.it.setFont(font)
        self.it.setStyleSheet("QPushButton{\n"
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
        self.it.setObjectName("it")
        self.gridLayout.addWidget(self.it, 6, 1, 1, 1)
        self.fi = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.fi.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.fi.setFont(font)
        self.fi.setStyleSheet("QPushButton{\n"
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
        self.fi.setObjectName("fi")
        self.gridLayout.addWidget(self.fi, 4, 1, 1, 1)
        self.en = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.en.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.en.setFont(font)
        self.en.setStyleSheet("QPushButton{\n"
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
        self.en.setObjectName("en")
        self.gridLayout.addWidget(self.en, 2, 2, 1, 1)
        self.hy = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.hy.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.hy.setFont(font)
        self.hy.setStyleSheet("QPushButton{\n"
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
        self.hy.setObjectName("hy")
        self.gridLayout.addWidget(self.hy, 0, 1, 1, 1)
        self.sr = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.sr.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("KB Astrolyte")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sr.setFont(font)
        self.sr.setStyleSheet("QPushButton{\n"
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
        self.sr.setObjectName("sr")
        self.gridLayout.addWidget(self.sr, 9, 1, 1, 1)
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
        self.tl.setText(_translate("Dialog", "Филиппинский"))
        self.et.setText(_translate("Dialog", "Эстонский"))
        self.cn.setText(_translate("Dialog", "Белорусский"))
        self.ro.setText(_translate("Dialog", "Румынский"))
        self.be.setText(_translate("Dialog", "Белорусский"))
        self.fil.setText(_translate("Dialog", "Филиппинский"))
        self.el.setText(_translate("Dialog", "Греческий"))
        self.de.setText(_translate("Dialog", "Немецкий"))
        self.ar.setText(_translate("Dialog", "Арабский"))
        self.cs.setText(_translate("Dialog", "Чешский"))
        self.pt.setText(_translate("Dialog", "Португальский"))
        self.hu.setText(_translate("Dialog", "Венгерский"))
        self.pl.setText(_translate("Dialog", "Польский"))
        self.uk.setText(_translate("Dialog", "Украинский"))
        self.es.setText(_translate("Dialog", "Испанский"))
        self.bg.setText(_translate("Dialog", "Болгарский"))
        self.lt.setText(_translate("Dialog", "Литовский"))
        self.tr.setText(_translate("Dialog", "Турецкий"))
        self.hr.setText(_translate("Dialog", "Хорватский"))
        self.da.setText(_translate("Dialog", "Датский"))
        self.ru.setText(_translate("Dialog", "Русский"))
        self.no.setText(_translate("Dialog", "Норвежский"))
        self.ja.setText(_translate("Dialog", "Японский"))
        self.nl.setText(_translate("Dialog", "Нидерландский"))
        self.isl.setText(_translate("Dialog", "Исландский"))
        self.fr.setText(_translate("Dialog", "Французский"))
        self.sl.setText(_translate("Dialog", "Словенский"))
        self.az.setText(_translate("Dialog", "Азербайджанский"))
        self.sk.setText(_translate("Dialog", "Словацкий"))
        self.sv.setText(_translate("Dialog", "Шведский"))
        self.ko.setText(_translate("Dialog", "Корейский"))
        self.it.setText(_translate("Dialog", "Итальянский"))
        self.fi.setText(_translate("Dialog", "Финский"))
        self.en.setText(_translate("Dialog", "Английский"))
        self.hy.setText(_translate("Dialog", "Армянский"))
        self.sr.setText(_translate("Dialog", "Сербский"))
        self.SearchLine.setText(_translate("Dialog", "Поиск"))
        self.WindowMoveButton.setText(_translate("Dialog", "Steam"))
from GUI.pictures import resources
