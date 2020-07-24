#!/usr/bin/python3
import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

if __name__ == '__main__':
    install('setuptools')
    install('langdetect')
    install('googletrans')
    install('pyqt5')
    install('pyqt5-tools')
    install('pypiwin32')