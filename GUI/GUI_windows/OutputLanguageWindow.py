from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import OutputLanguage

from GUI.GUI_windows.MoreOutputLanguageWindow import MoreOutputLanguageWindow


class OutputLanguageWindow (QtWidgets.QDialog, OutputLanguage.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.init_handlers()
        self.oldPos = self.pos()
        self.WindowMoveButton.installEventFilter(self)
        self.parent = parent

    def init_handlers(self):
        self.MoreLanguagesButton.clicked.connect(self.show_more_output_language_window)
        self.ExitButton.clicked.connect(self.close)

    def show_more_output_language_window(self):
        more_output_language_window = MoreOutputLanguageWindow(self)
        more_output_language_window.show()

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
