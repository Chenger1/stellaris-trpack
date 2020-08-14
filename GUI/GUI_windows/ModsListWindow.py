from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import ModsList

from scripts.mods_sorting import set_settings, prep_data, sorting


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
        self.modList, self.dlc_load, self.game_data = prep_data(self.settingPaths[0])
        self.checkboxes = []
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)
        self.LocalizeButton.clicked.connect(self.make_sort)

    def make_sort(self):
        for checkbox, mod in zip(self.checkboxes, self.modList):
            mod.isEnabled = checkbox[0].isChecked()
            mod.sortRequired = checkbox[1].isChecked()
        try:
            status = sorting(self.modList, self.game_data, self.dlc_load)
            self.parent.show_system_message(status[0], status[1])
        except FileNotFoundError as error:
            self.parent.show_system_message('error', error.args[0])
        self.close()

    def paint_elements(self):
        grid = self.gridLayout
        help_label_1 = QtWidgets.QLabel('Название мода')
        help_label_2 = QtWidgets.QLabel('Вкл/Выкл')
        help_label_3 = QtWidgets.QLabel('Будет ли сортироваться')
        help_label_1.setStyleSheet('color:white')
        help_label_2.setStyleSheet('color:white')
        help_label_3.setStyleSheet('color:white')
        help_label_3.setWordWrap(True)
        grid.addWidget(help_label_1, 0, 0, 1, 5)
        grid.addWidget(help_label_2, 0, 6)
        grid.addWidget(help_label_3, 0, 7)
        for index, elem in enumerate(self.modList):
            grid.setSpacing(10)
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
            grid.addWidget(label, index+1, 0, 1, 5)
            grid.addWidget(checkbox1, index+1, 6)
            grid.addWidget(checkbox2, index+1, 7)
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
