import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt6.QtGui import QFont

from db.querys import Querys
from datetime import date

class Order(QMainWindow):
    def __init__(self):
        super().__init__()
        self.orderC = uic.loadUi('views/orders.ui')
        self.orderC.show()
        self.orderC.buttonPhotos.clicked.connect(self.openImagen)
        self.orderC.buttonInsert.clicked.connect(self.insertOrder)
        self.showTable()
        self.showOptions()
        self.img = []
    
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
        self.img = folder_path
        
    def insertOrder(self):
        print(self.img)
        self.name = self.orderC.textName.text()
        self.phone = int(self.orderC.textPhone.text())
        self.moto = self.orderC.textMoto.text()
        self.modelo = int(self.orderC.textYear.currentText())
        self.marca = self.orderC.textMarca.text()
        self.description = self.orderC.textDescription.toPlainText()
        self.salesmen = self.orderC.textSalesmen.text()
        self.state = 0
        
        if self.name and self.phone and self.moto:
            #self.insertCliente = Querys()
            #self.insertCliente.insertCliente(self.name, self.phone)
            fecha = date.today()
            print(fecha)
            idc = Querys()
            data = idc.selectDetailOrder()
            inf = Querys()
            for ruta_imagen in self.img:
                with open(ruta_imagen, 'rb') as file:
                    imagen_binaria = file.read()
                    inf.insertImages(imagen_binaria, data[0])
            print(data[0])
            row_count = self.orderC.tableR.rowCount()
            self.orderC.tableR.insertRow(row_count)
            self.orderC.tableR.setItem(row_count, 1, QTableWidgetItem(self.name))
            self.orderC.tableR.setItem(row_count, 2, QTableWidgetItem(str(self.phone)))
            self.orderC.tableR.setItem(row_count, 3, QTableWidgetItem(self.moto))
            self.orderC.tableR.setItem(row_count, 4, QTableWidgetItem(str(self.modelo)))
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
        else:    
            print(self.name)