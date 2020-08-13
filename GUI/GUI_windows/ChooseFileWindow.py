from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ChooseFile
from  GUI.GUI_windows.CollectionWindow import CollectionWindow
from GUI.GUI_windows.SteamIDWindow import SteamIDWindow

from scripts.utils import get_mod_id, paradox_mod_way_to_content


class ChooseFileWindow(QtWidgets.QDialog, ChooseFile.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.parent = parent

    def init_handlers(self):
        self.ManualButton.clicked.connect(lambda :self.choose_file(QtWidgets.QFileDialog.getOpenFileName()[0]))
        self.SteamButton.clicked.connect(self.show_steam_id_window)
        self.CollectionButton.clicked.connect(self.show_collection_window)
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)

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
