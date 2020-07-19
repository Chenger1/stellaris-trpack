import sys

from PyQt5 import QtWidgets

from GUI import main_window_design
from scripts.loc_cutter import cutter_main
from scripts.loc_translator import translating_file
from scripts.loc_putter import put_lines
from scripts.utils import STELLARIS, get_mod_id

#681576508
class MainApp(QtWidgets.QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()
        self.init_helpers()

    def init_handlers(self):
        self.pushButton_2.clicked.connect(self.start_local)
        self.pushButton_5.clicked.connect(self.choose_file)

    def init_helpers(self):
        self.lineEdit.setText(STELLARIS)

    def choose_file(self):
        f_patch = QtWidgets.QFileDialog.getOpenFileName()[0]
        mod_id = get_mod_id(f_patch)
        self.lineEdit_2.setText(mod_id)

    def start_local(self):
        workshop_id = self.lineEdit_2.text()
        cutter_main(workshop_id)
        translating_file()
        put_lines()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()