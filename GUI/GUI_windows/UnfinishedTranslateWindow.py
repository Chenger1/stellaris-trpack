from PyQt5 import QtWidgets, QtCore

from GUI.GUI_windows_source import UnfinishedTranslate

from scripts.utils import collection_append, save_unfinished_machine_text, call_success_message


class UnfinishedTranslateWindow(QtWidgets.QDialog, UnfinishedTranslate.Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setModal(True)
        self.init_handlers()
        self.oldPos = self.pos()
        self.parent = parent
        self.messege = ''

    def init_handlers(self):
        self.ExitButton.clicked.connect(self.close)
        self.DeniedButton.clicked.connect(self.close)
        self.AcceptButton.clicked.connect(self.save_translation_state)
        self.ReferenceButton.clicked.connect(lambda: self.parent.reference_window('QLabel_2_1_Functional'))
        self.WindowMoveButton.installEventFilter(self)

    def save_translation_state(self):
        pointer_position = self.parent.pointer
        translation_status = round((len(self.parent.user_text*100))/len(self.parent.orig_text))
        save_unfinished_machine_text(self.parent.machine_text)
        collection_append(self.parent.ModIDLine.text(), translation_status, pointer_position
                          )
        self.parent.clean_state()
        message = 'file_was_written'
        self.message = ''
        call_success_message(self, message)

        self.close()

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