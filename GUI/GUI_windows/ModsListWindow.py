"""
                            ↓ Инициализация данных ↓
"""

from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import ModsList

from GUI.GUI_windows.AcceptMessageWindow import AcceptMessageWindow

from functools import partial
from os import listdir
import copy

from scripts.mods_sorting import prep_data, sorting
from scripts.db import get_info_from_db, get_mods_from_playset
from scripts.utils import paradox_folder, open_zip_file, mod_name_wrap, get_collection_data, scan_for_files,\
                          remove_unpacked_files, collection_append, get_total_value
from scripts.cutter import parser_main
from scripts.stylesheets import mod_name_style, mod_avtivation_status_style, mod_sorting_status_style
from scripts.messeges import call_success_message, call_error_message
from scripts.pictures import get_thumbnail


class ModsListWindow(QtWidgets.QDialog, ModsList.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers()
        self.message = None

        self.collection = get_collection_data()
        self.playsets = self.playset_check()
        self.modList, self.game_data, self.dlc_load, self.playset = prep_data(paradox_folder, list(self.playsets.items())[0])
        self.grid = self.gridLayout
        self.grid.setSpacing(10)
        self.buttons = {}
        self.generator = copy.copy(self.modList)
        self.checkboxes = []
        self.string = self.StringsList.text().split('.')
        self.PlaysetsList.view().parentWidget().setStyleSheet("background: #5abe41;")
        self.borders = {'blue': 'border: 3px solid #05B8CC;',
                        'green': 'border: 3px solid #5abe41;',
                        'gray': 'border: 3px solid gray'}
        self.switch = {
            True: {
                'act_switcher': lambda: self.ActivationSwticherButton.setText(self.string[0]),
                'reversing': lambda: self.ReverseSortingButton.setText('Z-A')
            },
            False: {
                'act_switcher': lambda: self.ActivationSwticherButton.setText(self.string[1]),
                'reversing': lambda: self.ReverseSortingButton.setText('A-Z')
            }
        }
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.switch[self.ReverseSortingButton.isChecked()]['reversing']()
        self.check_enabling_status()
        self.paint_elements()

    def init_handlers(self):
        self.ReverseSortingButton.setCheckable(True)
        self.ActivationSwticherButton.setCheckable(True)
        self.ExitButton.clicked.connect(self.close)
        self.SortButton.clicked.connect(self.make_sort)
        self.ActivationSwticherButton.clicked.connect(self.activation_switcher)
        self.ReverseSortingButton.clicked.connect(self.reversing)
        self.WindowMoveButton.installEventFilter(self)
        self.SearchLine.textChanged.connect(self.sync_lineEdit)
        self.PlaysetsList.activated[str].connect(self.update_mod_list)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_2_Modifications'))
        self.ResetButton.clicked.connect(self.reset_sorting_requiring)

    def playset_check(self):
        playsets = {
            elem[0]: {
                'name': elem[1],
                'isActive': elem[2],
            } for elem in get_info_from_db('get_playset_list')
        }
        for index, elem in enumerate(playsets.items()):
            self.PlaysetsList.addItem(elem[1]['name'])
            self.PlaysetsList.setItemData(index, elem[0])
        return playsets

    def update_mod_list(self):
        self.modList, self.game_data, self.dlc_load, self.playset = prep_data(paradox_folder, (self.PlaysetsList.currentData(),
                                                                              self.playsets[self.PlaysetsList.currentData()]))
        self.checkboxes = []
        self.check_enabling_status()
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.generator = copy.copy(self.modList)
        self.clean()
        self.paint_elements()

    def call_accept_message(self, message):
        types = {
            'collection_append': lambda: self.collection_append(message[1], message[-1]),
        }
        window = AcceptMessageWindow(self, message, types[message[0]])
        window.show()

    def collection_append(self, mod_name, mod_id, hash_key=None):
        """
                    Функция находит все переводимые файлы выбранной модификации,
                    создает для каждого временную папку в Коллекции
                    и сохраняет данные в базу данных
        """
        mod_path = get_mods_from_playset('get_mod_path', mod_name)[0][0].replace('/', '\\')
        images = get_info_from_db('get_images')
        for image_data in images:
            if image_data[2] == mod_id:
                hash_key = image_data[0]
                break

        if '.zip' in listdir(mod_path)[-1]:
            open_zip_file(f'{mod_path}\\{listdir(mod_path)[-1]}')

        try:
            for file_path in scan_for_files(mod_path):
                parser_main(mod_path, mod_id, file_path)
                collection_append(mod_id, hash_key, mod_name)
            message = 'files_was_added'
            call_success_message(self, message)
            self.findChild(QtWidgets.QDialog).close()
            self.close()

        except FileNotFoundError:
            message = 'files_not_found'
            call_error_message(self, message)
            self.findChild(QtWidgets.QDialog).close()

        if '.zip' in '|'.join(listdir(mod_path)):
            remove_unpacked_files(mod_path)

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

    def clean(self):
        for elem in reversed(range(self.gridLayout.count())):
            self.grid.itemAt(elem).widget().setParent(None)

    def search(self, text):
        self.generator = list(filter(lambda elem: text.lower() in elem.mod_name.lower(), self.modList))

    def sync_lineEdit(self, text):
        self.clean()
        self.search(text)
        self.paint_elements()

    def print_mod_name(self, index, mod, value):
        thumbnail = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(get_thumbnail(mod.hash_key))
        self.buttons[f'{mod.mod_name}'] = QtWidgets.QPushButton(mod_name_wrap(mod.mod_name, 35))

        message = ('collection_append', mod.mod_name, mod.mod_id)
        self.buttons[f'{mod.mod_name}'].clicked.connect(partial(self.call_accept_message, message))

        pixmap = pixmap.scaled(160, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        thumbnail.setPixmap(pixmap)
        if value == 0:
            thumbnail.setStyleSheet(self.borders['gray'])
        elif value >= 100:
            thumbnail.setStyleSheet(self.borders['green'])
        elif value < 100:
            thumbnail.setStyleSheet(self.borders['blue'])
        mod_name_style(self.buttons[f'{mod.mod_name}'])

        self.grid.addWidget(thumbnail, index + 1, 1)
        self.grid.addWidget(self.buttons[f'{mod.mod_name}'], index + 1, 2, 1, 5)

    def paint_elements(self):
        for index, mod in enumerate(self.generator):
            value = 0
            try:
                value = get_total_value(self.collection[mod.mod_id]) + 0.001   # for mark it as added to Collection if it's not started
            except KeyError:
                pass
            self.print_mod_name(index, mod, value)
        # print_checkboxes(self):
            checkbox1 = QtWidgets.QCheckBox()
            checkbox2 = QtWidgets.QCheckBox()
            try:
                checkbox1.setChecked(mod.checkboxes[0][0].isChecked())
                checkbox2.setChecked(mod.checkboxes[0][1].isChecked())
            except AttributeError:
                checkbox1.setChecked(mod.isEnabled)
                checkbox2.setChecked(mod.sortRequired)
            mod_avtivation_status_style(checkbox1)
            mod_sorting_status_style(checkbox2)

            self.grid.addWidget(checkbox1, index + 1, 6)
            self.grid.addWidget(checkbox2, index + 1, 7)

            mod.checkboxes[0][0] = checkbox1
            mod.checkboxes[0][1] = checkbox2

    """
                                ↓ Сортировка списка модификаций ↓
    """

    def reversing(self):
        self.ReverseSortingButton.setChecked(self.ReverseSortingButton.isChecked())
        self.switch[self.ReverseSortingButton.isChecked()]['reversing']()

    def check_enabling_status(self):
        disabled_mods = list(filter(lambda x: x.isEnabled is False, self.modList))
        self.ActivationSwticherButton.setChecked(not len(disabled_mods) >= 1)

    def activation_switcher(self):
        for mod in self.modList:
            mod.isEnabled = self.ActivationSwticherButton.isChecked()
            mod.checkboxes[0][0].setChecked(self.ActivationSwticherButton.isChecked())
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.ActivationSwticherButton.setChecked(self.ActivationSwticherButton.isChecked())

    def reset_sorting_requiring(self):
        for mod in self.modList:
            mod.sortRequired = True
            mod.checkboxes[0][1].setChecked(True)

    def make_sort(self):
        for mod in self.modList:
            mod.isEnabled = mod.checkboxes[0][0].isChecked()
            mod.sortRequired = mod.checkboxes[0][1].isChecked()
        try:
            status = sorting(self.modList, self.game_data, self.dlc_load, self.playset,
                             self.ReverseSortingButton.isChecked())
            if status in 'mods_was_sorted':
                message = status
                call_success_message(self, message)
            else:
                message = status
                call_error_message(self, message)
        except FileNotFoundError as error:
            message = 'FileNotFoundError'
            self.message = error.args[0]
            call_error_message(self, message)
        self.update_mod_list()
