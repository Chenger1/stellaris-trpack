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
        self.registry, self.modList, self.dlc_load, self.game_data, self.enabled_mods = prep_data(self.settingPaths[0])
        self.checkboxes = []
        self.labels = []
        self.MakeSortButton = QtWidgets.QPushButton('Sort')
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)

    def make_sort(self):
        for checkbox, mod in zip(self.checkboxes, self.modList):
            mod.isEnabled = checkbox[0].isChecked()
            mod.sortRequired = checkbox[1].isChecked()
        status = sorting(self.modList, self.game_data, self.dlc_load, self.enabled_mods)
        self.parent.show_system_message(status[0], status[1])
        self.close()

    def paint_elements(self):
        grid = self.gridLayout
        for elem in range(len(self.modList)):
            label = QtWidgets.QLabel(str(self.modList[elem].name))
            checkbox1 = QtWidgets.QCheckBox('Активный/Неактивный')
            checkbox1.setChecked(self.modList[elem].isEnabled)
            checkbox2 = QtWidgets.QCheckBox('Будет ли сортироваться')
            checkbox2.setChecked(self.modList[elem].sortRequired)
            label.setStyleSheet('color:white;')
            checkbox1.setStyleSheet('color:white;')
            checkbox2.setStyleSheet('color:white;')
            grid.addWidget(label, elem, 0)
            grid.addWidget(checkbox1, elem, 1)
            grid.addWidget(checkbox2, elem, 2)
            self.checkboxes.append((checkbox1, checkbox2))
        self.MakeSortButton.setStyleSheet("""
        QPushButton{
            background-color: #5abe41;;
            border: 3px solid #5abe41;
            border-radius: 20px;
            color: #1f2533;
        }
        QPushButton:hover{
            background-color: #438e30;
            border: #438e30;
            color: #ffffff;
        }
        """)
        grid.addWidget(self.MakeSortButton)
        self.MakeSortButton.clicked.connect(self.make_sort)

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
