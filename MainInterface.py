from sys import argv
from PyQt5 import QtWidgets, QtCore

from json.decoder import JSONDecodeError

from GUI.GUI_windows_source import MainWindow
from GUI.GUI_windows.ChooseFileWindow import ChooseFileWindow
from GUI.GUI_windows.ErrorMessageWindow import ErrorMessageWindow
from GUI.GUI_windows.SuccessMessageWindow import SuccessMessageWindow
from GUI.GUI_windows.TranslationLanguageWindow import TranslationLanguageWindow
from GUI.GUI_windows.ToolLanguageWindow import ToolLanguageWindow
from GUI.GUI_windows.ReferenceWindow import ReferenceWindow
from GUI.GUI_windows.ModsListWindow import ModsListWindow
from GUI.GUI_windows.UnfinishedTranslateWindow import UnfinishedTranslateWindow

from scripts.loc_cutter import cutter_main, cutting_lines
from scripts.loc_translator import writing_translation, translate_line
from scripts.loc_putter import put_lines
from scripts.utils import check_new_line_sym_ending, paradox_mod_way_to_content, check_if_line_translated,\
    local_mod_status, collection_append, init_collection, open_file_for_resuming, remove_extra_new_line_symbols


class MainApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.mod_status()
        self.init_handlers()
        self.init_helpers()
        self.oldPos = self.pos()
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text = [], [], []
        self.bar = [self.TprogressBar_L, self.TprogressBar_R,
                    self.BprogressBar_L, self.BprogressBar_R,
                    self.LprogressBar_T, self.LprogressBar_B,
                    self.RprogressBar_T, self.RprogressBar_B]
        self.system_messages = {
            'error': ErrorMessageWindow(self),
            'success': SuccessMessageWindow(self),
        }

    def progressbar_set_value(self):
        for i in self.bar:
            i.setValue(self.pointer if self.NextStringButton.isEnabled() is True else len(self.orig_text))

    def progressbar_set_maximum(self, max_value):
        for i in self.bar:
            i.setMaximum(max_value)

    def init_handlers(self):
        self.LocalizeButton.clicked.connect(self.start_local)
        self.FileSelectionButton.clicked.connect(self.show_choose_file_window)
        self.TranslationLanguageButton.clicked.connect(self.translation_language_window)
        self.ToolLanguageButton.clicked.connect(self.tool_language_window)
        self.ReferenceButton.clicked.connect(lambda: self.reference_window())
        self.NextStringButton.clicked.connect(self.pointer_inc)
        self.PreviousString.clicked.connect(self.pointer_red)
        self.ExitButton.clicked.connect(self.close)
        self.RollUpButton.clicked.connect(self.showMinimized)
        self.SortModListButton.clicked.connect(self.show_mods_list_window)
        self.WindowMoveButton.installEventFilter(self)

    def init_helpers(self):
        self.PreviousString.setEnabled(False)
        self.NextStringButton.setEnabled(False)
        self.StringOrder.setText('0')
        init_collection()

    def show_system_message(self, mes_type, text, label=None):
        self.system_messages[mes_type].show()
        self.system_messages[mes_type].ErrorMessageLine.setText(text)
        if label:
            self.system_messages[mes_type].ErrorLabel.setText(label)
        self.system_messages[mes_type].repaint()

    def show_choose_file_window(self):
        choose_file_window = ChooseFileWindow(self)
        choose_file_window.show()

    def show_mods_list_window(self):
        try:
            mod_list_window = ModsListWindow(self)
        except FileNotFoundError as error:
            filename = error.filename.split("\\")[-1]
            self.show_system_message('error', f'Не найден файл {filename}')
        except JSONDecodeError as error:
            self.show_system_message('error', f'{error.msg}')
        else:
            mod_list_window.show()

    def translation_language_window(self):
        translation_language_window = TranslationLanguageWindow(self)
        translation_language_window.show()

    def tool_language_window(self):
        tool_language_window = ToolLanguageWindow(self)
        tool_language_window.show()

    def reference_window(self, to_scroll='QLabel_1_Modification'):
        reference_window = ReferenceWindow(self, to_scroll)
        reference_window.show()

    def show_unfinished_translation_window(self):
        unfinished_translation_window = UnfinishedTranslateWindow(self)
        unfinished_translation_window.show()

    @staticmethod
    def mod_status():
        local_mod_status()

    def get_steam_id(self, mod_id):
        self.ModIDLine.setText(mod_id)
        data = paradox_mod_way_to_content(mod_id)
        self.ModNameLine.setText(data['name'])
        return data

    def centering_lines(self):
        self.OriginalString.setAlignment(QtCore.Qt.AlignCenter)
        self.TranslateString.setAlignment(QtCore.Qt.AlignCenter)
        self.EditString.setAlignment(QtCore.Qt.AlignCenter)

    def set_lines(self):
        self.OriginalString.setText(self.orig_text[self.pointer])
        self.TranslateString.setText(self.machine_text[self.pointer])
        self.EditString.setText(self.user_text[self.pointer])
        self.centering_lines()
        self.StringOrder.setText(f'{self.pointer}')
        self.progressbar_set_value()

    def check_new_line_symbol_string(self, value):
        while self.pointer < len(self.orig_text) - self.orig_text[self.pointer:].count('\n'):
            if self.orig_text[self.pointer].startswith('\n'):
                if value is True:
                    self.pointer += 1
                    if self.pointer > len(self.machine_text) - 1:
                        self.machine_text.append('\n')
                        self.user_text.append('\n')
                if value is False:
                    self.pointer -= 1
                continue
            break
        else:
            self.NextStringButton.setEnabled(False)
            self.pointer -= 1

    def pointer_inc(self):
        self.PreviousString.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer += 1
        try:
            self.check_new_line_symbol_string(True)
            self.set_lines()
        except IndexError as Error:
            self.check_new_line_symbol_string(True)
            self.user_text.append(translate_line(self.orig_text[self.pointer]))
            self.machine_text.append(check_if_line_translated(self.orig_text[self.pointer], self.user_text[-1]))
            self.set_lines()

    def pointer_red(self):
        self.NextStringButton.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer -= 1
        self.check_new_line_symbol_string(False)
        if self.pointer < 0:
            self.pointer = 0
            self.check_new_line_symbol_string(True)
            self.PreviousString.setEnabled(False)
        else:
            self.set_lines()

    def clean_state(self):
        elements = [self.LocalizeButton, self.ModIDLine, self.ModNameLine, self.OriginalString, self.TranslateString,
                    self.EditString, self.StringOrder]
        text = ['Локализировать'] + ['SteamWorkshop ID'] + [''] * 4 + ['0']
        for elem, line in zip(elements, text):
            elem.setText(line)
            elem.repaint()
        self.LocalizeButton.disconnect()
        self.LocalizeButton.clicked.connect(self.start_local)
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text = [], [], []

    def write_translation(self):
        try:
            self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
            writing_translation(self.user_text)
            put_lines()
            collection_append(self.ModIDLine.text(), 100, self.pointer)
            self.show_system_message('success', 'Файл перевода успешно записан')
            self.progressbar_set_maximum(0)
            self.clean_state()
        except FileNotFoundError as Error:
            if self.orig_text:
                self.show_system_message('error', 'Перевод уже был записан')
            else:
                self.show_system_message('error', 'Ошибка записи файла. Нет перевода.')
        except IndexError as Error:
            self.show_unfinished_translation_window()

    def continue_local(self, collection):
        self.pointer = collection['pointer_pos']
        self.PreviousString.setEnabled(True if self.pointer >= 1 else False)
        self.orig_text = open_file_for_resuming(collection['data']['cuttered'])
        self.machine_text = open_file_for_resuming(collection['data']['machine_text'])
        self.user_text = cutting_lines(f'{collection["data"]["folder_path"]}\\{collection["name"]}_temp',
                                       collection['file_path'])
        self.user_text = remove_extra_new_line_symbols(self.user_text)
        self.progressbar_set_maximum(len(self.orig_text))
        self.NextStringButton.setEnabled(True)
        self.LocalizeButton.setText('Закончить перевод')
        self.LocalizeButton.repaint()
        self.LocalizeButton.disconnect()
        self.LocalizeButton.clicked.connect(self.write_translation)
        self.check_new_line_symbol_string(True)
        self.set_lines()

    def start_local(self):
        try:
            workshop_id = self.ModIDLine.text()
            path = paradox_mod_way_to_content(workshop_id)['path']
            self.orig_text = cutter_main(path, workshop_id)
            self.progressbar_set_maximum(len(self.orig_text))
        except FileNotFoundError as Error:
            self.show_system_message('error', 'Вы не выбрали мод')
        else:
            self.NextStringButton.setEnabled(True)
            self.LocalizeButton.setText('Закончить перевод')
            self.LocalizeButton.repaint()
            self.LocalizeButton.disconnect()
            self.LocalizeButton.clicked.connect(self.write_translation)
            self.check_new_line_symbol_string(True)
            self.user_text.append(translate_line(self.orig_text[self.pointer]))
            self.machine_text.append(check_if_line_translated(self.orig_text[self.pointer], self.user_text[-1]))
            self.set_lines()

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


def main():
    app = QtWidgets.QApplication(argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
