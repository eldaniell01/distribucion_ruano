import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt6.QtGui import QFont

from db.db_c import CMysql
from datetime import datetime

class Order(QMainWindow):
    def __init__(self):
        super().__init__()
        self.orderC = uic.loadUi('views/orders.ui')
        self.orderC.show()
        self.orderC.buttonPhotos.clicked.connect(self.openImagen)
        self.orderC.buttonInsert.clicked.connect(self.insertOrder)
        self.con = CMysql()
        self.con.connection()
        self.showTable()
        self.showOptions()
    
    def showTable(self):
        columns = ['ID', 'CLIENTE', 'TELEFONO', 'MOTO', 'MODELO', 'MARCA', 'DESCRIPCION', 'VENDEDOR', 'ESTADO']
        self.orderC.tableR.setFont(QFont('FiraCode Nerd Font', 12))
        self.orderC.tableR.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.orderC.tableR.setHorizontalHeaderItem(column, QTableWidgetItem(name))
    
    def showOptions(self):
        year = 2000
        options = [str(year +x) for x in range(25)]
        self.orderC.textYear.addItems(options)

    def openImagen(self):
        folder = QFileDialog()
        folder_path, __= folder.getOpenFileNames(None, 'Cargar imagen', '', 'JPEG (*.jpg)')
        print(folder_path)
        
    def insertOrder(self):
        self.name = self.orderC.textName.text()
        self.phone = self.orderC.textPhone.setMaxLength(8)
        self.moto = self.orderC.textMoto.text()
        self.modelo = self.orderC.textYear.currentText()
        self.marca = self.orderC.textMarca.text()
        self.description = self.orderC.textDescription.toPlainText()
        self.salesmen = self.orderC.textSalesmen.text()
        self.state = False
        if not self.name or self.phone or self.moto:
            print('hay campos vacios')
        else:
            row_count = self.orderC.tableR.rowCount()
            self.orderC.tableR.insertRow(row_count)
            self.orderC.tableR.setItem(row_count, 1, QTableWidgetItem(self.name))
            self.orderC.tableR.setItem(row_count, 2, QTableWidgetItem(self.phone))
            self.orderC.tableR.setItem(row_count, 3, QTableWidgetItem(self.moto))
            self.orderC.tableR.setItem(row_count, 4, QTableWidgetItem(self.modelo))
            self.orderC.tableR.setItem(row_count, 5, QTableWidgetItem(self.marca))
            self.orderC.tableR.setItem(row_count, 6, QTableWidgetItem(self.description))
            self.orderC.tableR.setItem(row_count, 7, QTableWidgetItem(self.salesmen))
            self.orderC.tableR.setItem(row_count, 8, QTableWidgetItem(str(self.state)))
            self.orderC.textName.setText('')
            self.orderC.textPhone.setText('')
            self.orderC.textMoto.setText('')
            self.showOptions()
            self.orderC.textMarca.setText('')
            self.orderC.textDescription.setPlainText('')
            self.orderC.textSalesmen.setText('') 
        