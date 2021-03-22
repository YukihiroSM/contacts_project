# -*-coding: utf-8 -*-

from PyQt5.QtGui import QOpenGLDebugMessage
from PyQt5.QtWidgets import (QHBoxLayout, 
QMainWindow, 
QWidget,
QAbstractItemView, 
QPushButton, 
QVBoxLayout, 
QTableView)

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("InContact")
        self.resize(600, 400)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()
    def setupUI(self):
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        self.addButton = QPushButton('Добавить')
        self.delButton = QPushButton("Удалить")
        self.clearButton = QPushButton("Очистить всё")

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.delButton)
        layout.addStretch()
        layout.addWidget(self.clearButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)