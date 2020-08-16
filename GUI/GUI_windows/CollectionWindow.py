from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Collection

from scripts.utils import get_collection


class CollectionWindow(QtWidgets.QDialog, Collection.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers()
        self.collection = get_collection()
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)

    def paint_elements(self):
        grid = self.gridLayout
        for index, elem in enumerate(self.collection):
            grid.setSpacing(10)
            label = QtWidgets.QLabel(f'{index + 1}: {self.collection[elem][0]}')
            steam_id = QtWidgets.QLabel(elem)
            status = QtWidgets.QLabel(self.collection[elem][-1])
            label.setStyleSheet('color:white')
            label.setWordWrap(True)
            steam_id.setStyleSheet('color:white')
            status.setStyleSheet('color:white')
            grid.addWidget(label, index + 1, 2, 1, 4)
            grid.addWidget(steam_id, index + 1, 6)
            grid.addWidget(status, index + 1, 7)

    def eventFilter(self, source, event):
        if source == self.WindowMoveButton:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.oldPos = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.oldPos is not None:
                self.move(self.pos() - self.oldPos + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.oldPos = None
        return super().eventFilter(source, event)
