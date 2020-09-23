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
        self.messages = {'file_not_found': f'Не найден файл {parent.message}',
                         'JSONDecodeError': f'{parent.message}',
                         'translation_already_written': 'Перевод уже был записан',
                         'no_translation': 'Ошибка записи файла. Нет перевода.',
                         'mod_not_choosen': f'Вы не выбрали мод',
                         'invalid_file': 'Файл перевода поврежден или удален',
                         'mods_not_found': 'Моды не найдены',
                         'FileNotFoundError': f'{parent.message}',
                         'IndexError': 'Вы выбрали не тот файл',
                         'invalid_id': 'Вы не ввели ID мода',
                         'invalid_id_symbols': 'Строка ID содержит сторонние символы',
                         'OSError': 'Мод не найден',
                         'invalid_key': 'Неверный ключ [Для разработчиков]'}
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
