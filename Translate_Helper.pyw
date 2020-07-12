#!/usr/bin/python3
import sys
import subprocess
import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, QHBoxLayout


class Ui_Form(QWidget):

	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.rowcount = 6
		self.path = os.getcwd()
		self.setWindowTitle("Translate helper")
		self.setWindowIcon(QtGui.QIcon(self.path + '\\logo.png'))
		self.resize(720, 600)
		#------------------------------------------------
		self.verticalLayout = QVBoxLayout(self)
		for i in range(0, self.rowcount):
			row = 'row_' + str(i)
			setattr(self, row, QHBoxLayout(self))
			exec('self.' + row + '.addSpacing(15)')
		#------------------------------------------------
		self.cut = QPushButton("Вырезать строки", self)
		self.cut.clicked.connect(lambda: self.launch(self.path + '\\scripts\\loc_cutter.pyw'))
		self.cut.setFixedSize(150, 45)
		self.row_0.addWidget(self.cut)
		#------------------------------------------------
		self.put = QPushButton("Вставить строки", self)
		self.put.clicked.connect(lambda: self.launch(self.path + '\\scripts\\loc_putter.pyw'))
		self.put.setFixedSize(150, 45)
		self.row_1.addWidget(self.put)
		#------------------------------------------------
		self.tr = QPushButton("Быстрый перевод", self)
		self.tr.clicked.connect(lambda: self.launch(self.path + '\\scripts\\loc_translator.pyw'))
		self.tr.setFixedSize(150, 45)
		self.row_2.addWidget(self.tr)
		#------------------------------------------------
		self.cmb = QPushButton("Рекомбинация", self)
		self.cmb.clicked.connect(lambda: self.launch(self.path + '\\scripts\\loc_combiner.pyw'))
		self.cmb.setFixedSize(150, 45)
		self.row_3.addWidget(self.cmb)
		#------------------------------------------------
		self.cmpr = QPushButton("Сравнение версий", self)
		self.cmpr.clicked.connect(lambda: self.launch(self.path + '\\scripts\\loc_comparer.pyw'))
		self.cmpr.setFixedSize(150, 45)
		self.row_4.addWidget(self.cmpr)
		#------------------------------------------------
		for i in range(0, self.rowcount - 1):
			row = 'row_' + str(i)
			exec('self.' + row + '.addSpacing(30)')
		#------------------------------------------------
		self.label_1 = QLabel("<html><head/><body><p>Вырезает строки с переводом из файла локализации и переносит </p><p>их в файл rus_названиемода_l_english.yml</p></body></html>", self)
		self.row_0.addWidget(self.label_1)
		#------------------------------------------------
		self.label_2 = QLabel("<html><head/><body><p>Берёт файл из первого пункта и вставляет переведённые строки обратно.</p><p>(Выбирать изначальный файл)</p><p>(Создаёт новый файл на основе изначального с приставкой final_)</p></body></html>", self)
		self.row_1.addWidget(self.label_2)
		#------------------------------------------------
		self.label_3 = QLabel("<html><head/><body><p>На основе файла с вырезанными строками создаёт файл </p><p>с машинным переводом от GT для ориентировки при переводе.</p><p>(Выбирать файл с приставкой rus_)</p></body></html>", self)
		self.row_2.addWidget(self.label_3)
		#------------------------------------------------
		self.label_4 = QLabel("<html><head/><body><p>Берётся файл оригинала и файл устаревшего перевода,</p><p>они анализируются и все возможные строки из старого файла переносятся в новый.</p><p>(Выбирать оригинальный файл)</p></body></html>", self)
		self.row_3.addWidget(self.label_4)
		#------------------------------------------------
		self.label_5 = QLabel("<html><head/><body><p>Сравнение файлов разных версий модификаций</p></body></html>", self)
		self.row_4.addWidget(self.label_5)
		#------------------------------------------------
		self.exit = QPushButton("Выход", self)
		self.exit.clicked.connect(sys.exit)
		self.exit.setFixedSize(150, 45)
		self.row_5.addWidget(self.exit)
		for i in range(0, self.rowcount):
			row = 'row_' + str(i)
			exec('self.verticalLayout.addLayout(self.' + row + ')')
			exec('self.' + row + '.insertStretch(4, 140)')
		self.row_5.addStretch(1)
		self.show()

	def launch(self, script):
		DETACHED_PROCESS = 0x00000008
		subprocess.Popen([sys.executable, script], shell=False, stdin=None, stdout=None, stderr=None, close_fds=True, creationflags=DETACHED_PROCESS)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Ui_Form()
	sys.exit(app.exec_())
