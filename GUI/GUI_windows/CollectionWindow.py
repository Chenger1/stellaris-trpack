from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import Collection
from GUI.GUI_windows.AcceptWindow import AcceptWindow

from scripts.utils import get_collection, set_data, set_data_style, set_button_style, set_complete_style, \
    set_incomplete_style, create_separator, set_files_not_found_style, local_mod_rename

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
        steam_id = QtWidgets.QTextEdit(mod_id)
        steam_id.setAlignment(QtCore.Qt.AlignCenter)
        status = QtWidgets.QProgressBar()
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
        if self.collection[mod_id]['file_name_list']:
            for file_name in self.collection[mod_id]['file_name_list']:
                file_name_index = self.collection[mod_id]['file_name_list'].index(file_name)
                if '.yml' not in file_name.split('_l_english.yml')[0]:
                    file_name = QtWidgets.QTextEdit(file_name.split('_l_english.yml')[0])
                else:
                    file_name = QtWidgets.QTextEdit(file_name.split('l_english_')[-1].split('.yml')[0])
                file_name.setAlignment(QtCore.Qt.AlignRight)
                status = QtWidgets.QProgressBar()
                status.setValue(self.collection[mod_id]['file_tr_status_list'][file_name_index])
                set_data_style(file_name)
                if status.value() != 100:
                    set_incomplete_style(status)
                else:
                    set_complete_style(status)
                grid.addWidget(file_name, self.row_index + 1, 6)
                grid.addWidget(status, self.row_index + 1, 7)
                self.row_index += 1
        else:
            files_not_found = QtWidgets.QTextEdit(f"{'—' * 8}")
            files_not_found.setAlignment(QtCore.Qt.AlignRight)
            set_files_not_found_style(files_not_found)
            grid.addWidget(files_not_found, self.row_index + 1, 6)

    def print_name_lists(self, grid, mod_id):
        if self.collection[mod_id]['name_lists_list']:
            for name_list in self.collection[mod_id]['name_lists_list']:
                name_list_index = self.collection[mod_id]['name_lists_list'].index(name_list)
                name_list = QtWidgets.QTextEdit(name_list.split('_namelist.txt')[0])
                name_list.setAlignment(QtCore.Qt.AlignRight)
                status = QtWidgets.QProgressBar()
                status.setValue(self.collection[mod_id]['name_list_tr_status_list'][name_list_index])
                set_data_style(name_list)
                if status.value() != 100:
                    set_incomplete_style(status)
                else:
                    set_complete_style(status)
                grid.addWidget(name_list, self.row_index + 1, 6)
                grid.addWidget(status, self.row_index + 1, 7)
                self.row_index += 1
        else:
            files_not_found = QtWidgets.QTextEdit(f"{'—' * 8}")
            files_not_found.setAlignment(QtCore.Qt.AlignRight)
            set_files_not_found_style(files_not_found)
            grid.addWidget(files_not_found, self.row_index + 1, 6)

    def clean(self, grid):
        self.CollectionLabel.show()
        self.CollectionNameLabel.show()
        self.StatusLabel.show()
        self.ContinueButton.clicked.connect(lambda: self.clean(grid))
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)

    def rename(self, grid):
        self.CollectionLabel.hide()
        self.CollectionNameLabel.hide()
        self.StatusLabel.hide()
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)
        label = QtWidgets.QLabel(self.CollectionNameLabel.text())
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setFont(QtGui.QFont("Arkhip", 14))
        label.setStyleSheet("""
            QLabel{
        color: white;    
        }
        """)
        grid.addWidget(label, self.row_index + 1, 6)
        input_text = QtWidgets.QTextEdit('Новое имя')
        input_text.setAlignment(QtCore.Qt.AlignCenter)
        input_text.setFont(QtGui.QFont("Arkhip", 12))
        input_text.setStyleSheet("""
            QTextEdit{
        border: 1px solid #05B8CC;
        border-radius: 20px;
        color: white;
        max-height: 40px;    
        }
        """)
        grid.addWidget(input_text, self.row_index + 2, 6)
        self.ContinueButton.clicked.connect(lambda: local_mod_rename(input_text.toPlainText()))

    def paint_elements(self):
        grid = self.gridLayout
        options = self.OptionsListComboBox
        grid.setSpacing(10)
        self.clean(grid)
        for mod_id in self.collection:
            mod_name = QtWidgets.QTextEdit(self.collection[mod_id]['mod_name'])
            separator = create_separator()
            set_data_style(mod_name)
            self.row_index += 1
            grid.addWidget(mod_name, self.row_index + 1, 1, 1, 4)
            if options.currentText() in options.itemText(0):
                self.print_mod_id(grid, mod_id)
                grid.addWidget(separator, self.row_index + 1, 6)
            elif options.currentText() in options.itemText(1):
                self.print_files_names(grid, mod_id)
                grid.addWidget(separator, self.row_index + 1, 6)
            elif options.currentText() in options.itemText(2):
                self.print_name_lists(grid, mod_id)
                grid.addWidget(separator, self.row_index + 1, 6)
            elif options.currentText() in options.itemText(3):
                self.rename(grid)
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
