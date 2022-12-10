import re
from scraping import scraping
from create_csv import creating_csv
from random_copying import random_copying
from сopying_dataset import copying_dataset
from iterator import Iterator
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication,
    QDesktopWidget,
    QLineEdit,
    QInputDialog,
    QLabel,
    QMainWindow,
    QFileDialog
)
from PyQt5.QtGui import QPixmap

class interface(QWidget):
    def __init__(self):
        super().__init__

    def initUI(self):
        
        self.btn_0 = QPushButton("Создать датасет", self)
        self.btn_0.move(50, 20)
        self.btn_0.clicked.connect(self.showDialog_0)
        self.btn_1 = QPushButton("Создать файл анотацию исходного датасета", self)
        self.btn_1.move(50, 60)
        self.btn_1.clicked.connect(self.showDialog_1)
        self.btn_2 = QPushButton("Создание датасета с другой организацией файлов", self)
        self.btn_2.move(50, 100)
        self.btn_2.clicked.connect(self.showDialog_2)
        self.btn_3 = QPushButton("Создание копии датасета", self)
        self.btn_3.move(50, 140)
        self.btn_3.clicked.connect(self.showDialog_3)
        self.btn_4 = QPushButton("Просмотр изображений", self)
        self.btn_4.move(50, 180)
        self.btn_4.clicked.connect(self.showDialog_4)
        self.label = QLabel(self)
        self.btn_6 = QPushButton("Далее", self)
        self.btn_6.move(200, 550)
        self.btn_6.clicked.connect(self.showDialog_6)
        self.label.move(50, 220)


    
    
    


