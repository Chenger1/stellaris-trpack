from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ModsList

from scripts.mods_sorting import set_settings, prep_data, sorting
from scripts.db import get_info_from_db


class ModsListWindow(QtWidgets.QDialog, ModsList.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
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
        self.paint_elements()

    def init_handlers(self):
        self.ReverseSortingButton.setCheckable(True)
        self.ActivationSwticherButton.setCheckable(True)
        self.ExitButton.clicked.connect(self.close)
        self.SortButton.clicked.connect(self.make_sort)
        self.ActivationSwticherButton.clicked.connect(self.activation_switcher)
        self.ReverseSortingButton.clicked.connect(self.reversing)
        self.WindowMoveButton.installEventFilter(self)
        self.PlaysetsList.activated[str].connect(self.update_mod_list)

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

    def update_mod_list(self, text):
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
                            'isActive': elem[2]
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
        self.close()

    def clear_grid_layout(self):
        for elem in reversed(range(self.gridLayout.count())):
            self.grid.itemAt(elem).widget().setParent(None)

    def paint_elements(self):
        help_label_1 = QtWidgets.QLabel('Название мода')
        help_label_2 = QtWidgets.QLabel('Вкл/Выкл')
        help_label_3 = QtWidgets.QLabel('Будет ли сортироваться')
        help_label_1.setStyleSheet('color:white')
        help_label_2.setStyleSheet('color:white')
        help_label_3.setStyleSheet('color:white')
        help_label_3.setWordWrap(True)
        self.grid.addWidget(help_label_1, 0, 0, 1, 5)
        self.grid.addWidget(help_label_2, 0, 6)
        self.grid.addWidget(help_label_3, 0, 7)
        for index, elem in enumerate(self.modList):
            self.grid.setSpacing(10)
            label = QtWidgets.QLabel(str(elem.name))
            checkbox1 = QtWidgets.QCheckBox()
            checkbox1.setChecked(elem.isEnabled)
            checkbox2 = QtWidgets.QCheckBox()
            checkbox2.setChecked(elem.sortRequired)
            label.setStyleSheet('color:white')
            label.setWordWrap(True)
            checkbox1.setStyleSheet("""
                                    QCheckBox{
                                                color:white;
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
                                             }
                                    QCheckBox:indicator:unchecked{
                                            image: url(:/icons/icons/pass_sorting.png)
                                    }
                                    QCheckBox:indicator:checked{
                                            image: url(:/icons/icons/sorting.png)
                                    }
                                    """)
            self.grid.addWidget(label, index+1, 0, 1, 5)
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
