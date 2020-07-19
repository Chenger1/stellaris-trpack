import sys
from time import sleep

from PyQt5 import QtWidgets

from GUI import main_window_design
from scripts.loc_cutter import cutter_main
from scripts.loc_translator import writing_translation, translating_file
from scripts.loc_putter import put_lines
from scripts.utils import STELLARIS, get_mod_id


class MainApp(QtWidgets.QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()
        self.init_helpers()
        self.pointer = 0
        self.orig_text = self.machine_text = self.user_text = []

    def init_handlers(self):
        self.pushButton_2.clicked.connect(self.start_local)
        self.pushButton_5.clicked.connect(self.choose_file)
        self.pushButton_6.clicked.connect(self.pointer_inc)
        self.pushButton_7.clicked.connect(self.pointer_red)

    def init_helpers(self):
        self.lineEdit.setText(STELLARIS)

    def choose_file(self):
        f_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        mod_id = get_mod_id(f_patch)
        self.lineEdit_2.setText(mod_id)

    def set_lines(self):
        self.textEdit.setText(self.orig_text[self.pointer])
        self.textEdit_2.setText(self.machine_text[self.pointer])
        self.textEdit_3.setText(self.user_text[self.pointer])

    def check_line_translating(self, value):
        while True:
            if self.user_text[self.pointer].startswith('\n'):
                if value is True: self.pointer += 1
                if value is False: self.pointer -= 1
                continue
            break

    def pointer_inc(self):
        self.pushButton_7.setEnabled(True)
        try:
            self.user_text[self.pointer] = self.textEdit_3.toPlainText()
            self.pointer += 1
            self.check_line_translating(True)
            self.set_lines()
        except IndexError as Error:
            self.pushButton_6.setEnabled(False)

    def pointer_red(self):
        self.pushButton_6.setEnabled(True)
        try:
            self.user_text[self.pointer] = self.textEdit_3.toPlainText()
            self.pointer -= 1
            self.check_line_translating(False)
            self.set_lines()
        except IndexError as Error:
            self.pushButton_7.setEnabled(False)

    def write_translation(self):
        writing_translation(self.user_text)
        put_lines()
        self.textEdit_3.setText('Файл записан.')

    def start_local(self):
        self.textEdit_3.setText('Идет процесс перевода')
        self.textEdit_3.repaint()
        self.pushButton_2.setText('Закончить перевод')
        self.pushButton_2.repaint()
        self.pushButton_2.disconnect()
        self.pushButton_2.clicked.connect(self.write_translation)
        workshop_id = self.lineEdit_2.text()
        cutter_main(workshop_id)
        self.orig_text, self.machine_text, self.user_text = translating_file()
        self.check_line_translating(True)
        self.set_lines()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()