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
from GUI.GUI_windows.AcceptMessageWindow import AcceptMessageWindow

from scripts.loc_cutter import cutter_main, cutting_loc_lines
from scripts.loc_translator import writing_translation, translate_line
from scripts.loc_putter import put_lines
from scripts.db import get_info_from_db
from scripts.utils import check_new_line_sym_ending, paradox_mod_way_to_content, check_if_line_translated,\
    generated_files_status, collection_append, open_file_for_resuming, remove_extra_new_line_symbols,\
    remove_unpacked_files, get_mod_id, open_zip_file, mod_path, move_folder, save_unfinished_machine_text, get_translation
from scripts.messeges import call_success_message, call_error_message
from scripts.pictures import thumbs_synchronize


class MainApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.init_handlers()
        self.init_helpers()
        self.oldPos = self.pos()
        self.pointer = 0
        self.mods_folder = self.get_mods_folder_path()
        self.orig_text, self.machine_text, self.user_text = [], [], []
        self.bar = [self.TprogressBar_L, self.TprogressBar_R,
                    self.BprogressBar_L, self.BprogressBar_R,
                    self.LprogressBar_T, self.LprogressBar_B,
                    self.RprogressBar_T, self.RprogressBar_B]
        self.mod_type_pixmap(self.ModIDLine.text())
        self.message = ''

    def mod_type_pixmap(self, mod_id):
        if mod_id.isdigit() or self.ModIDLine.text() == 'SteamWorkshop ID':
            self.paradox_logo.hide()
            self.steam_logo.show()
        else:
            self.paradox_logo.show()
            self.steam_logo.hide()

    def progressbar_set_value(self):
        for i in self.bar:
            i.setValue(self.pointer if self.NextStringButton.isEnabled() is True else len(self.orig_text))

    def progressbar_set_maximum(self, max_value):
        for i in self.bar:
            i.setMaximum(max_value)

    def init_handlers(self):
        self.LocalizeButton.clicked.connect(self.start_local)
        self.TranslationLanguageButton.clicked.connect(self.translation_language_window)
        self.ToolLanguageButton.clicked.connect(self.tool_language_window)
        self.CollectionButton.clicked.connect(self.show_collection_window)
        self.ManualButton.clicked.connect(self.open_file_dialog)
        self.UpdateTranslationButton.clicked.connect(self.show_update_window)
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

    def get_mods_folder_path(self):
        raw_path = get_info_from_db('get_path_to_mods', 1)[0]
        if 'SteamLibrary' not in raw_path:
            message = 'mods_not_found'
            self.message = ''
            call_error_message(self, message)
        try:
            raw_path = raw_path.split('\\')
            path = '\\'.join(raw_path[:len(raw_path) - 1]) + '\\'
        except IndexError:
            path = []
        return path

    def open_file_dialog(self):
        if self.mods_folder:
            f_path = QtWidgets.QFileDialog.getOpenFileName(directory=self.mods_folder)[0]
            if '.zip' in f_path.split('/')[-1]:
                open_zip_file(f_path)
                f_path = QtWidgets.QFileDialog.getOpenFileName(directory='/'.join(f_path.split('/')[:-1]))[0]
        else:
            f_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.choose_file(f_path)

    def choose_file(self, f_path):
        if f_path:
            mod_id = get_mod_id(f_path)
            self.ModIDLine.setText(mod_id)
            self.mod_type_pixmap(self.ModIDLine.text())

    def show_collection_window(self):
        collection_window = CollectionWindow(self)
        collection_window.show()

    def show_update_window(self):
        update_window = UpdateTranslationWindow(self)
        update_window.show()

    def show_accept_window(self, message):
        accept_window = AcceptMessageWindow(self, message)
        accept_window.show()

    def show_mods_list_window(self):
        try:
            mod_list_window = ModsListWindow(self)
        except FileNotFoundError as error:
            message = 'file_not_found'
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

    def get_steam_id(self, mod_id):
        self.ModIDLine.setText(mod_id)
        self.mod_type_pixmap(self.ModIDLine.text())
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
        except IndexError:
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
        elements = [self.ModIDLine, self.ModNameLine, self.OriginalString, self.TranslateString,
                    self.EditString, self.FileNameLine, self.StringOrder]
        text = ['SteamWorkshop ID'] + [''] * 5 + ['0']
        for elem, line in zip(elements, text):
            elem.setText(line)
            elem.repaint()
        self.LocalizeButton.show()
        self.LocalizeButton.clicked.connect(self.start_local)
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text = [], [], []
        for i in self.bar:
            i.setValue(0)
        self.FinishButton.hide()
        self.mod_type_pixmap(self.ModIDLine.text())

    def write_translation(self):
        try:
            self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
            writing_translation(self.user_text)
            put_lines()
            save_unfinished_machine_text(self.machine_text)
            move_folder()
            hashKey = tuple(filter(lambda x: x[1] in self.ModIDLine.text(), get_info_from_db('get_mod_data')))[0][0]
            collection_append(self.ModIDLine.text(), 100, self.pointer, hashKey)
            remove_unpacked_files()
            message = 'file_was_written'
            self.message = ''
            call_success_message(self, message)
            self.clean_state()
        except FileNotFoundError:
            if self.orig_text:
                message = 'translation_already_written'
                self.message = ''
                call_error_message(self, message)
            else:
                message = 'no_translation'
                self.message = ''
                call_error_message(self, message)
        except IndexError:
            message = ('save_translation', '')
            self.show_accept_window(message)

    def continue_local(self, collection):
        self.pointer = collection['file_name_pointer_pos']
        self.PreviousString.setEnabled(True if self.pointer >= 1 else False)
        self.orig_text = open_file_for_resuming(collection['cuttered'])
        self.machine_text = open_file_for_resuming(collection['machine_text'])
        self.user_text = cutting_loc_lines(f'{collection["folder_path"]}\\{collection["original_name"]}_temp',
                                       f'{mod_path}\\localisation\\{collection["final_name"]}')

        self.user_text = remove_extra_new_line_symbols(self.user_text)
        self.progressbar_set_maximum(len(self.orig_text))
        self.NextStringButton.setEnabled(True)
        self.FinishButton.show()
        self.FinishButton.disconnect()
        self.FinishButton.clicked.connect(self.write_translation)
        self.check_new_line_symbol_string(True)
        self.set_lines()
        self.LocalizeButton.hide()

    def start_local(self):
        try:
            workshop_id = self.ModIDLine.text()
            data = paradox_mod_way_to_content(workshop_id)
            self.ModNameLine.setText(data['name'])
            self.FileNameLine.setText(data['file_name'])
            self.mod_type_pixmap(self.ModIDLine.text())
            self.orig_text = cutter_main(data['path'], workshop_id, data['file_name'])
            self.progressbar_set_maximum(len(self.orig_text))
        except FileNotFoundError:
            message = 'mod_not_choosen'
            self.message = ''
            call_error_message(self, message)
        else:
            self.NextStringButton.setEnabled(True)
            self.FinishButton.show()
            self.FinishButton.disconnect()
            self.FinishButton.clicked.connect(self.write_translation)
            self.check_new_line_symbol_string(True)
            self.user_text.append(translate_line(self.orig_text[self.pointer]))
            self.machine_text.append(check_if_line_translated(self.orig_text[self.pointer], self.user_text[-1]))
            self.set_lines()
            self.LocalizeButton.hide()

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
    translator = QtCore.QTranslator(app)
    translator.load(get_translation())
    app.installTranslator(translator)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    generated_files_status()
    thumbs_synchronize()
    main()
