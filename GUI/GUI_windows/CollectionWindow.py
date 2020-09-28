from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Collection
from GUI.GUI_windows.AcceptWindow import AcceptWindow

from scripts.utils import get_collection, set_data, local_mod_create, open_zip_file, mod_name_wrap
from scripts.stylesheets import set_name_style, set_button_style, set_complete_style, set_incomplete_style, create_separator
from scripts.messeges import call_error_message

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
        self.row_index = 0
        self.init_handlers()
        self.set_collection_name()
        self.paint_elements()
        self.message = ''

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.OptionsListComboBox.activated[str].connect(lambda: self.paint_elements())
        self.RenameCollectionButton.clicked.connect(self.local_mod_rename)
        self.ContinueButton.clicked.connect(lambda: self.clean(self.gridLayout))
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.reference_window('QLabel_2_Collection'))
        self.WindowMoveButton.installEventFilter(self)

    def call_accept_message(self, message, **kwargs):
        types = {
            'save_translation': lambda: self.start_translation(**kwargs),
            'collection_continue_translation': lambda: self.open_mod_loc(**kwargs)
        }
        window = AcceptWindow(self, message, types[message[0]])
        window.show()

    def open_mod_loc(self, **kwargs):
        if os.path.isdir(self.collection[kwargs['mod_id']].files[kwargs['file_name']]['folder_path']) is False:
            message = 'invalid_file'
            call_error_message(self, message)
        else:
            self.parent.FileNameLine.setText(self.collection[kwargs['mod_id']].files[kwargs['file_name']]['original_name'])
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

        for file_name, file_data in self.collection[mod_id].files.items():
            total_value += file_data['name_list_tr_status']
            count += 1
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
        split_setting = {
            False: lambda x, tr: x.split('_l_english.yml'),
            True: lambda x, tr: x.split(f'_l_{tr}.yml')
        }

        if self.collection[mod_id].files:
            for file_name, file_data in self.collection[mod_id].files.items():
                lang = file_data['language']

                if '.yml' not in split_setting[f'_l_{lang}.yml' in file_name](file_name, lang)[0]:
                    self.buttons[f'{mod_id}-{file_name}'] = QtWidgets.QPushButton(
                        split_setting[f'_l_{lang}.yml' in file_name](file_name, lang)[0])

                    if file_data['file_tr_status'] > 0:
                        message = ('collection_continue_translation', file_name)
                        self.buttons[f'{mod_id}-{file_name}'].clicked. \
                            connect(partial(self.call_accept_message, message, mod_id=mod_id, file_name=file_name))
                    else:
                        message = ('save_translation', file_name)
                        self.buttons[f'{mod_id}-{file_name}'].clicked. \
                            connect(partial(self.call_accept_message, message,
                                            mod_id=mod_id, file_name=file_name,
                                            base_dir=self.collection[mod_id].base_dir))
                else:
                    self.buttons[f'{mod_id}-{file_name}'] = QtWidgets.QPushButton(
                        split_setting[f'_l_{lang}.yml' in file_name](file_name, lang)[-1].split('.yml')[0])

                    self.buttons[f'{mod_id}-{file_name}'].clicked.connect(partial(self.open_mod_by_file_name))
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


        # if self.collection[mod_id]['file_name_list']:
        #     for file_name in self.collection[mod_id]['file_name_list']:
        #         lang = self.collection[mod_id]['language']
        #         file_name_index = self.collection[mod_id]['file_name_list'].index(file_name)
        #
        #         if '.yml' not in split_setting[f'_l_{lang}.yml' in file_name](file_name, lang)[0]:
        #             self.buttons[f'{mod_id}-{file_name}'] = QtWidgets.QPushButton(
        #                 split_setting[f'_l_{lang}.yml' in file_name](file_name, lang)[0])
        #
        #             if self.collection[mod_id]['file_tr_status_list'][file_name_index] > 0:
        #                 message = ('collection_continue_translation', file_name)
        #                 self.buttons[f'{mod_id}-{file_name}'].clicked. \
        #                     connect(partial(self.call_accept_message, message, mod_id=mod_id))
        #
        #             else:
        #                 message = ('save_translation', file_name)
        #                 self.buttons[f'{mod_id}-{file_name}'].clicked. \
        #                     connect(partial(self.call_accept_message, message,
        #                                     mod_id=mod_id, file_name=file_name,
        #                                     base_dir=self.collection[mod_id]['data']['base_dir']))
        #                 # self.buttons[f'{mod_id}-{file_name}'].clicked. \
        #                 #     connect(partial(self.start_translation, mod_id, file_name,
        #                 #                     self.collection[mod_id]['data']['base_dir']))
        #
        #         else:
        #             self.buttons[f'{mod_id}-{file_name}'] = QtWidgets.QPushButton(
        #                 split_setting[f'_l_{lang}.yml' in file_name](file_name, lang)[-1].split('.yml')[0])
        #
        #             self.buttons[f'{mod_id}-{file_name}'].clicked.connect(partial(self.open_mod_by_file_name))
        #         status = QtWidgets.QProgressBar()
        #
        #         # message = 'collection_continue_translation'
        #         # self.buttons[f'{mod_id}-{file_name}'].clicked.connect(partial(self.call_accept_message, message))
        #
        #         status.setValue(self.collection[mod_id]['file_tr_status_list'][file_name_index])
        #         set_button_style(self.buttons[f'{mod_id}-{file_name}'])
        #         if status.value() != 100:
        #             set_incomplete_style(status)
        #         else:
        #             set_complete_style(status)
        #         grid.addWidget(self.buttons[f'{mod_id}-{file_name}'], self.row_index + 1, 6)
        #         grid.addWidget(status, self.row_index + 1, 7)
        #         self.row_index += 1
        # else:
        #     files_not_found = QtWidgets.QPushButton(f"{'—' * 8}")
        #     status = QtWidgets.QProgressBar()
        #     set_button_style(files_not_found)
        #     set_incomplete_style(status)
        #     status.setValue(0)
        #     status.setFormat("——   ")
        #     grid.addWidget(files_not_found, self.row_index + 1, 6)
        #     grid.addWidget(status, self.row_index + 1, 7)
        #     self.row_index += 1

    def print_name_lists(self, grid, mod_id):
        if self.collection[mod_id]['name_lists_list']:
            for name_list in self.collection[mod_id]['name_lists_list']:
                name_list_index = self.collection[mod_id]['name_lists_list'].index(name_list)
                self.buttons[f'{mod_id}-{name_list}'] = QtWidgets.QPushButton(name_list.split('_namelist.txt')[0])
                status = QtWidgets.QProgressBar()
                # self.buttons[f'{mod_id}-{name_list}'].clicked.connect(partial(self.open_accept_window, mod_id))
                status.setValue(self.collection[mod_id]['name_list_tr_status_list'][name_list_index])
                set_button_style(self.buttons[f'{mod_id}-{name_list}'])
                if status.value() != 100:
                    set_incomplete_style(status)
                else:
                    set_complete_style(status)
                grid.addWidget(self.buttons[f'{mod_id}-{name_list}'], self.row_index + 1, 6)
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
            mod_name = QtWidgets.QPushButton(mod_name_wrap(mod.mod_name[0]))
            separator = create_separator()
            set_name_style(mod_name)
            self.row_index += 1
            grid.addWidget(mod_name, self.row_index+1, 1, 1, 4)
            if options.currentText() in options.itemText(0):
                self.print_mod_id(grid, mod_id)
                grid.addWidget(separator, self.row_index + 1, 6)
            elif options.currentText() in options.itemText(1):
                self.print_files_names(grid, mod_id)
                grid.addWidget(separator, self.row_index+1, 6)

        # for mod_id in self.collection:
        #     mod_name = QtWidgets.QPushButton(mod_name_wrap(self.collection[mod_id]['mod_name']))
        #     separator = create_separator()
        #     set_name_style(mod_name)
        #     self.row_index += 1
        #     grid.addWidget(mod_name, self.row_index + 1, 1, 1, 4)
        #     if options.currentText() in options.itemText(0):
        #         self.print_mod_id(grid, mod_id)
        #         grid.addWidget(separator, self.row_index + 1, 6)
        #     elif options.currentText() in options.itemText(1):
        #         self.print_files_names(grid, mod_id)
        #         grid.addWidget(separator, self.row_index + 1, 6)
        #     elif options.currentText() in options.itemText(2):
        #         self.print_name_lists(grid, mod_id)
        #         grid.addWidget(separator, self.row_index + 1, 6)
        #     elif options.currentText() in options.itemText(3):
        #         self.print_rename(grid)
        #     self.row_index += 1

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
