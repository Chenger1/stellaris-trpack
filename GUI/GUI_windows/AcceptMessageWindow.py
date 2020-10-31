# TODO Fix message depences
"""
                                    ↓ Инициализация данных ↓
"""
from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import AcceptMessage


class AcceptMessageWindow(QtWidgets.QDialog, AcceptMessage.Ui_Dialog):
    def __init__(self, parent, message, accept_func=None, denied_func=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers(accept_func, denied_func)

        self.InfoLabel.setWordWrap(True)
        self.string = self.StringsList.text().split('.')
        self.messages = {'collection_append': f'{message[1]}\n\n{self.string[0]}',
                         'continue_last_translation': f'{message[-1]}\n\n{self.string[1]}?',
                         'start_translation': f'{message[-1]}\n\n{self.string[1]}?',
                         'save_translation': f'{self.string[2]}',
                         'invalid_key': f'{self.string[3]}'}
        try:
            self.InfoLabel.setText(self.messages[message[0]])
        except AttributeError:
            self.InfoLabel.setText(self.messages['invalid_key'])
        except KeyError:
            self.InfoLabel.setText(self.messages['invalid_key'])

    def init_handlers(self, accept_func, denied_func):
        self.ExitButton.clicked.connect(self.close)
        self.AcceptButton.clicked.connect(accept_func)
        self.DeniedButton.clicked.connect(denied_func or self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.reference_window('QLabel_2_1_Functional'))
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
                self.move(self.pos() - self.oldPos + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.oldPos = None
        return super().eventFilter(source, event)
