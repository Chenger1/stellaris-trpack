import sys
import copy

from PyQt5 import QtWidgets

from GUI.GUI_windows_source import MainWindow
from GUI.GUI_windows.ChooseFileWindow import ChooseFileWindow

from scripts.loc_cutter import cutter_main
from scripts.loc_translator import writing_translation, translate_line
from scripts.loc_putter import put_lines
from scripts.utils import STELLARIS, check_new_line_sym_ending


class MainApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()
        #self.init_helpers()
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text = [], [], []

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
        self.ModIDLine.setText(path)

    def set_lines(self):
        self.OriginalString.setText(self.orig_text[self.pointer])
        self.TranslateString.setText(self.machine_text[self.pointer])
        self.EditString.setText(self.user_text[self.pointer])
        print(self.machine_text)
        print(self.user_text)

    def check_new_line_symbol_string(self, value):
        while True:
            if self.orig_text[self.pointer].startswith('\n'):
                if value is True:
                    self.pointer += 1
                    if self.pointer > len(self.machine_text)-1:
                        self.machine_text.append('\n')
                        self.user_text.append('\n')
                if value is False: self.pointer -= 1
                continue
            break

    def pointer_inc(self):
        self.PreviousString.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer += 1
        try:
            self.set_lines()
        except IndexError as Error:
            self.check_new_line_symbol_string(True)
            self.machine_text.append(translate_line(self.orig_text[self.pointer]))
            self.user_text.append(copy.deepcopy(self.machine_text[-1]))
            self.set_lines()

    def pointer_red(self):
        self.NextStringButton.setEnabled(True)
        self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
        self.pointer -= 1
        if self.pointer >= 0:
            self.check_new_line_symbol_string(False)
            self.set_lines()
        else:
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
        workshop_id = self.ModIDLine.text()
        self.orig_text = cutter_main(workshop_id)
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