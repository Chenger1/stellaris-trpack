"""
                            ↓ Instance initialization ↓
"""

from GUI.GUI_windows.SuccessMessageWindow import SuccessMessageWindow
from GUI.GUI_windows.ErrorMessageWindow import ErrorMessageWindow
from GUI.GUI_windows.AcceptMessageWindow import AcceptMessageWindow


def call_accept_window(parent, message, accept_func, denied_func=None):
    accept_window = AcceptMessageWindow(parent, message, accept_func, denied_func)
    accept_window.show()


def call_success_message(self, message):
    window = SuccessMessageWindow(self, message)
    window.show()


def call_error_message(self, message):
    window = ErrorMessageWindow(self, message)
    window.show()


