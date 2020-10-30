# TODO Return call_accept_message() to here
"""
                            ↓ Инициализация данных ↓
"""

from GUI.GUI_windows.SuccessMessageWindow import SuccessMessageWindow
from GUI.GUI_windows.ErrorMessageWindow import ErrorMessageWindow


def call_success_message(self, message):
    window = SuccessMessageWindow(self, message)
    window.show()


def call_error_message(self, message):
    window = ErrorMessageWindow(self, message)
    window.show()


