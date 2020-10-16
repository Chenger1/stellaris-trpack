from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import AcceptMessage

from scripts.utils import collection_append, save_unfinished_machine_text
from scripts.db import get_info_from_db
from scripts.messeges import call_success_message


class AcceptMessageWindow(QtWidgets.QDialog, AcceptMessage.Ui_Dialog):
    def __init__(self, parent, message, accept_func=None, denied_func=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.string = self.StringsList.text().split('.')
        self.messages = {'collection_continue_translation': f'{self.string[0]} - {message[1]}',
                         'start_translation': f'{self.string[1]} - {message[1]}',
                         'save_translation': f'{self.string[2]}',
                         'invalid_key': f'{self.string[3]}'}
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
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.reference_window('QLabel_2_1_Functional'))
        self.WindowMoveButton.installEventFilter(self)

    def save_translation_state(self):
        pointer_position = self.parent.pointer
        translation_status = round((len(self.parent.user_text*100))/len(self.parent.orig_text))
        save_unfinished_machine_text(self.parent.machine_text)
        hashKey = tuple(filter(lambda x: x[1] in self.parent.ModIDLine.text(), get_info_from_db('get_mod_data')))[0][0]
        collection_append(self.parent.ModIDLine.text(), translation_status, pointer_position, hashKey)
        self.parent.clean_state()
        message = 'file_was_written'
        self.message = ''
        self.close()
        call_success_message(self, message)

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
