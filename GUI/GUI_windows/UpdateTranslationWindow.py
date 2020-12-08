"""
                            ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import UpdateTranslation

from scripts.stylesheets import file_choosen_style, file_not_choosen_style
from scripts.utils import drive, user
from scripts.comparer import update_lines
from scripts.messeges import call_error_message, call_success_message


class UpdateTranslationWindow(QtWidgets.QDialog, UpdateTranslation.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.files = {}
        self.oldPos = self.pos()
        self.parent = parent
        self.init_handlers()
        self.message = None

        self.types = {
            'ChooseOldTrFileButton': self.OldTrStatusLabel,
            'ChooseNewVerFileButton': self.NewVerStatusLabel
        }

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_5_TranslationLanguage'))
        self.ChooseOldTrFileButton.clicked.connect(lambda: self.choose_file(self.ChooseOldTrFileButton.objectName()))
        self.ChooseNewVerFileButton.clicked.connect(lambda: self.choose_file(self.ChooseNewVerFileButton.objectName()))
        self.AcceptButton.clicked.connect(self.compare)
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

    """
                                ↓ Рендер ↓
    """

    def clean_state(self):
        self.files = {}
        for elem in self.types.values():
            file_not_choosen_style(elem)

    def choose_file(self, file_type):
        file = QtWidgets.QFileDialog.getOpenFileName(directory=f'{drive}:\\Users\\{user}\\Desktop')

        if file[0]:
            if file[0].split('.')[-1] not in '.txt.yml.yaml':
                call_error_message(self, 'TypeError')
            else:
                self.files[file_type] = file[0]
                file_choosen_style(self.types[file_type])
        else:
            try:
                self.files.pop(file_type)
                file_not_choosen_style(self.types[file_type])
            except KeyError:
                pass

    """
                                ↓ Обновление временных файлов ↓
    """

    def compare(self):
        if not self.files:
            self.message = 'Вы не выбрали файлы'
            call_error_message(self, 'files_not_choosen')
            return False
        try:
            old_tr_file_path = self.files['ChooseOldTrFileButton']
            new_ver_file_path = self.files['ChooseNewVerFileButton']

            if old_tr_file_path.split('.')[-1] == new_ver_file_path.split('.')[-1]:
                update_lines(old_tr_file_path, new_ver_file_path)
                # self.close()
            else:
                raise KeyError

        except KeyError:
            self.clean_state()
            call_error_message(self, 'files_not_choosen')
        else:
            call_success_message(self, 'files_was_compared')
            self.close()
