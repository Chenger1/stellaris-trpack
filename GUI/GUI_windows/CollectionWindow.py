from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Collection
from GUI.GUI_windows.AcceptWindow import AcceptWindow

from scripts.utils import get_collection, set_data

from functools import partial
import os


class CollectionWindow(QtWidgets.QDialog, Collection.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.init_handlers()
        self.collection = get_collection()
        self.buttons = {}
        self.accept_window = AcceptWindow
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
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

    def paint_elements(self):
        grid = self.gridLayout
        for index, elem in enumerate(self.collection):
            grid.setSpacing(10)
            self.buttons[f'{elem}'] = QtWidgets.QPushButton(f'{index + 1}: {self.collection[elem]["name"]}')
            steam_id = QtWidgets.QLabel(elem)
            file_name = QtWidgets.QLineEdit(self.collection[elem]['file_name'])
            status = QtWidgets.QProgressBar()
            self.buttons[f'{elem}'].setStyleSheet("""
            QPushButton{
            background-color: transparent;
            min-height: 40px;
            max-width: 200px;
            color: #ffffff;
            }
            """)
            self.buttons[f'{elem}'].clicked.connect(partial(self.open_accept_window, elem))
            steam_id.setStyleSheet('color:white')
            file_name.setStyleSheet("""
            QLineEdit{           
            background-color: transparent;
            border: transparent;
            max-width: 130px;
            color: #ffffff;
            }
            QLineEdit:hover{
            background-color: transparent;
            }
            """)
            status.setFormat("%p% ")
            status.setValue(self.collection[elem]['tr_status'])
            if status.value() != 100:
                status.setInvertedAppearance(True)
                status.setStyleSheet("""
                QProgressBar{
                background-color:  #1f2533;
                border: solid grey;
                border-radius: 10px;
                color: white;
                font-family: "KB Astrolyte";
                text-align: right;
                max-height: 20px;
                max-width: 110px;
                }
                QProgressBar::chunk {
                background-color: #05B8CC;
                border-radius :10px;
                }      """)
            else:
                status.setStyleSheet("""
                QProgressBar{
                background-color: #1f2533;
                border: solid grey;
                border-radius: 10px;
                color: white;
                font-family: "KB Astrolyte";
                text-align: right;
                max-height: 20px;
                max-width: 110px;
                }
                QProgressBar::chunk {
                background-color: #5abe41;
                border-radius :10px;
                }      """)
            grid.addWidget(self.buttons[f'{elem}'], index + 1, 3, 1, 4)
            grid.addWidget(steam_id, index + 1, 5)
            grid.addWidget(file_name, index + 1, 6)
            grid.addWidget(status, index + 1, 7)

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
