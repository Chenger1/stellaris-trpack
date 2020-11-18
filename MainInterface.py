# TODO Добавить обработку для нейм-листов
"""
                              ↓ Инициализация данных ↓
"""

from sys import argv
from PyQt5 import QtWidgets, QtCore

from json.decoder import JSONDecodeError

from GUI.GUI_windows_source import MainWindow
from GUI.GUI_windows.CollectionWindow import CollectionWindow
from GUI.GUI_windows.TranslationLanguageWindow import TranslationLanguageWindow
from GUI.GUI_windows.UpdateTranslationWindow import UpdateTranslationWindow
from GUI.GUI_windows.ToolLanguageWindow import ToolLanguageWindow
from GUI.GUI_windows.ReferenceWindow import ReferenceWindow
from GUI.GUI_windows.ModsListWindow import ModsListWindow

from scripts.comparer import put_lines
from scripts.utils import check_new_line_sym_ending, generated_files_init, collection_update, get_interface_lang, pop_stack
from scripts.messeges import call_success_message, call_error_message


class MainApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.init_handlers()
        self.init_helpers(False)
        self.oldPos = self.pos()
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text, self.translated = [], [], [], []
        self.bar = [
                    self.TprogressBar_L, self.TprogressBar_R,
                    self.BprogressBar_L, self.BprogressBar_R,
                    self.LprogressBar_T, self.LprogressBar_B,
                    self.RprogressBar_T, self.RprogressBar_B
                    ]
        self.key = 'new'
        self.user_text_method = {
            'new': lambda pointer: self.orig_text[pointer],
            'old': lambda pointer: self.translated[pointer]
        }
        self.mod_type_pixmap(self.ModIDLine.text())
        self.file = None
        self.message = None

    def init_handlers(self):
        self.SaveButton.clicked.connect(self.save_localisation)
        self.TranslationLanguageButton.clicked.connect(self.translation_language_window)
        self.ToolLanguageButton.clicked.connect(self.tool_language_window)
        self.CollectionButton.clicked.connect(self.show_collection_window)
        self.UpdateTranslationButton.clicked.connect(self.show_update_window)
        self.ReferenceButton.clicked.connect(lambda: self.reference_window())
        self.NextStringButton.clicked.connect(self.pointer_inc)
        self.PreviousStringButton.clicked.connect(self.pointer_red)
        self.ExitButton.clicked.connect(self.close)
        self.RollUpButton.clicked.connect(self.showMinimized)
        self.SortModListButton.clicked.connect(self.show_mods_list_window)
        self.WindowMoveButton.installEventFilter(self)

    def init_helpers(self, mode):
        self.PreviousStringButton.setEnabled(mode)
        self.NextStringButton.setEnabled(mode)

    def show_collection_window(self):
        collection_window = CollectionWindow(self)
        collection_window.show()

    def show_update_window(self):
        update_window = UpdateTranslationWindow(self)
        update_window.show()

    def show_mods_list_window(self):
        try:
            mod_list_window = ModsListWindow(self)
        except FileNotFoundError as error:
            message = 'files_not_found'
            self.message = error.filename.split("\\")[-1]
            call_error_message(self, message)
        except JSONDecodeError as error:
            message = 'JSONDecodeError'
            self.message = error.msg
            call_error_message(self, message)
        else:
            mod_list_window.show()

    def translation_language_window(self):
        translation_language_window = TranslationLanguageWindow(self)
        translation_language_window.show()

    def tool_language_window(self):
        tool_language_window = ToolLanguageWindow(self)
        tool_language_window.show()

    def reference_window(self, to_scroll='QLabel_1_Translation'):
        reference_window = ReferenceWindow(self, to_scroll)
        reference_window.show()

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
        elements = [self.ModIDLine, self.ModNameLine, self.OriginalString, self.TranslateString,
                    self.EditString, self.FileNameLine, self.StringOrder]
        text = ['SteamWorkshop ID'] + [''] * 5 + ['0']
        for elem, line in zip(elements, text):
            elem.setText(line)
            elem.repaint()
        self.pointer = 0
        self.file = None
        self.source_text, self.machine_text, self.user_text, self.translated = [], [], [], []
        self.key = 'new'
        self.user_text_method = {
            'new': lambda pointer: self.orig_text[pointer],
            'old': lambda pointer: self.translated[pointer]
        }
        for i in self.bar:
            i.setValue(0)
        self.mod_type_pixmap(self.ModIDLine.text())

    def mod_type_pixmap(self, mod_id):
        if mod_id.isdigit() or self.ModIDLine.text() == 'SteamWorkshop ID':
            self.paradox_logo.hide()
            self.steam_logo.show()
        else:
            self.paradox_logo.show()
            self.steam_logo.hide()

    def progressbar_set_maximum(self, max_value):
        for i in self.bar:
            i.setMaximum(max_value)

    def progressbar_set_value(self):
        for i in self.bar:
            i.setValue(self.pointer if self.NextStringButton.isEnabled() is True else len(self.orig_text))

    def centering_lines(self):
        self.OriginalString.setAlignment(QtCore.Qt.AlignCenter)
        self.TranslateString.setAlignment(QtCore.Qt.AlignCenter)
        self.EditString.setAlignment(QtCore.Qt.AlignCenter)

    """
                                ↓ Работа с локализациями ↓
    """

    def check_new_line_symbol_string(self, value):
        while self.pointer < len(self.orig_text) - self.orig_text[self.pointer:].count('\n'):
            if self.orig_text[self.pointer].startswith('\n'):
                if value is True:
                    self.pointer += 1
                if value is False:
                    self.pointer -= 1
                continue
            break
        else:
            self.NextStringButton.setEnabled(False)
            self.pointer -= 1

    def set_lines(self):
        self.OriginalString.setText(self.orig_text[self.pointer])
        self.TranslateString.setText(self.machine_text[self.pointer])
        self.EditString.setText(self.user_text[self.pointer] if self.user_text[self.pointer] != '\n'
                                else self.machine_text[self.pointer])
        self.centering_lines()
        self.StringOrder.setText(f'{self.pointer}')
        self.progressbar_set_value()

    def pointer_inc(self):
        self.PreviousStringButton.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer += 1
        self.check_new_line_symbol_string(True)
        self.set_lines()

    def pointer_red(self):
        self.NextStringButton.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer -= 1
        self.check_new_line_symbol_string(False)
        if self.pointer < 0:
            self.pointer = 0
            self.check_new_line_symbol_string(True)
            self.PreviousStringButton.setEnabled(False)
        else:
            self.set_lines()

    def save_localisation(self):
        try:
            self.file.tr_status = round((self.bar[0].value() / self.bar[0].maximum()) * 100) \
                                    if self.bar[0].value() != self.bar[0].maximum() \
                                    else 100    # meaning it's Complete
            self.file.pointer_pos = self.pointer
            collection_update(self.file, self.user_text)

            message = 'file_was_updated'
            call_success_message(self, message)

            if self.file.tr_status == 100:
                put_lines(self.file)
                pop_stack()

            self.clean_state()

        except AttributeError:
            message = 'no_translation'
            call_error_message(self, message)


def main():
    app = QtWidgets.QApplication(argv)
    translator = QtCore.QTranslator(app)
    translator.load(get_interface_lang())
    app.installTranslator(translator)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    generated_files_init()
    main()
