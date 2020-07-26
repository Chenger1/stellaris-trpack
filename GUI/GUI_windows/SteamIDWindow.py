from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import SteamID


class SteamIDWindow(QtWidgets.QMainWindow, SteamID.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.init_handlers()
        self.parent = parent
        self.oldPos = self.pos()
        self.WindowMoveButton.installEventFilter(self)

    def init_handlers(self):
        self.AcceptButton.clicked.connect(self.get_steam_id)

    def get_steam_id(self):
        path = self.IDLine.text()
        self.parent.parent.get_steam_id(path.split('=')[-1])
        self.parent.close()
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