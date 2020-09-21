from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import TranslationLanguage
from json import load, dump
import copy

from scripts.stylesheets import active_lang_style, inactive_lang_style


class TranslationLanguageWindow(QtWidgets.QDialog, TranslationLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.parent = parent
        self.grid = self.GridLangButtonsLayout
        self.grid.setColumnMinimumWidth(1, 50)
        self.lang = self.LanguagesList.text().split()
        self.ArabicButton = QtWidgets.QPushButton(self.lang[0])
        self.ArmenianButton = QtWidgets.QPushButton(self.lang[1])
        self.AzerbaijaniButton = QtWidgets.QPushButton(self.lang[2])
        self.BelarusianButton = QtWidgets.QPushButton(self.lang[3])
        self.BulgarianButton = QtWidgets.QPushButton(self.lang[4])
        self.ChineseButton = QtWidgets.QPushButton(self.lang[5])
        self.CroatianButton = QtWidgets.QPushButton(self.lang[6])
        self.CzechButton = QtWidgets.QPushButton(self.lang[7])
        self.DanishButton = QtWidgets.QPushButton(self.lang[8])
        self.DutchButton = QtWidgets.QPushButton(self.lang[9])
        self.EnglishButton = QtWidgets.QPushButton(self.lang[10])
        self.EstonianButton = QtWidgets.QPushButton(self.lang[11])
        self.FinnishButton = QtWidgets.QPushButton(self.lang[12])
        self.FrenchButton = QtWidgets.QPushButton(self.lang[13])
        self.GermanButton = QtWidgets.QPushButton(self.lang[14])
        self.GreekButton = QtWidgets.QPushButton(self.lang[15])
        self.HungarianButton = QtWidgets.QPushButton(self.lang[16])
        self.ItalianButton = QtWidgets.QPushButton(self.lang[17])
        self.JapaneseButton = QtWidgets.QPushButton(self.lang[18])
        self.KoreanButton = QtWidgets.QPushButton(self.lang[19])
        self.LithuanianButton = QtWidgets.QPushButton(self.lang[20])
        self.NorwegianButton = QtWidgets.QPushButton(self.lang[21])
        self.PolishButton = QtWidgets.QPushButton(self.lang[22])
        self.PortugueseButton = QtWidgets.QPushButton(self.lang[23])
        self.RussianButton = QtWidgets.QPushButton(self.lang[24])
        self.SlovakButton = QtWidgets.QPushButton(self.lang[25])
        self.SlovenianButton = QtWidgets.QPushButton(self.lang[26])
        self.SpanishButton = QtWidgets.QPushButton(self.lang[27])
        self.SwedishButton = QtWidgets.QPushButton(self.lang[28])
        self.TurkishButton = QtWidgets.QPushButton(self.lang[29])
        self.UkrainianButton = QtWidgets.QPushButton(self.lang[30])
        self.FilipinoButton = QtWidgets.QPushButton(self.lang[31])

        self.buttons = {
            'EnglishButton': [self.EnglishButton, 'en'],
            'RussianButton': [self.RussianButton, 'ru'],
            'UkrainianButton': [self.UkrainianButton, 'uk'],
            'PolishButton': [self.PolishButton, 'pl'],
            'ChineseButton': [self.ChineseButton, 'zh-cn'],
            'ArabicButton': [self.ArabicButton, 'ar'],
            'ArmenianButton': [self.ArmenianButton, 'hy'],
            'AzerbaijaniButton': [self.AzerbaijaniButton, 'az'],
            'BelarusianButton': [self.BelarusianButton, 'be'],
            'BulgarianButton': [self.BulgarianButton, 'bg'],
            'CroatianButton': [self.CroatianButton, 'hr'],
            'CzechButton': [self.CzechButton, 'cs'],
            'DanishButton': [self.DanishButton, 'da'],
            'DutchButton': [self.DutchButton, 'nl'],
            'EstonianButton': [self.EstonianButton, 'et'],
            'FinnishButton': [self.FinnishButton, 'fi'],
            'FrenchButton': [self.FrenchButton, 'fr'],
            'GermanButton': [self.GermanButton, 'de'],
            'GreekButton': [self.GreekButton, 'el'],
            'HungarianButton': [self.HungarianButton, 'hu'],
            'ItalianButton': [self.ItalianButton, 'it'],
            'JapaneseButton': [self.JapaneseButton, 'ja'],
            'KoreanButton': [self.KoreanButton, 'ko'],
            'LithuanianButton': [self.LithuanianButton, 'lt'],
            'NorwegianButton': [self.NorwegianButton, 'no'],
            'PortugueseButton': [self.PortugueseButton, 'pt'],
            'SlovakButton': [self.SlovakButton, 'sk'],
            'SpanishButton': [self.SpanishButton, 'es'],
            'SwedishButton': [self.SwedishButton, 'sv'],
            'TurkishButton': [self.TurkishButton, 'tr'],
        }
        self.generator = copy.copy(self.buttons)
        self.set_active()
        self.init_handlers()

    def set_active(self):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
        for button in self.buttons:
            if self.buttons[button][1] == properties["translation_language"]:
                active_lang_style(self.buttons[button][0])
            else:
                inactive_lang_style(self.buttons[button][0])
        self.gen()

    def gen(self):
        n = 0
        k = -1
        for button in self.generator:
            if k != 2:
                k += 1
            else:
                k = 0
                n += 1
            self.grid.addWidget(self.buttons[button][0], n, k)

    def clean(self):
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

    def search(self, text):
        with open('Properties.json', 'r', encoding='utf-8') as prop:
            properties = load(prop)
        self.generator = copy.copy(self.buttons)
        for button in self.buttons:
            if text in self.buttons[button][0].text().lower():
                pass
            else:
                if properties["translation_language"] != self.buttons[button][1]:
                    del self.generator[button]

    def set_translation_language(self, translation_language):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
            properties["translation_language"] = translation_language
        with open("Properties.json", 'w', encoding='utf-8') as prop:
            dump(properties, prop)
        self.set_active()

    def init_handlers(self):
        self.WindowMoveButton.installEventFilter(self)
        self.ExitButton.clicked.connect(self.close)
        self.ArabicButton.clicked.connect(lambda: self.set_translation_language('ar'))
        self.ArmenianButton.clicked.connect(lambda: self.set_translation_language('hy'))
        self.AzerbaijaniButton.clicked.connect(lambda: self.set_translation_language('az'))
        self.BelarusianButton.clicked.connect(lambda: self.set_translation_language('be'))
        self.BulgarianButton.clicked.connect(lambda: self.set_translation_language('bg'))
        self.ChineseButton.clicked.connect(lambda: self.set_translation_language('zh-cn'))
        self.CroatianButton.clicked.connect(lambda: self.set_translation_language('hr'))
        self.CzechButton.clicked.connect(lambda: self.set_translation_language('cs'))
        self.DanishButton.clicked.connect(lambda: self.set_translation_language('da'))
        self.DutchButton.clicked.connect(lambda: self.set_translation_language('nl'))
        self.EnglishButton.clicked.connect(lambda: self.set_translation_language('en'))
        self.EstonianButton.clicked.connect(lambda: self.set_translation_language('et'))
        self.FinnishButton.clicked.connect(lambda: self.set_translation_language('fi'))
        self.FrenchButton.clicked.connect(lambda: self.set_translation_language('fr'))
        self.GermanButton.clicked.connect(lambda: self.set_translation_language('de'))
        self.GreekButton.clicked.connect(lambda: self.set_translation_language('el'))
        self.HungarianButton.clicked.connect(lambda: self.set_translation_language('hu'))
        self.ItalianButton.clicked.connect(lambda: self.set_translation_language('it'))
        self.JapaneseButton.clicked.connect(lambda: self.set_translation_language('ja'))
        self.KoreanButton.clicked.connect(lambda: self.set_translation_language('ko'))
        self.LithuanianButton.clicked.connect(lambda: self.set_translation_language('lt'))
        self.NorwegianButton.clicked.connect(lambda: self.set_translation_language('no'))
        self.PolishButton.clicked.connect(lambda: self.set_translation_language('pl'))
        self.PortugueseButton.clicked.connect(lambda: self.set_translation_language('pt'))
        self.RussianButton.clicked.connect(lambda: self.set_translation_language('ru'))
        self.SlovakButton.clicked.connect(lambda: self.set_translation_language('sk'))
        self.SlovenianButton.clicked.connect(lambda: self.set_translation_language('sl'))
        self.SpanishButton.clicked.connect(lambda: self.set_translation_language('es'))
        self.SwedishButton.clicked.connect(lambda: self.set_translation_language('sv'))
        self.TurkishButton.clicked.connect(lambda: self.set_translation_language('tr'))
        self.UkrainianButton.clicked.connect(lambda: self.set_translation_language('uk'))
        self.SearchLine.textChanged.connect(self.sync_lineEdit)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_4_TranslationLanguage'))

    def sync_lineEdit(self, text):
        self.clean()
        self.search(text)
        self.set_active()

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
