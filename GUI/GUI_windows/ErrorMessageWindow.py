from PyQt5 import QtWidgets

from GUI.GUI_windows_source import ErrorMessage


class ErrorMessageWindow(QtWidgets.QMainWindow, ErrorMessage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.AcceptButton.clicked.connect(self.close)
