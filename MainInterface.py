import sys

from PyQt5 import QtWidgets

from GUI import main_window_design
from GUI.GUI_windows.ChooseFileWindow import ChooseFileWindow

from scripts.loc_cutter import cutter_main
from scripts.loc_translator import writing_translation, translating_file
from scripts.loc_putter import put_lines
from scripts.utils import STELLARIS, check_new_line_sym_ending


class MainApp(QtWidgets.QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()
        #self.init_helpers()
        self.pointer = 0
        self.orig_text = self.machine_text = self.user_text = []

    def init_handlers(self):
        self.LocalizeButton.clicked.connect(self.start_local)
        self.FileSelectionButton.clicked.connect(self.show_choose_file_window)
        self.NextStringButton.clicked.connect(self.pointer_inc)
        self.PreviousString.clicked.connect(self.pointer_red)

    def init_helpers(self):
        self.lineEdit.setText(STELLARIS)

    def show_choose_file_window(self):
        choose_file_window = ChooseFileWindow(self)
        choose_file_window.show()

    def get_steam_id(self, path):
        self.FilePathString.setText(path)

    def set_lines(self):
        self.OriginalString.setText(self.orig_text[self.pointer])
        self.TranslateString.setText(self.machine_text[self.pointer])
        self.EditString.setText(self.user_text[self.pointer])

    def check_new_line_symbol_string(self, value):
        while True:
            if self.user_text[self.pointer].startswith('\n'):
                if value is True: self.pointer += 1
                if value is False: self.pointer -= 1
                continue
            break

    def pointer_inc(self):
        self.PreviousString.setEnabled(True)
        try:
            self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
            self.pointer += 1
            self.check_new_line_symbol_string(True)
            self.set_lines()
        except IndexError as Error:
            self.NextStringButton.setEnabled(False)

    def pointer_red(self):
        self.NextStringButton.setEnabled(True)
        try:
            self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
            self.pointer -= 1
            self.check_new_line_symbol_string(False)
            self.set_lines()
        except IndexError as Error:
            self.PreviousString.setEnabled(False)

    def write_translation(self):
        try:
            writing_translation(self.user_text)
            put_lines()
            self.EditString.setText('Файл записан.')
        except FileNotFoundError as Error:
            if self.orig_text:
                self.EditString.setText('Перевод уже был записан')
                self.EditString.repaint()
            else:
                self.EditString.setText('Ошибка записи файла. Нет перевода.')
                self.EditString.repaint()

    def start_local(self):
        self.EditString.setText('Идет процесс перевода')
        self.EditString.repaint()
        self.LocalizeButton.setText('Закончить перевод')
        self.LocalizeButton.repaint()
        self.LocalizeButton.disconnect()
        self.LocalizeButton.clicked.connect(self.write_translation)
        workshop_id = self.FilePathString.text()
        cutter_main(workshop_id)
        self.orig_text, self.machine_text, self.user_text = translating_file()
        self.check_new_line_symbol_string(True)
        self.set_lines()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()