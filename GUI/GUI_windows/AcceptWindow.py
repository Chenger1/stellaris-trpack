from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Accept

from scripts.utils import collection_append, save_unfinished_machine_text
from scripts.messeges import call_success_message


class AcceptWindow(QtWidgets.QDialog, Accept.Ui_Dialog):
    def __init__(self, parent, message, accept_func=None, denied_func=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.string = self.StringsList.text().split('.')
        self.messages = {'collection_continue_translation': f'{self.string[0]} - {message[1]}',
                         'save_translation': f'{self.string[1]}',
                         'invalid_key': f'{self.string[2]}'}
        try:
            self.InfoLabel.setText(self.messages[message[0]])
        except AttributeError:
            self.InfoLabel.setText(self.messages['invalid_key'])
        except KeyError:
            self.InfoLabel.setText(self.messages['invalid_key'])

        self.InfoLabel.setWordWrap(True)
        self.init_handlers(accept_func, denied_func)
        self.message = ''

    def init_handlers(self, accept_func, denied_func):
        self.ExitButton.clicked.connect(self.close)
        self.AcceptButton.clicked.connect(accept_func or self.save_translation_state)
        self.DeniedButton.clicked.connect(denied_func or self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.parent.reference_window('QLabel_2_1_Functional'))
        self.WindowMoveButton.installEventFilter(self)

    def save_translation_state(self):
        pointer_position = self.parent.pointer
        translation_status = round((len(self.parent.user_text*100))/len(self.parent.orig_text))
        save_unfinished_machine_text(self.parent.machine_text)
        collection_append(self.parent.ModIDLine.text(), translation_status, pointer_position)
        self.parent.clean_state()
        message = 'file_was_written'
        self.message = ''
        call_success_message(self, message)
        self.close()

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
