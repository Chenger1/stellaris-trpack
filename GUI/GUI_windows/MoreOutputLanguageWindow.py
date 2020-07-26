from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import MoreOutputLanguage


class MoreOutputLanguageWindow(QtWidgets.QMainWindow, MoreOutputLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)