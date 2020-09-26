from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ErrorMessage


class ErrorMessageWindow(QtWidgets.QDialog, ErrorMessage.Ui_Dialog):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.init_handlers()
        self.oldPos = self.pos()
        self.string = self.StringsList.text().split('.')
        self.messages = {'file_not_found': f'{self.string[0]} {parent.message}',
                         'JSONDecodeError': f'{parent.message}',
                         'translation_already_written': f'{self.string[1]}',
                         'no_translation': f'{self.string[2]}',
                         'mod_not_choosen': f'{self.string[3]}',
                         'invalid_file': f'{self.string[4]}',
                         'mods_not_found': f'{self.string[5]}',
                         'FileNotFoundError': f'{parent.message}',
                         'IndexError': f'{self.string[6]}',
                         'invalid_id': f'{self.string[7]}',
                         'invalid_id_symbols': f'{self.string[8]}',
                         'OSError': f'{self.string[9]}',
                         'invalid_key': f'{self.string[10]}'}
        print(self.messages)
        try:
            self.InfoLabel.setText(self.messages[message])
        except KeyError:
            self.InfoLabel.setText(self.messages['invalid_key'])
        self.InfoLabel.setWordWrap(True)
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
