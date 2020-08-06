from PyQt5 import QtWidgets, QtCore
from json import load, dump

from GUI.GUI_windows_source import ToolLanguage


class ToolLanguageWindow(QtWidgets.QDialog, ToolLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.parent = parent
        self.active_button = {
            'zh-cn': self.ChineseButton,
            'en': self.EnglishButton,
            'pl': self.PolishButton,
            'ru': self.RussianButton,
            'uk': self.UkrainianButton,
        }
        self.set_active()

    def set_inactive(self):
        with open("Properties.json", 'r', encoding='utf-8') as prop:
            properties = load(prop)
        button = self.active_button[properties["tool_language"]]
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
        button = self.active_button[properties["tool_language"]]
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
            properties["tool_language"] = translation_language
        self.set_inactive()
        with open("Properties.json", 'w', encoding='utf-8') as prop:
            dump(properties, prop)
        self.set_active()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)
        self.ChineseButton.clicked.connect(lambda: self.set_translation_language('zh-cn'))
        self.EnglishButton.clicked.connect(lambda: self.set_translation_language('en'))
        self.PolishButton.clicked.connect(lambda: self.set_translation_language('pl'))
        self.RussianButton.clicked.connect(lambda: self.set_translation_language('ru'))
        self.UkrainianButton.clicked.connect(lambda: self.set_translation_language('uk'))

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