from PyQt5 import QtWidgets

from GUI.GUI_windows_source import ChooseFile

from GUI.GUI_windows.SteamIDWindow import SteamIDWindow

from scripts.utils import get_mod_id


class ChooseFileWindow(QtWidgets.QMainWindow, ChooseFile.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_handlers()
        self.parent = parent

    def init_handlers(self):
        self.FileSelectionButton.clicked.connect(self.choose_file)
        self.SteamButton.clicked.connect(self.show_steam_id_window)

    def choose_file(self):
        f_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if f_path:
            mod_id = get_mod_id(f_path)
            self.parent.FilePathString.setText(mod_id)
            self.close()

    def show_steam_id_window(self):
        steam_id_window = SteamIDWindow(self)
        steam_id_window.show()

