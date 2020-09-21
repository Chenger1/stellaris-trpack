from PyQt5 import QtWidgets, QtGui


def set_name_style(button):
    button.setFont(QtGui.QFont("Arkhip", 9))
    button.setStyleSheet("""
    QPushButton{
        background-color: transparent;
        min-height: 40px;
        max-width: 500px;
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


def set_button_style(button):
    button.setFont(QtGui.QFont("Arkhip", 9))
    button.setStyleSheet("""
    QPushButton{
        background-color: transparent;
        min-height: 40px;
        max-width: 400px;
        text-align: right;
        margin-right: 20px;
        color: #ffffff;
    }
    QPushButton::hover {
        color: #05B8CC;
    }
    QPushButton::pressed {
        color: rgba(194, 194, 194, 50);
    }
""")


def set_incomplete_style(status):
    status.setFormat("%p%   ")
    status.setInvertedAppearance(True)
    status.setFont(QtGui.QFont("KB Astrolyte", 9))
    status.setStyleSheet("""
    QProgressBar{
        background-color:  #1f2533;
        border: solid grey;
        border-radius: 10px;
        color: white;
        text-align: right;
        max-height: 20px;
        max-width: 125;
        margin-right: 10px;
    }
    QProgressBar::chunk {
        background-color: #05B8CC;
        border-radius :10px;
    }
""")


def set_complete_style(status):
    status.setFormat("%p%   ")
    status.setInvertedAppearance(True)
    status.setFont(QtGui.QFont("KB Astrolyte", 9))
    status.setStyleSheet("""
    QProgressBar{
        background-color: #1f2533;
        border: solid grey;
        border-radius: 10px;
        color: white;
        text-align: right;
        max-height: 20px;
        max-width: 125;
        margin-right: 10px;
    }
    QProgressBar::chunk {
        background-color: #5abe41;
        border-radius :10px;
    }
""")


def create_separator():
    separator = QtWidgets.QTextEdit()
    separator.setStyleSheet("""
    QTextEdit {
        max-height: 0px;
        max-width: 100px;
        margin-right: 75px;
        border: 1px solid #05B8CC;
    }
""")
    return separator
