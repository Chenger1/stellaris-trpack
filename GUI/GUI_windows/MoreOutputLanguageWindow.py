from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import MoreOutputLanguage


class MoreOutputLanguageWindow(QtWidgets.QDialog, MoreOutputLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.WindowMoveButton.installEventFilter(self)
        self.ExitButton.clicked.connect(self.close)

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