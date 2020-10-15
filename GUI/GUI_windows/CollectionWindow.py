from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import Collection
from GUI.GUI_windows.AcceptMessageWindow import AcceptMessageWindow

from scripts.utils import get_collection, set_data, local_mod_create, open_zip_file, mod_name_wrap, get_info_from_stack
from scripts.stylesheets import set_name_style, set_button_style, set_complete_style, set_incomplete_style, \
    create_separator
from scripts.messeges import call_error_message
from scripts.pictures import get_thumbnail

import os
import json
from functools import partial


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
        self.buttons = {}
        self.borders = {'blue': 'border: 3px solid #05B8CC;',
                        'green': 'border: 3px solid #5abe41;',
                        'gray': 'border: 3px solid gray'}
        self.row_index = 0
        self.init_handlers()
        self.set_collection_name()
        self.paint_elements()
        self.message = ''

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.OptionsListComboBox.activated[str].connect(lambda: self.paint_elements())
        self.RenameCollectionButton.clicked.connect(self.local_mod_rename)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_3_Collection'))
        self.WindowMoveButton.installEventFilter(self)
        self.ContinueButton.clicked.connect(self.continue_last_translation)

    def call_accept_message(self, message, **kwargs):
        types = {
            'start_translation': lambda: self.start_translation(**kwargs),
            'collection_continue_translation': lambda: self.open_mod_loc(**kwargs)
        }
        window = AcceptMessageWindow(self, message, types[message[0]])
        window.show()

    def open_mod_loc(self, **kwargs):
        if os.path.isdir(self.collection[kwargs['mod_id']].files[kwargs['file_name']]['folder_path']) is False:
            message = 'invalid_file'
            call_error_message(self, message)
        else:
            self.parent.FileNameLine.setText(
                self.collection[kwargs['mod_id']].files[kwargs['file_name']]['original_name'])
            self.parent.ModIDLine.setText(str(kwargs['mod_id']))
            self.collection[kwargs['mod_id']].files[kwargs['file_name']]['final_name'] = kwargs['file_name']
            set_data(self.collection[kwargs['mod_id']].files[kwargs['file_name']])
            self.findChild(QtWidgets.QDialog).close()
            self.close()
            self.parent.ModNameLine.setText(self.collection[kwargs['mod_id']].mod_name[0])
            self.parent.continue_local(self.collection[kwargs['mod_id']].files[kwargs['file_name']])

    def open_mod_by_id(self, mod_id):
        mod_data = self.parent.get_steam_id(str(mod_id))
        f_path = QtWidgets.QFileDialog.getOpenFileName(directory=f"{mod_data['path']}\\localisation")[0]
        if f_path:
            if '.zip' in f_path.split('/')[-1]:
                open_zip_file(f_path)
                f_path = QtWidgets.QFileDialog.getOpenFileName(directory='/'.join(f_path.split('/')[:-1]))[0]
            self.parent.choose_file(f_path)
            self.close()

    def continue_last_translation(self):
        last_mod: list = get_info_from_stack()
        if last_mod:
            message = ('collection_continue_translation', last_mod[1])
            self.call_accept_message(message, mod_id=last_mod[0], file_name=last_mod[1])
        else:
            message = 'all_is_complete'
            self.message = ''
            call_error_message(self, message)

    def print_mod_id(self, grid, mod_id):
        self.buttons[mod_id] = QtWidgets.QPushButton(f'{mod_id}')
        self.buttons[mod_id].clicked.connect(partial(self.open_mod_by_id, mod_id))
        status = QtWidgets.QProgressBar()
        status.setValue(self.get_total_value(mod_id))
        set_button_style(self.buttons[mod_id])
        if status.value() != 100:
            set_incomplete_style(status)
        else:
            set_complete_style(status)
        grid.addWidget(self.buttons[mod_id], self.row_index + 1, 6)
        grid.addWidget(status, self.row_index + 1, 7)
        self.row_index += 1

    def get_total_value(self, mod_id):
        total_value = 0
        count = 0

        for file_name, file_data in self.collection[mod_id].files.items():
            total_value += file_data['file_tr_status']
            count += 1

        # for file_name, file_data in self.collection[mod_id].files.items():
        #     total_value += file_data['name_list_tr_status']
        #     count += 1

        total_value /= count
        return total_value

    def start_translation(self, **kwargs):
        path = f'{kwargs["base_dir"]}\\{kwargs["file_name"]}'

        if os.path.exists(path) is False:
            dirs = list(filter(lambda x: os.path.isdir(f'{kwargs["base_dir"]}/{x}'), os.listdir(kwargs["base_dir"])))
            target_dir = list(filter(lambda x: kwargs["file_name"] in os.listdir(f'{kwargs["base_dir"]}/{x}'), dirs))
            path = '/'.join(f'{kwargs["base_dir"]}\\{target_dir[0]}\\{kwargs["file_name"]}'.split('\\'))

        self.parent.choose_file(path)
        self.parent.ModNameLine.setText(self.collection[kwargs['mod_id']].mod_name[0])
        self.findChild(QtWidgets.QDialog).close()
        self.close()

    def print_files_names(self, grid, mod_id):
        if self.collection[mod_id].files:
            for file_name, file_data in self.collection[mod_id].files.items():
                if '.yml' in file_name:
                    self.buttons[f'{mod_id}-{file_name}'] = QtWidgets.QPushButton(file_name.split('_l_')[0])
                    if file_data['file_tr_status'] > 0:
                        message = ('collection_continue_translation', file_name)
                        self.buttons[f'{mod_id}-{file_name}'].clicked. \
                            connect(partial(self.call_accept_message, message, mod_id=mod_id, file_name=file_name))
                    else:
                        message = ('start_translation', file_name)
                        self.buttons[f'{mod_id}-{file_name}'].clicked. \
                            connect(partial(self.call_accept_message, message,
                                            mod_id=mod_id, file_name=file_name,
                                            base_dir=self.collection[mod_id].base_dir))
                    status = QtWidgets.QProgressBar()
                    status.setValue(file_data['file_tr_status'])
                    set_button_style(self.buttons[f'{mod_id}-{file_name}'])
                    if status.value() != 100:
                        set_incomplete_style(status)
                    else:
                        set_complete_style(status)
                    grid.addWidget(self.buttons[f'{mod_id}-{file_name}'], self.row_index + 1, 6)
                    grid.addWidget(status, self.row_index + 1, 7)
                    self.row_index += 1
        else:
            files_not_found = QtWidgets.QPushButton(f"{'—' * 8}")
            status = QtWidgets.QProgressBar()
            set_button_style(files_not_found)
            set_incomplete_style(status)
            status.setValue(0)
            status.setFormat("——   ")
            grid.addWidget(files_not_found, self.row_index + 1, 6)
            grid.addWidget(status, self.row_index + 1, 7)
            self.row_index += 1

    @staticmethod
    def split_name_list(file_name):
        split_setting = ['_namelist', '_name_list', '_names', 'name_list_']
        for setting in split_setting:
            if setting in file_name:
                return file_name.split(setting)[0]

    def print_name_lists(self, grid, mod_id):
        if self.collection[mod_id].files:
            for file_name, file_data in self.collection[mod_id].files.items():
                if '.txt' in file_name:
                    self.buttons[f'{mod_id}-{file_name}'] = QtWidgets.QPushButton(self.split_name_list(file_name))
                    if file_data['file_tr_status'] > 0:
                        message = ('collection_continue_translation', file_name)
                        self.buttons[f'{mod_id}-{file_name}'].clicked. \
                            connect(partial(self.call_accept_message, message, mod_id=mod_id, file_name=file_name))
                    else:
                        message = ('start_translation', file_name)
                        self.buttons[f'{mod_id}-{file_name}'].clicked. \
                            connect(partial(self.call_accept_message, message,
                                            mod_id=mod_id, file_name=file_name,
                                            base_dir=self.collection[mod_id].base_dir))
                    status = QtWidgets.QProgressBar()
                    status.setValue(file_data['file_tr_status'])
                    set_button_style(self.buttons[f'{mod_id}-{file_name}'])
                    if status.value() != 100:
                        set_incomplete_style(status)
                    else:
                        set_complete_style(status)
                    grid.addWidget(self.buttons[f'{mod_id}-{file_name}'], self.row_index + 1, 6)
                    grid.addWidget(status, self.row_index + 1, 7)
                    self.row_index += 1

                    # TODO print 'files_not_found' if mods are exists, but another type
        else:
            files_not_found = QtWidgets.QPushButton(f"{'—' * 8}")
            status = QtWidgets.QProgressBar()
            set_button_style(files_not_found)
            set_incomplete_style(status)
            status.setValue(0)
            status.setFormat("——   ")
            grid.addWidget(files_not_found, self.row_index + 1, 6)
            grid.addWidget(status, self.row_index + 1, 7)
            self.row_index += 1

    def clean(self, grid):
        self.CollectionLabel.show()
        self.CollectionNameLabel.show()
        self.StatusLabel.show()
        self.ContinueButton.show()
        self.RenameCollectionButton.hide()
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)

    def set_collection_name(self):
        with open('Properties.json', 'r', encoding='utf-8') as prop:
            properties = json.load(prop)
            self.NewNameText.setText(properties["collection_name"])
            self.NewNameText.setAlignment(QtCore.Qt.AlignCenter)
            self.CollectionNameLabel.setText(properties["collection_name"])

    def local_mod_rename(self):
        with open('Properties.json', 'r', encoding='utf-8') as prop:
            properties = json.load(prop)
            properties["collection_name"] = self.NewNameText.toPlainText()
        with open("Properties.json", 'w', encoding='utf-8') as prop:
            json.dump(properties, prop)
        self.set_collection_name()
        local_mod_create()

    def print_rename(self, grid):
        self.CollectionLabel.hide()
        self.CollectionNameLabel.hide()
        self.StatusLabel.hide()
        self.ContinueButton.hide()
        self.RenameCollectionButton.show()
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)
        grid.addWidget(self.NewNameText)

    def paint_elements(self):
        grid = self.gridLayout
        options = self.OptionsListComboBox
        grid.setSpacing(10)
        self.clean(grid)
        for mod_id, mod in self.collection.items():
            label = QtWidgets.QLabel(self)
            value = self.get_total_value(mod_id)
            if value == 100:
                label.setStyleSheet(self.borders['green'])
            elif value < 100:
                label.setStyleSheet(self.borders['blue'])
            pixmap = QtGui.QPixmap(get_thumbnail(mod.hashKey))
            pixmap = pixmap.scaled(160, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            label.setPixmap(pixmap)
            mod_name = QtWidgets.QPushButton(mod_name_wrap(mod.mod_name[0]))
            separator = create_separator()
            set_name_style(mod_name)
            self.row_index += 1
            grid.addWidget(label, self.row_index + 1, 0)
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
                self.print_rename(grid)
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
