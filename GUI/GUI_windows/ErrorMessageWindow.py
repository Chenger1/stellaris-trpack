"""
                                    ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ErrorMessage


class ErrorMessageWindow(QtWidgets.QDialog, ErrorMessage.Ui_Dialog):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.string = self.StringsList.text().split('.')
        self.messages = {'files_not_found': f'{self.string[0]} {parent.message}',
                         'JSONDecodeError': f'{parent.message}',
                         'invalid_file': f'{self.string[4]}',
                         'mods_not_found': f'{self.string[5]}',
                         'FileNotFoundError': f'{parent.message}',
                         'someting_went_wrong': f'{self.string[6]}\n\n{parent.message}',
                         'all_is_complete': f'{self.string[10]}',
                         'no_string_matches': f'{self.string[11]}',
                         'files_are_identical': f'{self.string[12]}',
                         'TypeError': f'{self.string[13]}',
                         'files_not_choosen': f'{self.string[14]}',
                         'invalid_key': f'{self.string[15]}'
                         }
        self.InfoLabel.setWordWrap(True)
        try:
            self.InfoLabel.setText(self.messages[message])
        except KeyError:
            self.InfoLabel.setText(self.messages['invalid_key'])
        # self.parent.message = None

    def init_handlers(self):
        self.AcceptButton.clicked.connect(self.close)
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)

    def eventFilter(self, source, event):
        """
                    Данная функция предназначена для отслеживания позиции окна
                    и его перемещения кликом по шапке
        """
        if source == self.WindowMoveButton:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.oldPos = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.oldPos is not None:
                self.move(self.pos() - self.oldPos+event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.oldPos = None
        return super().eventFilter(source, event)
