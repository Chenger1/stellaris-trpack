from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import SteamID

from scripts.utils import open_zip_file


class SteamIDWindow(QtWidgets.QDialog, SteamID.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.init_handlers()
        self.parent = parent
        self.oldPos = self.pos()
        self.WindowMoveButton.installEventFilter(self)

    def init_handlers(self):
        self.AcceptButton.clicked.connect(self.get_steam_id)
        self.ExitButton.clicked.connect(self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.reference_window('QLabel_1_2_SteamID'))

    def accept_file(self):
        self.parent.close()
        self.close()

    def get_steam_id(self):
        try:
            path = self.IDLine.text().strip()
            if path.isnumeric():
                mod_data = self.parent.parent.get_steam_id(path.split('=')[-1])
                f_path = QtWidgets.QFileDialog.getOpenFileName(directory=f"{mod_data['path']}\\localisation")[0]
                if '.zip' in f_path.split('/')[-1]:
                    open_zip_file(f_path)
                    f_path = QtWidgets.QFileDialog.getOpenFileName(directory='/'.join(f_path.split('/')[:-1]))[0]
                self.AcceptButton.setText('Подтвердить файл')
                self.AcceptButton.repaint()
                self.AcceptButton.disconnect()
                self.AcceptButton.clicked.connect(self.accept_file)
                self.parent.choose_file(f_path)
            elif path == '':
                self.parent.parent.show_system_message('error', 'Вы не ввели ID мода')
            else:
                self.parent.parent.show_system_message('error', 'Строка ID содержит сторонние символы')
        except OSError:
            self.parent.parent.show_system_message('error', 'Мод не найден')

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
