import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint

from GUI.GUI_windows_source import MainWindow
from GUI.GUI_windows.ChooseFileWindow import ChooseFileWindow
from GUI.GUI_windows.ErrorMessageWindow import ErrorMessageWindow
from GUI.GUI_windows.SuccessMessageWindow import SuccessMessageWindow

from scripts.loc_cutter import cutter_main
from scripts.loc_translator import writing_translation, translate_line
from scripts.loc_putter import put_lines
from scripts.utils import check_new_line_sym_ending, paradox_mod_way_to_content, check_if_line_translated


class MainApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.init_handlers()
        self.init_helpers()
        self.oldPos = self.pos ()
        self.show()
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

    def progressbar_set_maximum(self, max):
        for i in self.bar:
            i.setMaximum(max)

    def init_handlers(self):
        self.LocalizeButton.clicked.connect(self.start_local)
        self.FileSelectionButton.clicked.connect(self.show_choose_file_window)
        self.NextStringButton.clicked.connect(self.pointer_inc)
        self.PreviousString.clicked.connect(self.pointer_red)
        self.ExitButton.clicked.connect(self.close)
        self.RollUpButton.clicked.connect(self.showMinimized)

    def init_helpers(self):
        self.PreviousString.setEnabled(False)
        self.NextStringButton.setEnabled(False)
        self.StringOrder.setText('0')

    def show_system_message(self, mes_type, text, label=None):
        self.system_messages[mes_type].show()
        self.system_messages[mes_type].ErrorMessageLine.setText(text)
        if label: self.system_messages[mes_type].ErrorLabel.setText(label)
        self.system_messages[mes_type].repaint()

    def show_choose_file_window(self):
        choose_file_window = ChooseFileWindow(self)
        choose_file_window.show()

    def get_steam_id(self, path):
        self.ModIDLine.setText(path)

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
        while self.pointer < len(self.orig_text)-self.orig_text[self.pointer:].count('\n'):
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
        elems = [self.LocalizeButton, self.OriginalString, self.TranslateString,
                 self.EditString, self.ModIDLine, self.StringOrder]
        text = ['Локализировать'] + ['']*4 + ['0']
        for elem, line in zip(elems, text):
            elem.setText(line)
            elem.repaint()
        self.LocalizeButton.disconnect()
        self.LocalizeButton.clicked.connect(self.start_local)
        self.pointer = 0
        self.orig_text, self.machine_text, self.user_text = [], [],[]

    def write_translation(self):
        try:
            self.user_text[self.pointer] = check_new_line_sym_ending(self.EditString.toPlainText())
            writing_translation(self.user_text)
            put_lines()
            self.show_system_message('success', 'Файл перевода успешно записан')
            self.clean_state()
        except FileNotFoundError as Error:
            if self.orig_text:
                self.show_system_message('error', 'Перевод уже был записан')
            else:
                self.show_system_message('error', 'Ошибка записи файла. Нет перевода.')
        except IndexError as Error:
            self.show_system_message('error', 'Вы ещё не закончили перевод')

    def start_local(self):
        try:
            workshop_id = self.ModIDLine.text()
            path = paradox_mod_way_to_content(workshop_id)
            self.orig_text = cutter_main(path, workshop_id)
            self.progressbar_set_maximum(len(self.orig_text))
        except FileNotFoundError as Error:
            self.show_system_message('error', 'Вы не выбрали мод')
        else:
            self.NextStringButton.setEnabled(True)
            self.show_system_message('success', 'Идет процесс перевода', 'Перевод')
            self.LocalizeButton.setText('Закончить перевод')
            self.LocalizeButton.repaint()
            self.LocalizeButton.disconnect()
            self.LocalizeButton.clicked.connect(self.write_translation)
            self.check_new_line_symbol_string(True)
            self.user_text.append(translate_line(self.orig_text[self.pointer]))
            self.machine_text.append(check_if_line_translated(self.orig_text[self.pointer], self.user_text[-1]))
            self.set_lines()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()