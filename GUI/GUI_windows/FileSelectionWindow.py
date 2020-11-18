"""
                            ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import UpdateTranslation

from scripts.stylesheets import file_choosen_style, file_not_choosen_style
from scripts.utils import drive, user
from scripts.messeges import call_error_message


class FileSelectionWindow(QtWidgets.QDialog, UpdateTranslation.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.parent = parent
        self.init_handlers()
        self.message = None

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_5_TranslationLanguage'))
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
