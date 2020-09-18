from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ChooseFile
from GUI.GUI_windows.CollectionWindow import CollectionWindow
from GUI.GUI_windows.SteamIDWindow import SteamIDWindow

from scripts.utils import get_mod_id, open_zip_file
from scripts.db import get_info_from_db


class ChooseFileWindow(QtWidgets.QDialog, ChooseFile.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.parent = parent
        self.mods_folder = self.get_mods_folder_path()

    def init_handlers(self):
        self.ManualButton.clicked.connect(self.open_file_dialog)
        self.SteamButton.clicked.connect(self.show_steam_id_window)
        self.CollectionButton.clicked.connect(self.show_collection_window)
        self.ExitButton.clicked.connect(self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_1_Modification'))
        self.WindowMoveButton.installEventFilter(self)

    def open_file_dialog(self):
        if self.mods_folder:
            f_path = QtWidgets.QFileDialog.getOpenFileName(directory=self.mods_folder)[0]
            if '.zip' in f_path.split('/')[-1]:
                open_zip_file(f_path)
                f_path = QtWidgets.QFileDialog.getOpenFileName(directory='/'.join(f_path.split('/')[:-1]))[0]
        else:
            f_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.choose_file(f_path)

    def choose_file(self, f_path):
        if f_path:
            mod_id = get_mod_id(f_path)
            self.parent.ModIDLine.setText(mod_id)
            self.close()

    def show_steam_id_window(self):
        steam_id_window = SteamIDWindow(self)
        steam_id_window.show()
        self.close()

    def show_collection_window(self):
        collection_window = CollectionWindow(self)
        collection_window.show()
        self.close()

    def get_mods_folder_path(self):
        raw_path = get_info_from_db('get_path_to_mods', 1)[0]
        if 'SteamLibrary' not in raw_path:
            self.parent.show_system_message('error', 'Не найдено установленных модов для Stellaris')
        try:
            raw_path = raw_path.split('\\')
            path = '\\'.join(raw_path[:len(raw_path) - 1]) + '\\'
        except IndexError:
            path = []
        return path

    def eventFilter(self, source, event):
        if source == self.WindowMoveButton:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.oldPos = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.oldPos is not None:
                self.move(self.pos() - self.oldPos+event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.oldPos = None
        return super().eventFilter(source, event)
