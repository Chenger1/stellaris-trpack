import sys

from PyQt5 import QtWidgets

from GUI.GUI_windows_source import MainWindow
from GUI.GUI_windows.ChooseFileWindow import ChooseFileWindow
from GUI.GUI_windows.ErrorMessageWindow import ErrorMessageWindow
from GUI.GUI_windows.SuccessMessageWindow import SuccessMessageWindow

from scripts.loc_cutter import cutter_main
from scripts.loc_translator import writing_translation, translate_line
from scripts.loc_putter import put_lines
from scripts.utils import STELLARIS, check_new_line_sym_ending


class MainApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()
        self.init_helpers()
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text = [], [], []
        self.ErrorMessage = ErrorMessageWindow(self)
        self.SuccessMessage = SuccessMessageWindow(self)
        self.system_messages = {
            'error': self.ErrorMessage,
            'success': self.SuccessMessage,
        }

    def init_handlers(self):
        self.LocalizeButton.clicked.connect(self.start_local)
        self.FileSelectionButton.clicked.connect(self.show_choose_file_window)
        self.NextStringButton.clicked.connect(self.pointer_inc)
        self.PreviousString.clicked.connect(self.pointer_red)

    def init_helpers(self):
        #self.lineEdit.setText(STELLARIS)
        self.PreviousString.setEnabled(False)
        self.NextStringButton.setEnabled(False)

    def show_system_message(self, mes_type, text):
        self.system_messages[mes_type].show()
        self.system_messages[mes_type].ErrorMessageLine.setText(text)
        self.system_messages[mes_type].repaint()

    def show_choose_file_window(self):
        choose_file_window = ChooseFileWindow(self)
        choose_file_window.show()

    def get_steam_id(self, path):
        self.ModIDLine.setText(path)

    def set_lines(self):
        self.OriginalString.setText(self.orig_text[self.pointer])
        self.TranslateString.setText(self.machine_text[self.pointer])
        self.EditString.setText(self.user_text[self.pointer])

    def check_new_line_symbol_string(self, value):
        while True:
            if self.orig_text[self.pointer].startswith('\n'):
                if value is True:
                    self.pointer += 1
                    if self.pointer > len(self.machine_text)-1:
                        self.machine_text.append('\n')
                        self.user_text.append('\n')
                if value is False:
                    self.pointer -= 1
                continue
            break

    def pointer_inc(self):
        self.PreviousString.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer += 1
        try:
            if self.pointer > len(self.orig_text)-2:
                self.NextStringButton.setEnabled(False)
            self.check_new_line_symbol_string(True)
            self.set_lines()
        except IndexError as Error:
            if self.pointer > len(self.orig_text)-2:
                self.NextStringButton.setEnabled(False)
            self.check_new_line_symbol_string(True)
            self.machine_text.append(translate_line(self.orig_text[self.pointer]))
            self.user_text.append(self.machine_text[-1])
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

    def write_translation(self):
        try:
            self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
            writing_translation(self.user_text)
            put_lines()
            self.show_system_message('success', 'Файл перевода успешно записан')
        except FileNotFoundError as Error:
            if self.orig_text:
                self.show_system_message('error', 'Перевод уже был записан')
            else:
                self.show_system_message('errors', 'Ошибка записи файла. Нет перевода.')
        except IndexError as Error:
            self.show_system_message('error', 'Вы ещё не закончили перевод')

    def start_local(self):
        try:
            workshop_id = self.ModIDLine.text()
            self.orig_text = cutter_main(workshop_id)
        except FileNotFoundError as Error:
            self.show_system_message('error', 'Вы не выбрали мод')
        else:
            self.NextStringButton.setEnabled(True)
            self.EditString.setText('Идет процесс перевода')
            self.EditString.repaint()
            self.LocalizeButton.setText('Закончить перевод')
            self.LocalizeButton.repaint()
            self.LocalizeButton.disconnect()
            self.LocalizeButton.clicked.connect(self.write_translation)
            self.check_new_line_symbol_string(True)
            self.machine_text.append(translate_line(self.orig_text[self.pointer]))
            self.user_text.append(self.machine_text[-1])
            self.set_lines()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()