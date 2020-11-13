"""
                            ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import TranslationLanguage
from json import load, dump
from functools import partial
import copy

from scripts.stylesheets import choosen_lang_style, not_chosen_lang_style


class TranslationLanguageWindow(QtWidgets.QDialog, TranslationLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.buttons_data = {
            'RussianButton': 'ru', 'UkrainianButton': 'uk', 'PolishButton': 'pl',
            'ChineseButton': 'zh-cn', 'ArabicButton': 'ar', 'BelarusianButton': 'be',
            'BulgarianButton': 'bg', 'CroatianButton': 'hr', 'CzechButton': 'cs',
            'DanishButton': 'da', 'DutchButton': 'nl', 'EstonianButton': 'et',
            'FinnishButton': 'fi', 'FrenchButton': 'fr', 'GermanButton': 'de',
            'GreekButton': 'el', 'HungarianButton': 'hu', 'ItalianButton': 'it',
            'JapaneseButton': 'ja', 'KoreanButton': 'ko', 'LithuanianButton': 'lt',
            'NorwegianButton': 'no', 'PortugueseButton': 'pt', 'SlovakButton': 'sk',
            'SpanishButton': 'es', 'SwedishButton': 'sv', 'TurkishButton': 'tr'
        }
        self.string = self.LanguagesList.text().split()
        self.buttons = self.prep_buttons()
        self.init_handlers()

        self.gridLayout.setColumnMinimumWidth(1, 50)
        self.generator = copy.copy(self.buttons)
        self.row_index = 0
        self.column_index = -1
        self.paint_elements()

    def init_handlers(self):
        self.WindowMoveButton.installEventFilter(self)
        self.ExitButton.clicked.connect(self.close)
        self.SearchLine.textChanged.connect(self.search_init)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_5_TargetLanguage'))

    def prep_buttons(self):
        buttons = {}
        index = 0

        for button, lang in self.buttons_data.items():
            buttons[button] = QtWidgets.QPushButton(self.string[index])
            buttons[button].setObjectName(button)
            buttons[button].clicked.connect(partial(self.set_target_language, target_language=lang))
            index += 1

        return buttons

    def search_init(self, text):
        self.clean()
        self.search(text)
        self.choose_lang()

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

    def clean(self):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

    def search(self, text):
        with open('Properties.json', 'r', encoding='utf-8') as prop:
            properties = load(prop)

        self.column_index = -1
        self.generator = copy.copy(self.buttons)

        for object_name, button in self.buttons.items():
            if text not in button.text().lower():
                if properties["target_language"] not in self.buttons_data[object_name]:
                    del self.generator[object_name]
        self.paint_elements()

    def paint_elements(self):
        for object_name, button in self.generator.items():
            if self.column_index < 2:
                self.column_index += 1
            else:
                self.column_index = 0
                self.row_index += 1

            self.gridLayout.addWidget(button, self.row_index, self.column_index)

        self.choose_lang()

    """
                                ↓ Выбор языка, на который будут переводиться файлы ↓
    """

    def choose_lang(self):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)

        for object_name, button in self.buttons.items():
            if self.buttons_data[object_name] == properties["target_language"]:
                choosen_lang_style(button)
            else:
                not_chosen_lang_style(button)

    def set_target_language(self, target_language=None):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
            properties["target_language"] = target_language
        with open("Properties.json", 'w', encoding='utf-8') as prop:
            dump(properties, prop)
        self.choose_lang()
