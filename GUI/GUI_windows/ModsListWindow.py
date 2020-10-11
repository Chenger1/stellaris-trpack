from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import ModsList

from functools import partial
import copy

from scripts.mods_sorting import set_settings, prep_data, sorting
from scripts.db import get_info_from_db, get_mods_from_playset
from scripts.utils import get_mod_id, open_zip_file, mod_name_wrap, get_collection
from scripts.stylesheets import set_name_style, mod_avtivation_status_style, mod_sorting_status_style
from scripts.messeges import call_success_message, call_error_message
from scripts.pictures import get_thumbnail


class ModsListWindow(QtWidgets.QDialog, ModsList.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.PlaysetsList.view().parentWidget().setStyleSheet("background: #05B8CC;")
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.collection = get_collection()
        self.init_handlers()
        self.settingPaths = set_settings()
        self.playsets = self.playset_check()
        self.modList, self.dlc_load, self.game_data, self.playset = prep_data(self.settingPaths[0],
                                                                              list(self.playsets.items())[0])
        self.checkboxes = []
        self.string = self.StringsList.text().split('.')
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
        self.check_enabling_status()
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.switch[self.ReverseSortingButton.isChecked()]['reversing']()
        self.grid = self.gridLayout
        self.buttons = {}
        self.generator = copy.copy(self.modList)
        self.paint_elements()
        self.message = ''

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

    def update_mod_list(self):
        self.modList, self.dlc_load, \
        self.game_data, self.playset = prep_data(self.settingPaths[0], (self.PlaysetsList.currentData(),
                                                 self.playsets[self.PlaysetsList.currentData()]))
        self.checkboxes = []
        self.check_enabling_status()
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.generator = copy.copy(self.modList)
        self.clear_grid_layout()
        self.paint_elements()

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

    def make_sort(self):
        for mod in self.modList:
            mod.isEnabled = mod.checkboxes[0][0].isChecked()
            mod.sortRequired = mod.checkboxes[0][1].isChecked()
        try:
            status = sorting(self.modList, self.game_data, self.dlc_load, self.playset,
                             self.ReverseSortingButton.isChecked())
            if status in 'mods_successfully_sorted':
                message = status
                self.message = ''
                call_success_message(self, message)
            else:
                message = status
                self.message = ''
                call_error_message(self, message)
        except FileNotFoundError as error:
            message = 'FileNotFoundError'
            self.message = error.args[0]
            call_error_message(self, message)
        self.update_mod_list()

    def clear_grid_layout(self):
        for elem in reversed(range(self.gridLayout.count())):
            self.grid.itemAt(elem).widget().setParent(None)

    def open_mod(self, name):
        mod_loc = get_mods_from_playset('get_mod_path', name)[0][0]
        f_path = QtWidgets.QFileDialog.getOpenFileName(directory=mod_loc)[0]
        if '.zip' in f_path.split('/')[-1]:
            open_zip_file(f_path)
            f_path = QtWidgets.QFileDialog.getOpenFileName(directory='/'.join(f_path.split('/')[:-1]))[0]
        if f_path:
            try:
                mod_id = get_mod_id(f_path)
                self.parent.ModIDLine.setText(mod_id)
                self.close()
            except IndexError:
                message = 'IndexError'
                self.message = ''
                call_error_message(self, message)

    def search(self, text):
        self.generator = copy.copy(self.modList)
        for elem in self.modList:
            if text.lower() not in elem.name.lower():
                del self.generator[self.generator.index(elem)]

    def sync_lineEdit(self, text):
        self.clear_grid_layout()
        self.search(text)
        self.paint_elements()

    def get_total_value(self, mod_id):
        total_value = 0
        if mod_id in self.collection:
            count = 0
            for file_name, file_data in self.collection[mod_id].files.items():
                total_value += file_data['file_tr_status']
                count += 1

            # for file_name, file_data in self.collection[mod_id].files.items():
            #     total_value += file_data['name_list_tr_status']
            #     count += 1

            total_value /= count
        return total_value

    def paint_elements(self):
        for index, elem in enumerate(self.generator):
            self.grid.setSpacing(10)
            self.buttons[f'{elem.name}'] = QtWidgets.QPushButton(mod_name_wrap(elem.name))
            set_name_style(self.buttons[f'{elem.name}'])
            self.buttons[f'{elem.name}'].clicked.connect(partial(self.open_mod, elem.name))
            checkbox1 = QtWidgets.QCheckBox()
            checkbox2 = QtWidgets.QCheckBox()
            try:
                checkbox1.setChecked(elem.checkboxes[0][0].isChecked())
                checkbox2.setChecked(elem.checkboxes[0][1].isChecked())
            except AttributeError:
                checkbox1.setChecked(elem.isEnabled)
                checkbox2.setChecked(elem.sortRequired)
            mod_avtivation_status_style(checkbox1)
            mod_sorting_status_style(checkbox2)
            label = QtWidgets.QLabel(self)
            value = self.get_total_value(elem.modId.split('_')[-1].split('.')[0])
            if value == 0:
                label.setStyleSheet(self.borders['gray'])
            elif value == 100:
                label.setStyleSheet(self.borders['green'])
            elif value < 100:
                label.setStyleSheet(self.borders['blue'])

            pixmap = QtGui.QPixmap(get_thumbnail(elem.hashKey))
            pixmap = pixmap.scaled(160, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            label.setPixmap(pixmap)
            self.grid.addWidget(label, index+1, 1)
            self.grid.addWidget(self.buttons[f'{elem.name}'], index+1, 2, 1, 5)
            self.grid.addWidget(checkbox1, index+1, 6)
            self.grid.addWidget(checkbox2, index+1, 7)
            elem.checkboxes[0][0] = checkbox1
            elem.checkboxes[0][1] = checkbox2

    def eventFilter(self, source, event):
        if source == self.WindowMoveButton:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.oldPos = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.oldPos is not None:
                self.move(self.pos() - self.oldPos+event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.oldPos = None
        return super().eventFilter(source, event)
