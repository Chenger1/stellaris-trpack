#!/usr/bin/python3
from subprocess import call
from sys import executable


def install(package):
    call([executable, "-m", "pip", "install", package])


if __name__ == '__main__':
    install('setuptools')
    install('langdetect')
    install('googletrans')
    install('pyqt5')
    install('pyqt5-tools')
    install('pypiwin32')
    install('requests')
    install('pillow')
