from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Accept

from scripts.utils import collection_append, save_unfinished_machine_text


class AcceptWindow(QtWidgets.QDialog, Accept.Ui_Dialog):
    def __init__(self, parent, message, accept_func, denied_func=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.string = self.StringsList.text().split('.')
        # в цикле создания кнопок self.message перезаписывается до вызова фукции, поэтому
        # надо как-то сохранять или передавать название мода
        self.messages = {'collection_continue_translation': f'{self.string[0]} - {parent.message}',
                         'save_translation': f'{self.string[1]}',
                         'invalid_key': f'{self.string[2]}'}
        # 'Желаете продолжить перевод мода.Вы уверены что хотите сохранить перевод?.Неверный ключ [Для разработчиков]'
        try:
            self.InfoLabel.setText(self.messages[message])
        except AttributeError:
            self.InfoLabel.setText(message)
        except KeyError:
            #self.InfoLabel.setText(self.messages['invalid_key'])
            self.InfoLabel.setText(message)

        self.InfoLabel.setWordWrap(True)
        self.init_handlers(accept_func, denied_func)
        self.message = ''

    def init_handlers(self, accept_func, denied_func):
        self.ExitButton.clicked.connect(self.close)
        self.AcceptButton.clicked.connect(accept_func)
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
        self.call_success_message(self, message)
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
