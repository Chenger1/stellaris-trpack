"""
                            ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import Collection

from scripts.utils import get_collection_data, mod_name_wrap, get_info_from_stack, get_total_value, \
    file_name_fix, open_file_for_resuming, find_last_file, get_collection_description, get_collection_mod_list, collection_settings_update
from scripts.stylesheets import mod_name_style, file_name_style, complete_translation_style, \
    incomplete_translation_style, create_row_separator
from scripts.messeges import call_error_message, call_accept_message
from scripts.pictures import get_thumbnail

import json
from functools import partial


class CollectionWindow(QtWidgets.QDialog, Collection.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers()
        self.message = None

        self.string = self.StringsList.text().split('.')
        self.collection = get_collection_data()
        self.set_collection_name()
        self.gridLayout.setSpacing(15)
        self.buttons = {}
        self.row_index = 0
        self.OptionsListComboBox.view().parentWidget().setStyleSheet("background: #05B8CC;")
        self.borders = {
            'blue': 'border: 3px solid #05B8CC;',
            'green': 'border: 3px solid #5abe41;',
            'gray': 'border: 3px solid gray'
        }
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.OptionsListComboBox.activated[str].connect(lambda: self.paint_elements())
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_3_Collection'))
        self.WindowMoveButton.installEventFilter(self)

    def eventFilter(self, source, event):
        """
                    Данная функция предназначена для отслеживания позиции окна
                    и его перемещения кликом по шапке
        """
        if source == self.WindowMoveButton:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.oldPos = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.oldPos is not None:
                self.move(self.pos() - self.oldPos + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.oldPos = None
        return super().eventFilter(source, event)

    """
                            ↓ Рендер ↓
    """

    def set_collection_name(self):
        with open('Properties.json', 'r', encoding='utf-8') as properties:
            properties = json.load(properties)

        self.NewNameText.setText(properties["collection_name"])
        self.NewNameText.setAlignment(QtCore.Qt.AlignCenter)
        self.CollectionNameLabel.setText(properties["collection_name"])

    def clean(self, grid):
        self.ContinueButton.setText(self.string[0])
        self.ContinueButton.disconnect()
        self.ContinueButton.clicked.connect(self.close)
        self.ContinueButton.clicked.connect(self.continue_last_translation)

        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)

    def print_mod_name(self, grid, files, value):
        thumbnail = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(get_thumbnail(files[0].hash_key))
        mod_name = QtWidgets.QPushButton(mod_name_wrap(files[0].mod_name, 35))

        pixmap = pixmap.scaled(160, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        thumbnail.setPixmap(pixmap)
        if value == 100:
            thumbnail.setStyleSheet(self.borders['green'])
        elif value < 100:
            thumbnail.setStyleSheet(self.borders['blue'])
        mod_name_style(mod_name)

        grid.addWidget(thumbnail, self.row_index + 1, 0)
        grid.addWidget(mod_name, self.row_index + 1, 1, 1, 4)

    def print_mod_id(self, grid, mod_id, value):
        self.buttons[mod_id] = QtWidgets.QPushButton(mod_id)
        status = QtWidgets.QProgressBar()

        file_name_style(self.buttons[mod_id])
        status.setValue(value)
        if status.value() != 100:
            incomplete_translation_style(status)
        else:
            complete_translation_style(status)

        grid.addWidget(self.buttons[mod_id], self.row_index + 1, 6)
        grid.addWidget(status, self.row_index + 1, 7)

        self.row_index += 1

    def files_not_found(self, grid):
        """
                    Если, вдруг, файлов для текущей опции в списке не окажется,
                    вместо них будет добавлена заглушка
        """
        button = QtWidgets.QPushButton(f"{'—' * 8}")
        status = QtWidgets.QProgressBar()

        file_name_style(button)
        incomplete_translation_style(status)
        status.setValue(0)
        status.setFormat("——   ")

        grid.addWidget(button, self.row_index + 1, 6)
        grid.addWidget(status, self.row_index + 1, 7)

        self.row_index += 1

    def print_files_names(self, grid, files, option):
        files_list = [file for file in files if option in file.type]
        if files_list:
            for file in files_list:
                button = f'{file.mod_id}-{file.original_file_name}'
                self.buttons[button] = QtWidgets.QPushButton(file_name_fix(file.original_file_name, option))

                message = ('start_translation', file, file.original_file_name)

                self.buttons[button].clicked.connect(partial(call_accept_message,
                                                             self, message,
                                                             lambda: self.start_localisation(file)))

                status = QtWidgets.QProgressBar()

                file_name_style(self.buttons[button])
                status.setValue(file.tr_status)
                if status.value() != 100:
                    incomplete_translation_style(status)
                else:
                    complete_translation_style(status)

                grid.addWidget(self.buttons[button], self.row_index + 1, 6)
                grid.addWidget(status, self.row_index + 1, 7)

                self.row_index += 1
        else:
            self.files_not_found(grid)

    def print_rename_collection(self, grid):
        name = self.CollectionNameLabel.text()
        mod_list = get_collection_mod_list(self.collection.items(), self.string[3])

        self.ContinueButton.setText(self.string[1])
        self.ModDescriptionText.setText(get_collection_description(name, self.string[2], self.string[3]))
        self.ModDescriptionText.setAlignment(QtCore.Qt.AlignCenter)
        self.ModListLabel.setText(mod_list)

        self.ContinueButton.disconnect()
        self.ContinueButton.clicked.connect(
            lambda: collection_settings_update((self.NewNameText.toPlainText(),
                                                f'{self.ModDescriptionText.toPlainText()}\n{mod_list}',
                                                self.CollectionNameLabel.text())
                                               )
        )

        grid.addWidget(self.NewNameText, 1, 0)
        grid.addWidget(self.ModDescriptionText, 2, 0)
        grid.addWidget(self.ModListLabel, 3, 0)

    def paint_elements(self):
        grid = self.gridLayout
        options = self.OptionsListComboBox
        self.clean(grid)
        self.set_collection_name()

        for mod_id, files in self.collection.items():
            value = get_total_value(files)
            self.print_mod_name(grid, files, value)
            separator = create_row_separator()

            if options.currentText() in options.itemText(0):
                self.print_mod_id(grid, mod_id, value)
                grid.addWidget(separator, self.row_index + 1, 6)

            elif options.currentText() in options.itemText(1):
                self.print_files_names(grid, files, 'localisation')
                grid.addWidget(separator, self.row_index + 1, 6)

            elif options.currentText() in options.itemText(2):
                self.print_files_names(grid, files, 'name_lists')
                grid.addWidget(separator, self.row_index + 1, 6)

            self.row_index += 1

        if options.currentText() in options.itemText(3):
            self.clean(grid)
            self.print_rename_collection(grid)

    """
                                ↓ Работа с локализациями ↓
    """

    def start_localisation(self, file):
        self.parent.orig_text = open_file_for_resuming(file.source_file_path)
        self.parent.machine_text = open_file_for_resuming(file.machine_file_path)
        self.parent.user_text = open_file_for_resuming(file.user_input_file_path)
        self.parent.pointer = file.pointer_pos
        self.parent.file = file
        self.parent.init_helpers(True)
        self.parent.progressbar_set_maximum(len(self.parent.orig_text))
        self.parent.set_lines()
        self.parent.ModIDLine.setText(file.mod_id)
        self.parent.mod_type_pixmap(file.mod_id)
        self.parent.ModNameLine.setText(file.mod_name)
        self.parent.FileNameLine.setText(file.original_file_name)

        self.findChild(QtWidgets.QDialog).close()
        self.close()

    def continue_last_translation(self):
        last_file: list = get_info_from_stack()
        if last_file:
            file = find_last_file(self.collection, last_file)
            message = ('continue_last_translation', file, file.original_file_name)
            call_accept_message(self, message, lambda: self.start_localisation(file))

        else:
            message = 'all_is_complete'
            call_error_message(self, message)
