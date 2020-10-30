from PyQt5 import QtWidgets, QtGui


def mod_name_style(button):
    button.setFont(QtGui.QFont("Arkhip", 9))
    button.setStyleSheet("""
    QPushButton{
        background-color: transparent;
        min-height: 40px;
        max-width: 320px;
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


def file_name_style(button):
    button.setFont(QtGui.QFont("Arkhip", 9))
    button.setStyleSheet("""
    QPushButton{
        background-color: transparent;
        min-height: 40px;
        max-width: 170px;
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


def not_chosen_lang_style(button):
    button.setFont(QtGui.QFont("KB Astrolyte", 9))
    button.setStyleSheet("""
    QPushButton{
        background-color: rgba(31, 37, 51, 50);
        border: 2px solid #ffffff;
        border-radius: 13px;
        min-height: 22px;
        max-width: 175px;
        color: #ffffff;
    }
    QPushButton:hover{
        background-color: rgba(56, 57, 61, 50);
    }
    QPushButton:pressed{
        background-color: rgba(194, 194, 194, 50);
        border: #c2c2c2;
    }
""")


def choosen_lang_style(button):
    button.setFont(QtGui.QFont("KB Astrolyte", 10))
    button.setStyleSheet("""
    QPushButton{
        background-color: #05B8CC;
        border: 2px solid #05B8CC;
        border-radius: 13px;
        min-height: 22px;
        max-width: 175px;
        color: #1f2533;
    }
    QPushButton:hover{
        background-color: #31858f;
        border: #31858f;
        color: #ffffff;
    }
    QPushButton:pressed{
        background-color: rgba(194, 194, 194, 50);
        border: #c2c2c2;
    }
    """)


def incomplete_translation_style(status):
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


def complete_translation_style(status):
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


def file_choosen_style(status):
    status.setText('|')
    status.setStyleSheet("""
    QLabel{
        background-color: #4ea838;
        border: #c2c2c2;
        border-radius: 20px;
        min-height: 27px;
        color: #ffffff;
    }
    QLabel:hover{
        background-color: #438e30;
        border: #31858f;
        color: #ffffff;
    }
""")


def file_not_choosen_style(status):
    status.setText('—')
    status.setStyleSheet("""
        QLabel{
            background-color: #c93c3c;
            border: #c2c2c2;
            border-radius: 20px;
            min-height: 27px;
            color: #ffffff;
        }
        QLabel:hover{
            background-color: #b33434;
            border: #31858f;
            color: #ffffff;
        }
    """)


def create_row_separator():
    separator = QtWidgets.QLabel()
    separator.setStyleSheet("""
    QLabel {
        max-height: 0px;
        min-width: 100px;
        margin-right: 75px;
        border: 1px solid #05B8CC;
    }
""")
    return separator


def mod_avtivation_status_style(checkbox):
    checkbox.setStyleSheet("""
    QCheckBox{
        color:white;
        margin-left: 30px;
    }
    QCheckBox:indicator:unchecked{
        image: url(:/icons/icons/pass.png)
    }
    QCheckBox:indicator:checked{
        image: url(:/icons/icons/active.png)
    }
""")


def mod_sorting_status_style(checkbox):
    checkbox.setStyleSheet("""
    QCheckBox{
        color:white;
        margin-right: 10px;
    }
    QCheckBox:indicator:unchecked{
        image: url(:/icons/icons/pass_sorting.png)
    }
    QCheckBox:indicator:checked{
        image: url(:/icons/icons/sorting.png)
    }
""")
