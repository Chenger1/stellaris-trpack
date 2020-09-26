from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import SuccessMessage


class SuccessMessageWindow(QtWidgets.QDialog, SuccessMessage.Ui_Dialog):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.init_handlers()
        self.oldPos = self.pos()
        self.string = self.StringsList.text().split('.')
        self.messages = {'file_was_written': f'{self.string[0]}',
                         'file_was_saved': f'{self.string[1]}',
                         'mods_successfully_sorted': f'{self.string[2]}',
                         'invalid_key': f'{self.string[3]}'}
        try:
            self.InfoLabel.setText(self.messages[message])
        except KeyError:
            self.InfoLabel.setText(self.messages['invalid_key'])
        self.WindowMoveButton.installEventFilter(self)

    def init_handlers(self):
        self.AcceptButton.clicked.connect(self.close)
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
