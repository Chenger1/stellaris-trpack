"""
                            ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore
from json import load, dump

from GUI.GUI_windows_source import ToolLanguage

from scripts.stylesheets import choosen_lang_style, not_chosen_lang_style
from scripts.messeges import call_success_message


class ToolLanguageWindow(QtWidgets.QDialog, ToolLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.parent = parent
        self.buttons = {
            'zh': self.ChineseButton,
            'en': self.EnglishButton,
            'pl': self.PolishButton,
            'ru': self.RussianButton,
            'uk': self.UkrainianButton,
        }
        self.choose_lang()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)
        self.ChineseButton.clicked.connect(lambda: self.set_translation_language('zh'))
        self.EnglishButton.clicked.connect(lambda: self.set_translation_language('en'))
        self.PolishButton.clicked.connect(lambda: self.set_translation_language('pl'))
        self.RussianButton.clicked.connect(lambda: self.set_translation_language('ru'))
        self.UkrainianButton.clicked.connect(lambda: self.set_translation_language('uk'))
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_4_InterfaceLanguage'))

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

    """
                                    ↓ Рендер ↓
    """

    def choose_lang(self):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
        for button in self.buttons:
            if button == properties["tool_language"]:
                choosen_lang_style(self.buttons[button])
            else:
                not_chosen_lang_style(self.buttons[button])

    """
                                    ↓ Выбор языка интерфейса ↓
    """

    def set_translation_language(self, translation_language):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
            properties["tool_language"] = translation_language
        with open("Properties.json", 'w', encoding='utf-8') as prop:
            dump(properties, prop)
        message = 'language_was_changed'
        call_success_message(self, message)
        self.close()
