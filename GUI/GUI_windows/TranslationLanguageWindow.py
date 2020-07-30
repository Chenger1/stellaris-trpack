from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import TranslationLanguage
from json import load, dump


class TranslationLanguageWindow(QtWidgets.QDialog, TranslationLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.init_handlers()
        self.setModal(True)
        self.oldPos = self.pos()
        self.parent = parent
        self.active_button = {
            'ar': self.ArabicButton,
            'hy': self.ArmenianButton,
            'az': self.AzerbaijaniButton,
            'be': self.BelarusianButton,
            'bg': self.BulgarianButton,
            'zh-cn': self.ChineseButton,
            'hr': self.CroatianButton,
            'cs': self.CzechButton,
            'da': self.DanishButton,
            'nl': self.DutchButton,
            'en': self.EnglishButton,
            'et': self.EstonianButton,
            'fi': self.FinnishButton,
            'fr': self.FrenchButton,
            'de': self.GermanButton,
            'el': self.GreekButton,
            'hu': self.HungarianButton,
            'is': self.IcelandicButton,
            'it': self.ItalianButton,
            'ja': self.JapaneseButton,
            'ko': self.KoreanButton,
            'lt': self.LithuanianButton,
            'no': self.NorwegianButton,
            'pl': self.PolishButton,
            'pt': self.PortugueseButton,
            'ro': self.RomanianButton,
            'ru': self.RussianButton,
            'sr': self.SerbianButton,
            'sk': self.SlovakButton,
            'sl': self.SlovenianButton,
            'es': self.SpanishButton,
            'sv': self.SwedishButton,
            'tr': self.TurkishButton,
            'uk': self.UkrainianButton,
            'fil': self.FilipinoButton
        }
        self.set_active()

    def set_inactive(self):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
        button = self.active_button[properties["translation_language"]]
        button.setStyleSheet("""
        QPushButton{
            background-color: rgba(31, 37, 51, 50);
            border: 2px solid #ffffff;
            border-radius: 15px;
            color: #ffffff;
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
        button = self.active_button[properties["translation_language"]]
        button.setStyleSheet("""
QPushButton{
    background-color: #05B8CC;
    border: 2px solid #05B8CC;
    border-radius: 15px;
    color: #1f2533;
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

    def set_translation_language(self, translation_language):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
            properties["translation_language"] = translation_language
        self.set_inactive()
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
        self.IcelandicButton.clicked.connect(lambda: self.set_translation_language('is'))
        self.ItalianButton.clicked.connect(lambda: self.set_translation_language('it'))
        self.JapaneseButton.clicked.connect(lambda: self.set_translation_language('ja'))
        self.KoreanButton.clicked.connect(lambda: self.set_translation_language('ko'))
        self.LithuanianButton.clicked.connect(lambda: self.set_translation_language('lt'))
        self.NorwegianButton.clicked.connect(lambda: self.set_translation_language('no'))
        self.PolishButton.clicked.connect(lambda: self.set_translation_language('pl'))
        self.PortugueseButton.clicked.connect(lambda: self.set_translation_language('pt'))
        self.RomanianButton.clicked.connect(lambda: self.set_translation_language('ro'))
        self.RussianButton.clicked.connect(lambda: self.set_translation_language('ru'))
        self.SerbianButton.clicked.connect(lambda: self.set_translation_language('sr'))
        self.SlovakButton.clicked.connect(lambda: self.set_translation_language('sk'))
        self.SlovenianButton.clicked.connect(lambda: self.set_translation_language('sl'))
        self.SpanishButton.clicked.connect(lambda: self.set_translation_language('es'))
        self.SwedishButton.clicked.connect(lambda: self.set_translation_language('sv'))
        self.TurkishButton.clicked.connect(lambda: self.set_translation_language('tr'))
        self.UkrainianButton.clicked.connect(lambda: self.set_translation_language('uk'))
        self.FilipinoButton.clicked.connect(lambda: self.set_translation_language('fil'))

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
