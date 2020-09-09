from PyQt5 import QtWidgets, QtCore, QtGui

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
        self.OptionsListComboBox.view().parentWidget().setStyleSheet("background: #05B8CC;")
        self.setModal(True)
        self.parent = parent
        self.oldPos = self.pos()
        self.collection = get_collection()
        self.buttons = {}
        self.accept_window = AcceptWindow
        self.init_handlers()
        self.paint_elements()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.OptionsListComboBox.activated[str].connect(lambda: self.paint_elements())
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.reference_window('QLabel_2_Collection'))
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

    @staticmethod
    def set_button_style(button):
        button.setFont(QtGui.QFont("Arkhip", 9))
        button.setStyleSheet("""
            QPushButton{
            background-color: transparent;
            min-height: 40px;
            max-width: 400px;
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

    @staticmethod
    def set_data_style(data_field):
        data_field.setFont(QtGui.QFont("Arkhip", 9))
        data_field.setStyleSheet("""
                            QLineEdit{
                        background-color: transparent;
                        border: transparent;
                        max-width: 245px;
                        color: #ffffff;
                        text-align: left;            
                        }
                            QLineEdit:hover{
                        color: #05B8CC;
                        }
                        """)

    @staticmethod
    def set_incomplete_style(status):
        status.setFormat("%p%   ")
        status.setInvertedAppearance(True)
        status.setFont(QtGui.QFont("Arkhip", 9))
        status.setStyleSheet("""
                        QProgressBar{
                        background-color:  #1f2533;
                        border: solid grey;
                        border-radius: 10px;
                        color: white;
                        font-family: "KB Astrolyte";
                        text-align: right;
                        max-height: 20px;
                        max-width: 125;
                        margin-right: 10px;
                        }
                        QProgressBar::chunk {
                        background-color: #05B8CC;
                        border-radius :10px;
                        }      """)

    @staticmethod
    def set_complete_style(status):
        status.setFormat("%p%   ")
        status.setInvertedAppearance(True)
        status.setFont(QtGui.QFont("Arkhip", 9))
        status.setStyleSheet("""
                        QProgressBar{
                        background-color: #1f2533;
                        border: solid grey;
                        border-radius: 10px;
                        color: white;
                        font-family: "KB Astrolyte";
                        text-align: right;
                        max-height: 20px;
                        max-width: 125;
                        margin-right: 10px;
                        }
                        QProgressBar::chunk {
                        background-color: #5abe41;
                        border-radius :10px;
                        }      """)

    def clean(self, grid):
        for i in reversed(range(grid.count())):
            grid.itemAt(i).widget().setParent(None)

    def paint_elements(self):
        grid = self.gridLayout
        self.clean(grid)
        for index, elem in enumerate(self.collection):
            grid.setSpacing(10)
            self.buttons[f'{elem}'] = QtWidgets.QPushButton(f'{index + 1}: {self.collection[elem]["name"]}')
            #
            self.set_button_style(self.buttons[f'{elem}'])
            #
            self.buttons[f'{elem}'].clicked.connect(partial(self.open_accept_window, elem))
            grid.addWidget(self.buttons[f'{elem}'], index + 1, 3, 1, 4)

            if self.OptionsListComboBox.currentText() == (self.OptionsListComboBox.itemText(0)):
                file_name = QtWidgets.QLineEdit(self.collection[elem]['file_name'])
                #
                self.set_data_style(file_name)
                #
                grid.addWidget(file_name, index + 1, 6)

                status = QtWidgets.QProgressBar()
                status.setValue(self.collection[elem]['tr_status'])
                if status.value() != 100:
                    #
                    self.set_incomplete_style(status)
                    #
                else:
                    #
                    self.set_complete_style(status)
                    #
                grid.addWidget(status, index + 1, 7)

            elif self.OptionsListComboBox.currentText() == (self.OptionsListComboBox.itemText(1)):
                # name_list = QtWidgets.QLineEdit(self.collection[elem]['file_name'])
                name_list = QtWidgets.QLineEdit('-' * 20)
                self.OptionDataLabel.setText('Файлы')
                self.set_data_style(name_list)
                grid.addWidget(name_list, index + 1, 6)

                status = QtWidgets.QProgressBar()
                # status.setValue(self.collection[elem]['tr_status'])
                status.setValue(0)
                if status.value() != 100:
                    self.set_incomplete_style(status)
                else:
                    self.set_complete_style(status)
                grid.addWidget(status, index + 1, 7)

            elif self.OptionsListComboBox.currentText() == (self.OptionsListComboBox.itemText(2)):
                steam_id = QtWidgets.QLineEdit(f'{" " * 12}{elem}')
                self.OptionDataLabel.setText('  ID')
                self.set_data_style(steam_id)
                grid.addWidget(steam_id, index + 1, 6)

                status = QtWidgets.QProgressBar()
                # status.setValue(self.collection[elem]['tr_status'])
                status.setValue(0)
                if status.value() != 100:
                    self.set_incomplete_style(status)
                else:
                    self.set_complete_style(status)
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
