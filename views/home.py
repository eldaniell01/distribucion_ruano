import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from .orderMain import OrderMain

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi('views/home.ui')
        self.main.show()
        self.main.buttonOrder.clicked.connect(self.openOrderMain)
        
        
    
    def openOrderMain(self):
        self.order = OrderMain()
        self.main.close() 
