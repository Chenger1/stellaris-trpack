from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import Reference
from GUI.GUI_windows.AboutToolWindow import AboutToolWindow


class ReferenceWindow(QtWidgets.QDialog, Reference.Ui_Dialog):
    def __init__(self, parent, to_scroll):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.oldPos = self.pos()
        self.init_handlers()
        self.parent = parent
        self.area_widget = self.scrollArea.children()[0].children()[0]
        self.labels = self.set_labels()
        self.scroll_bar(self.labels[to_scroll]['pos'])
        self.scrollAreaWidgetContents.adjustSize()

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.WindowMoveButton.installEventFilter(self)
        self.AboutToolButton.clicked.connect(self.about_tool_window)
        self.SearchLine.textChanged.connect(self.search)

    def about_tool_window(self):
        about_tool_window = AboutToolWindow(self)
        about_tool_window.show()
        self.close()

    def set_labels(self):
        return {
            label.objectName(): {'pos': label.y(),
                                 'text': label.text()} for label in self.area_widget.findChildren(QtWidgets.QLabel) if 'QLabel' in label.objectName()
        }

    def search(self, string):
        for label in list(self.labels.values()):
            if string.lower() in label['text'].lower() and string != '':
                self.scroll_bar(label['pos'])

    def scroll_bar(self, to_scroll):
        self.scrollArea.verticalScrollBar().setValue(to_scroll)

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
