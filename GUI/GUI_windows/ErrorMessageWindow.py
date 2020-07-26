from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint

from GUI.GUI_windows_source import ErrorMessage


class ErrorMessageWindow(QtWidgets.QMainWindow, ErrorMessage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.oldPos = self.pos()
        self.show()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.AcceptButton.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()