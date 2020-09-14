from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Collection
from GUI.GUI_windows.AcceptWindow import AcceptWindow

from scripts.utils import get_collection, set_data, set_data_style, set_button_style, set_complete_style, \
    set_incomplete_style, clean, add_separator

import os


class CollectionWindow(QtWidgets.QDialog, Collection.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.OptionsListComboBox.view().parentWidget().setStyleSheet("background: #05B8CC;")
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.collection = get_collection()
        # self.buttons = {}
        self.row_index = 0
        self.accept_window = AcceptWindow
        self.init_handlers()
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.OptionsListComboBox.activated[str].connect(lambda: self.paint_elements())
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.reference_window('QLabel_2_Collection'))
        self.WindowMoveButton.installEventFilter(self)

    def open_accept_window(self, elem):
        accept_window = AcceptWindow(self, f'Хотите продолжить перевод мода - {self.collection[elem]["name"]}',
                                     lambda: self.open_mod_loc(elem))
        accept_window.AcceptButton.setText('Да, хочу')
        accept_window.DeniedButton.setText('Нет')
        accept_window.show()

    def open_mod_loc(self, elem):
        if os.path.isdir(self.collection[elem]['data']['folder_path']) is False:
            self.parent.parent.show_system_message('error', 'Файл перевода поврежден или удален')
            self.findChild(QtWidgets.QDialog).close()
        else:
            self.parent.parent.ModIDLine.setText(elem)
            set_data(self.collection[elem])
            self.findChild(QtWidgets.QDialog).close()
            self.close()
            self.parent.parent.continue_local(self.collection[elem])

    #         # self.buttons[f'{mod_id}'] = QtWidgets.QPushButton(f'{index + 1}: {self.collection[mod_id]["name"]}')
    #         # #
    #         # set_button_style(self.buttons[f'{mod_id}'])
    #         # #
    #         # self.buttons[f'{mod_id}'].clicked.connect(partial(self.open_accept_window, mod_id))
    #         # grid.addWidget(self.buttons[f'{mod_id}'], index + 1, 3, 1, 4)

    def print_mod_id(self, grid, mod_id):
        steam_id = QtWidgets.QLineEdit(f'{" " * 12}{mod_id}')
        status = QtWidgets.QProgressBar()
        self.OptionDataLabel.setText('  ID')
        status.setValue(self.get_total_value(mod_id))
        set_data_style(steam_id)
        if status.value() != 100:
            set_incomplete_style(status)
        else:
            set_complete_style(status)
        grid.addWidget(steam_id, self.row_index + 1, 6)
        grid.addWidget(status, self.row_index + 1, 7)
        self.row_index += 1

    def get_total_value(self, mod_id):
        total_value = 0
        count = 0
        for file_value in self.collection[mod_id]["file_tr_status_list"]:
            total_value = total_value + file_value
            count += 1
        for name_list_value in self.collection[mod_id]["name_list_tr_status_list"]:
            total_value = total_value + name_list_value
            count += 1
        total_value /= count
        return total_value

    def print_files_names(self, grid, mod_id):
        for file_name in self.collection[mod_id]['file_name_list']:
            file_name_index = self.collection[mod_id]['file_name_list'].index(file_name)
            file_name = QtWidgets.QLineEdit(file_name)
            status = QtWidgets.QProgressBar()
            self.OptionDataLabel.setText('Файлы')
            status.setValue(self.collection[mod_id]['file_tr_status_list'][file_name_index])
            set_data_style(file_name)
            if status.value() != 100:
                set_incomplete_style(status)
            else:
                set_complete_style(status)
            grid.addWidget(file_name, self.row_index + 1, 6)
            grid.addWidget(status, self.row_index + 1, 7)
            self.row_index += 1

    def print_name_lists(self, grid, mod_id):
        for name_list in self.collection[mod_id]['name_lists_list']:
            name_list_index = self.collection[mod_id]['name_lists_list'].index(name_list)
            name_list = QtWidgets.QLineEdit(name_list)
            status = QtWidgets.QProgressBar()
            self.OptionDataLabel.setText('Файлы')
            status.setValue(self.collection[mod_id]['name_list_tr_status_list'][name_list_index])
            set_data_style(name_list)
            if status.value() != 100:
                set_incomplete_style(status)
            else:
                set_complete_style(status)
            grid.addWidget(name_list, self.row_index + 1, 6)
            grid.addWidget(status, self.row_index + 1, 7)
            self.row_index += 1

    def paint_elements(self):
        grid = self.gridLayout
        options = self.OptionsListComboBox
        grid.setSpacing(10)
        clean(grid)
        for mod_id in self.collection:
            separator = add_separator()
            mod_name = QtWidgets.QLineEdit(self.collection[mod_id]['mod_name'])
            set_data_style(mod_name)
            grid.addWidget(separator, self.row_index + 1, 3, 1, 4)
            self.row_index += 1
            grid.addWidget(mod_name, self.row_index + 1, 3, 1, 4)
            if options.currentText() in options.itemText(0):
                self.print_mod_id(grid, mod_id)
            elif options.currentText() in options.itemText(1):
                self.print_files_names(grid, mod_id)
            elif options.currentText() in options.itemText(2):
                self.print_name_lists(grid, mod_id)
            self.row_index += 1

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
