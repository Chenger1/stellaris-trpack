from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Accept


class AcceptWindow(QtWidgets.QDialog, Accept.Ui_Dialog):
    def __init__(self, parent, label_text, accept_func, denied_func=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.parent = parent
        self.InfoLabel.setText(label_text)
        self.InfoLabel.setWordWrap(True)
        self.oldPos = self.pos()
        self.init_handlers(accept_func, denied_func)

    def init_handlers(self, accept_func, denied_func):
        self.ExitButton.clicked.connect(self.close)
        self.AcceptButton.clicked.connect(accept_func)
        self.DeniedButton.clicked.connect(denied_func or self.close)
        self.ReferenceButton.clicked.connect(lambda: self.parent.parent.parent.reference_window('QLabel_2_1_Functional'))
        self.WindowMoveButton.installEventFilter(self)

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