import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

import design
from scripts.loc_cutter import cutter_main
from scripts.loc_translator import translating_file
from scripts.loc_putter import put_lines
from scripts.utils import STELLARIS


class MainApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()
        self.init_helpers()

    def init_handlers(self):
        self.pushButton_2.clicked.connect(self.start_local)

    def init_helpers(self):
        self.lineEdit.setText(STELLARIS)

    def start_local(self):
        workshop_id = self.lineEdit_2.text()
        cutter_main(workshop_id)
        translating_file()
        put_lines()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()