import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt6.QtGui import QFont
from datetime import datetime

class OrderMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.order = uic.loadUi('views/orderMain.ui')
        self.order.show()
        self.order.dateOrder.setDate(datetime.now().date())
        self.order.dateOrder.editingFinished.connect(self.searchDate)
        self.showTable()
        
    def searchDate(self):
        print('fecha nueva')
        
    def showTable(self):
        columns = ['ID', 'CLIENTE', 'TELEFONO', 'MOTO', 'MODELO', 'MARCA', 'DESCRIPCION', 'VENDEDOR', 'ESTADO', 'OPCIONES']
        self.order.tableOrder.setFont(QFont('FiraCode Nerd Font', 12))
        self.order.tableOrder.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.order.tableOrder.setHorizontalHeaderItem(column, QTableWidgetItem(name))