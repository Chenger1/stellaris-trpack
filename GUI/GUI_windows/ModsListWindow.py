from PyQt5 import QtWidgets, QtCore, QtGui

from GUI.GUI_windows_source import ModsList

from scripts.mods_sorting import set_settings, prep_data, sorting
from scripts.db import get_info_from_db, get_mods_from_playset, write_data_into_db
from scripts.utils import get_mod_id, paradox_folder, open_zip_file

from functools import partial
import os
import requests
import copy


class ModsListWindow(QtWidgets.QDialog, ModsList.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.PlaysetsList.view().parentWidget().setStyleSheet("background: #05B8CC;")
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers()
        self.settingPaths = set_settings()
        self.playsets = self.playset_check()
        self.modList, self.dlc_load, self.game_data, self.playset = prep_data(self.settingPaths[0],
                                                                              list(self.playsets.items())[0])
        self.checkboxes = []
        self.switch = {
            True: {
                'act_switcher': lambda: self.ActivationSwticherButton.setText('Выкл все моды'),
                'reversing': lambda: self.ReverseSortingButton.setText('Z-A')
            },
            False: {
                'act_switcher': lambda: self.ActivationSwticherButton.setText('Вкл все моды'),
                'reversing': lambda: self.ReverseSortingButton.setText('A-Z')
            }
        }
        self.check_enabling_status()
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.switch[self.ReverseSortingButton.isChecked()]['reversing']()
        self.grid = self.gridLayout
        self.buttons = {}
        self.generator = copy.copy(self.modList)
        self.images = {
                    elem[0]: {
                            'steam_path': elem[1],
                            'cache_path': elem[2],
                            'steam_id': elem[3],
                             } for elem in get_info_from_db('get_images')
                   }
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
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_5_AdvancedSorter'))
        self.ResetButton.clicked.connect(self.reset_sorting_requiring)

    def reversing(self):
        self.ReverseSortingButton.setChecked(self.ReverseSortingButton.isChecked())
        self.switch[self.ReverseSortingButton.isChecked()]['reversing']()

    def check_enabling_status(self):
        disabled_mods = list(filter(lambda x: x.isEnabled is False, self.modList))
        self.ActivationSwticherButton.setChecked(not len(disabled_mods) >= 1)

    def activation_switcher(self):
        for checkbox, mod in zip(self.checkboxes, self.modList):
            mod.isEnabled = self.ActivationSwticherButton.isChecked()
            checkbox[0].setChecked(self.ActivationSwticherButton.isChecked())
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
        self.ActivationSwticherButton.setChecked(self.ActivationSwticherButton.isChecked())

    def reset_sorting_requiring(self):
        for checkbox, mod in zip(self.checkboxes, self.modList):
            mod.sortRequired = True
            checkbox[1].setChecked(True)

    def update_mod_list(self):
        self.modList, self.dlc_load, \
        self.game_data, self.playset = prep_data(self.settingPaths[0], (self.PlaysetsList.currentData(),
                                                 self.playsets[self.PlaysetsList.currentData()]))
        self.checkboxes = []
        self.check_enabling_status()
        self.switch[self.ActivationSwticherButton.isChecked()]['act_switcher']()
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
        for checkbox, mod in zip(self.checkboxes, self.modList):
            mod.isEnabled = checkbox[0].isChecked()
            mod.sortRequired = checkbox[1].isChecked()
        try:
            status = sorting(self.modList, self.game_data, self.dlc_load, self.playset,
                             self.ReverseSortingButton.isChecked())
            self.parent.show_system_message(status[0], status[1])
        except FileNotFoundError as error:
            self.parent.show_system_message('error', error.args[0])
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
                self.parent.show_system_message('error', 'Вы выбрали не тот файл')

    @staticmethod
    def download_image(url, file_name, steam_id):
        response = requests.get(url)
        if '.' in file_name:
            path = f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{steam_id}\\{file_name}'
        else:
            path = f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{steam_id}\\{file_name}' #TODO
            write_data_into_db('write_new_image_path', {'image_path': path,
                                                        'steam_id': steam_id})
        with open(path, 'wb') as file:
            file.write(response.content)

        return path

    def get_images(self, mod_id):
        image_pth = self.images[mod_id]
        if not image_pth['cache_path'] and not image_pth['steam_path']:
            return None
        if not image_pth['cache_path'] and image_pth['steam_path']:
            os.mkdir(f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{image_pth["steam_id"]}')
            image_pth['cache_path'] = self.download_image(image_pth['steam_path'],
                                                          image_pth['steam_path'].split('/')[-2].lower(),
                                                          image_pth['steam_id'])
            return image_pth['cache_path']
        try:
            dir = os.listdir(f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{image_pth["steam_id"]}')
            if dir:
                return image_pth['cache_path']
            image_pth['cache_path'] = self.download_image(image_pth['steam_path'],
                                                          image_pth['cache_path'].split('\\')[-1],
                                                          image_pth['steam_id'])
            return image_pth['cache_path']
        except FileNotFoundError:
            os.mkdir(f'{paradox_folder}\\.launcher-cache\\steam-mod-thumbnail-{image_pth["steam_id"]}')
            image_pth['cache_path'] = self.download_image(image_pth['steam_path'],
                                                          image_pth['cache_path'].split('\\')[-1],
                                                          image_pth['steam_id'])
            return image_pth['cache_path']

    def search(self, text):
        self.generator = copy.copy(self.modList)
        # self.checkboxes = []
        # self.buttons = {}
        for elem in self.modList:
            if text.lower() in elem.name.lower():
                pass
            else:
                del self.generator[self.generator.index(elem)]
        print(len(self.generator))

    def sync_lineEdit(self, text):
        self.clear_grid_layout()
        self.search(text)
        self.paint_elements()

    def paint_elements(self):
        for index, elem in enumerate(self.generator):
            self.grid.setSpacing(10)
            self.buttons[f'{elem.name}'] = QtWidgets.QPushButton(f'{elem.name}')
            self.buttons[f'{elem.name}'].setStyleSheet("""
                                                    QPushButton{
                                                                background-color: transparent;
                                                                min-height: 40px;
                                                                max-width: 600px;
                                                                color: #ffffff;
                                                                text-align: left;            
                                                    }
                                                    QPushButton::hover {
                                                                color: #05B8CC;
                                                    }
                                                    QPushButton::pressed {
                                                                color: rgba(194, 194, 194, 50);
                                                    }
                            """)
            self.buttons[f'{elem.name}'].setFont(QtGui.QFont("Arkhip", 9))
            self.buttons[f'{elem.name}'].clicked.connect(partial(self.open_mod, elem.name))
            checkbox1 = QtWidgets.QCheckBox()
            checkbox1.setChecked(elem.isEnabled)
            checkbox2 = QtWidgets.QCheckBox()
            checkbox2.setChecked(elem.sortRequired)
            checkbox1.setStyleSheet("""
                                    QCheckBox{
                                                color:white;
                                                margin-left: 30px;
                                             }
                                    QCheckBox:indicator:unchecked{
                                            image: url(:/icons/icons/pass.png)
                                    }
                                    QCheckBox:indicator:checked{
                                            image: url(:/icons/icons/active.png)
                                    }
                                    """)
            checkbox2.setStyleSheet("""
                                    QCheckBox{
                                                color:white;
                                                margin-right: 10px;
                                             }
                                    QCheckBox:indicator:unchecked{
                                            image: url(:/icons/icons/pass_sorting.png)
                                    }
                                    QCheckBox:indicator:checked{
                                            image: url(:/icons/icons/sorting.png)
                                    }
                                    """)
            label = QtWidgets.QLabel(self)
            # pixmap = QtGui.QPixmap(self.get_images(elem.hashKey))
            # pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
            # label.setPixmap(pixmap)
            self.grid.addWidget(label, index+1, 1)
            self.grid.addWidget(self.buttons[f'{elem.name}'], index+1, 2, 1, 5)
            self.grid.addWidget(checkbox1, index+1, 6)
            self.grid.addWidget(checkbox2, index+1, 7)
            self.checkboxes.append((checkbox1, checkbox2))

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
