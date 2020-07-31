#!/usr/bin/python3
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtCore import QSize, Qt
from pandas import read_csv


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.setMinimumSize(QSize(800, 600))
		self.setWindowTitle("Отображение данных")
		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)

		grid_layout = QGridLayout()
		central_widget.setLayout(grid_layout)

		# Считывание данных
		df = read_csv('files.csv', delimiter=';')
		tuples = [[row[col] for col in df.columns] for row in df.to_dict('records')]

		table = QTableWidget(self)			# Создаём таблицу
		table.setColumnCount(3)				# Устанавливаем x колонок
		table.setRowCount(len(tuples))		# Устанавливаем y строк

		# Таблица с данными из csv
		self.multifiles = []
		self.tags = []
		self.unit = {}

		# Сохранение путей всех файлов
		count = 0
		for i in tuples:
			self.tags.append(i[1])
			if i[3].find('-') != -1:
				self.multifiles.append(i[1])  #создание списка мультифайлов модов
				ss = i[3].split('-')
				self.unit[i[1]] = len(ss)
				for j in range(1, len(ss) + 1):
					self.unit[i[1] + str(j)] = ss[j - 1]
			else:
				self.unit[i[1]] = i[3]
			count += 1
		self.unit['exit'] = None

		table.setHorizontalHeaderLabels(["Name", "ID", "Tag"])
		for i in range(0, 2):
			table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
		for j in range(0, len(tuples)):
			table.setItem(j, 0, QTableWidgetItem(tuples[j][0]))
			table.setItem(j, 1, QTableWidgetItem(str(tuples[j][2])))
			table.setItem(j, 2, QTableWidgetItem(tuples[j][1]))

		table.setEditTriggers(QTableWidget.NoEditTriggers)

		table.resizeColumnsToContents()
		grid_layout.addWidget(table, 0, 0, 5, 5)
		self.lbtn = QPushButton('Сравнить', self)
		grid_layout.addWidget(self.lbtn, 7, 4)
		self.text = QTextEdit('', self)
		grid_layout.addWidget(self.text, 6, 0, 2, 4)
		self.tag = QLineEdit(self)
		self.tag.setMaximumSize(QSize(100, 30))
		grid_layout.addWidget(self.tag, 6, 4)
		self.lbtn.clicked.connect(self.compare)
		self.checker = 0

	def compare(self):
		if self.tag.text() in self.tags:
			if self.tag.text() not in self.multifiles:
				self.lblfunc(self.tag.text(), 0)
			else:
				self.checker = 1
				self.lblfunc(self.tag.text(), 1)
		else:
			self.text.setText('Некорректный ID')

	def lblfunc(self, txt, num):
		if num == 1:
			self.text.setText('')
		if self.checker == 1:
			cmd = txt + str(num)
		else:
			cmd = txt
		a = 'new/' + self.unit[cmd]
		b = 'old/' + self.unit[cmd]
		test_lines = open(a, 'r', encoding='utf-8').readlines()
		correct_lines = open(b, 'r', encoding='utf-8').readlines()

		self.text.setText('')
		newstr = self.unit[cmd] + '\nВсего строк (новый): ' + str(len(test_lines)) + '\nВсего строк (старый): ' + str(len(correct_lines))
		self.text.append(newstr)

		trlist = zip(test_lines, correct_lines)
		counter = 0
		err = 0
		for test, correct in trlist:
			counter += 1
			if test != correct:
				err = 1
				self.text.append('Изменение в строке ' + str(counter))
				break
		if err == 0:
			if self.checker == 1:
				if num + 1 <= int(self.unit[txt]):
					self.lblfunc(self.tag.text(), num + 1)
				else:
					self.text.setText('Всё совпадает')
					self.checker = 0
			else:
				self.text.setText('Всё совпадает')


if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	sys.exit(app.exec())
