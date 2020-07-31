from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ModsList

from scripts.mods_sorting import set_settings, prep_data


class ModsListWindow(QtWidgets.QDialog, ModsList.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.settingPaths = set_settings()
        self.registry, self.modList, self.dlc_load, self.game_data, self.enabled_mods = prep_data(self.settingPaths[0])
        self.checkboxes = []
        self.labels = []
        self.SortMods = QtWidgets.QPushButton('Sort mods')
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)

    def paint_elements(self):
        pass

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
