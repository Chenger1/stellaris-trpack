from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Collection


class CollectionWindow(QtWidgets.QDialog, Collection.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)

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
