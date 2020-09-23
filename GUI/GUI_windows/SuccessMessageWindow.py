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
        self.messages = {'file_was_written': 'Файл перевода успешно записан',
                         'file_was_saved': 'Файл сохранен',
                         'mods_successfully_sorted': 'Моды успешно отсортированы',
                         'invalid_key': 'Неверный ключ [Для разработчиков]'}
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
