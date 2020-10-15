from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import UpdateTranslation

from scripts.stylesheets import set_choosen_file_style, set_not_choosen_file_style


class UpdateTranslationWindow(QtWidgets.QDialog, UpdateTranslation.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.parent = parent
        self.init_handlers()

    def init_handlers(self):
        self.WindowMoveButton.installEventFilter(self)
        self.ExitButton.clicked.connect(self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_5_TranslationLanguage'))
        # self.ChooseOldFilelButton.clicked.connect(lambda: )
        # self.ChooseNewFilelButton.clicked.connect(lambda: )
        # self.AcceptButton.clicked.connect(lambda: )

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
