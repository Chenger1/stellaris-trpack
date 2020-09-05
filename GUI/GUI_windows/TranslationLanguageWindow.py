from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import TranslationLanguage
from json import load, dump
import copy


class TranslationLanguageWindow(QtWidgets.QDialog, TranslationLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.parent = parent
        self.grid = self.GridLangButtonsLayout

        # Необходимо сделать мультиязычность
        self.ArabicButton = QtWidgets.QPushButton('Арабский')
        self.ArmenianButton = QtWidgets.QPushButton('Армянский')
        self.AzerbaijaniButton = QtWidgets.QPushButton('Азербайджанский')
        self.BelarusianButton = QtWidgets.QPushButton('Белорусский')
        self.BulgarianButton = QtWidgets.QPushButton('Болгарский')
        self.ChineseButton = QtWidgets.QPushButton('Китайский')
        self.CroatianButton = QtWidgets.QPushButton('Хорватский')
        self.CzechButton = QtWidgets.QPushButton('Чешский')
        self.DanishButton = QtWidgets.QPushButton('Датский')
        self.DutchButton = QtWidgets.QPushButton('Нидерландский')
        self.EnglishButton = QtWidgets.QPushButton('Английский')
        self.EstonianButton = QtWidgets.QPushButton('Эстонский')
        self.FinnishButton = QtWidgets.QPushButton('Финский')
        self.FrenchButton = QtWidgets.QPushButton('Французский')
        self.GermanButton = QtWidgets.QPushButton('Немецкий')
        self.GreekButton = QtWidgets.QPushButton('Греческий')
        self.HungarianButton = QtWidgets.QPushButton('Венгерский')
        self.ItalianButton = QtWidgets.QPushButton('Итальянский')
        self.JapaneseButton = QtWidgets.QPushButton('Японский')
        self.KoreanButton = QtWidgets.QPushButton('Корейский')
        self.LithuanianButton = QtWidgets.QPushButton('Литовский')
        self.NorwegianButton = QtWidgets.QPushButton('Норвежский')
        self.PolishButton = QtWidgets.QPushButton('Польский')
        self.PortugueseButton = QtWidgets.QPushButton('Португальский')
        self.RussianButton = QtWidgets.QPushButton('Русский')
        self.SlovakButton = QtWidgets.QPushButton('Словацкий')
        self.SlovenianButton = QtWidgets.QPushButton('Словенский')
        self.SpanishButton = QtWidgets.QPushButton('Испанский')
        self.SwedishButton = QtWidgets.QPushButton('Шведский')
        self.TurkishButton = QtWidgets.QPushButton('Турецкий')
        self.UkrainianButton = QtWidgets.QPushButton('Украинский')
        self.FilipinoButton = QtWidgets.QPushButton('Филиппинский')

        self.buttons = {
            'EnglishButton': [self.EnglishButton, 'en'],
            'RussianButton': [self.RussianButton, 'ru'],
            'PolishButton': [self.PolishButton, 'pl'],
            'ChineseButton': [self.ChineseButton, 'zh-cn'],
            'UkrainianButton': [self.UkrainianButton, 'uk'],
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

    @staticmethod
    def set_inactive(button):
        button.setFont(QtGui.QFont("KB Astrolyte", 9))
        button.setStyleSheet("""
        QPushButton{
            background-color: rgba(31, 37, 51, 50);
            border: 2px solid #ffffff;
            border-radius: 12px;
            color: #ffffff;
            min-height: 20px;
            max-width: 180px;
            }
        QPushButton:hover{
            background-color: rgba(56, 57, 61, 50);
        }
        QPushButton:pressed{
            background-color: rgba(194, 194, 194, 50);
            border: #c2c2c2;
        }
        """)

    def set_active(self):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
        for button in self.buttons:
            if self.buttons[button][1] == properties["translation_language"]:
                self.buttons[button][0].setStyleSheet("""
QPushButton{
    background-color: #05B8CC;
    border: 2px solid #05B8CC;
    border-radius: 12px;
    color: #1f2533;
    min-height: 20px;
    max-width: 180px;       

}
QPushButton:hover{
    background-color: #31858f;
    border: #31858f;
    color: #ffffff;
}
QPushButton:pressed{
    background-color: rgba(194, 194, 194, 50);
    border: #c2c2c2;
}
""")
                self.generator[button][0].setFont(QtGui.QFont("KB Astrolyte", 9))
            else:
                self.set_inactive(self.buttons[button][0])
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
        # for button in self.buttons:
        #     self.grid.removeWidget(self.buttons[button][0])
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
