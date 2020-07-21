from PyQt5 import QtWidgets

from GUI.GUI_windows_source import SteamID


class SteamIDWindow(QtWidgets.QMainWindow, SteamID.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_handlers()
        self.parent = parent

    def init_handlers(self):
        self.LocalizeButton.clicked.connect(self.get_steam_id)

    def get_steam_id(self):
        path = self.lineEdit.text()
        self.parent.parent.get_steam_id(path.split('=')[-1])
        self.parent.close()
        self.close()
