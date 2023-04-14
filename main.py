import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import random


class Lab5(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lab5, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    
    def init_ui(self):
        self.setWindowTitle('Обход Графа')
        self.setWindowIcon(QIcon('Discord.ico'))

        self.ui.input_1.setPlaceholderText('Количество вершин:')
        self.ui.input_1.setToolTip('Введите желаемое количество вершин')

        self.ui.input_2.setPlaceholderText('Тип графа:')
        self.ui.input_2.setToolTip('Взвешенный/не взвешанный')

        self.ui.input_3.setPlaceholderText('Способ обхода:')
        self.ui.input_3.setToolTip('В глубину/ширину/Дейкстры/...')

        self.ui.input_4.setPlaceholderText('Ранг графа:')
        self.ui.input_4.setToolTip('1/2/...')

        self.ui.Clear_btn.clicked.connect(self.clean_out)
        self.ui.Clear_btn.setToolTip('Очистить поля')

        self.ui.Create_btn.clicked.connect(self.foo)

        self.ui.Random_btn.clicked.connect(self.setRandom)

    
    def setRandom(self):
        n_top = random.randrange(1, 16)
        self.ui.tableWidget.setRowCount(n_top)
        self.ui.tableWidget.setColumnCount(n_top)
        self.ui.OutputText.setText(str(n_top))
        for i in range(n_top):
            for j in range(n_top):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(random.randrange(0,2))))
        self.ui.tableWidget.resizeColumnsToContents()
            


    def foo(self):
        if self.is_text():
            self.setText(False, False)
            self.ui.OutputText.setText(str(self.n_top))
            self.ui.tableWidget.setRowCount(self.n_top)
            self.ui.tableWidget.setColumnCount(self.n_top)
            self.ui.tableWidget.resizeColumnsToContents()
            #for i in range(self.n_top):
            #   self.ui.tableWidget.setColumnWidth(i, 50)
            



    def is_text(self):
        if self.ui.input_1.text() != '':
            if self.ui.input_2.text() != '':
                if self.ui.input_3.text() != '':
                    if self.ui.input_4.text() != '': return True
        else: return False

    
    def setText(self, isClear, Random):#, isClear,  n_top, type_graph, method, rang):
        flag = False
        if isClear:
            self.n_top = None
            self.type_graph = None
            self.method = None
            self.rang = None


        elif self.is_text():
            self.n_top = int(self.ui.input_1.text())
            self.type_graph = self.ui.input_2.text()
            self.method = self.ui.input_3.text()
            self.rang = int(self.ui.input_4.text())
            flag = True
        
        return flag

    def getText(self):
        self.setText(False, False)
        

    def clean_out(self):
        self.setText(True, False)
        self.ui.input_1.setText(None)
        self.ui.input_2.setText(None)
        self.ui.input_3.setText(None)
        self.ui.input_4.setText(None)


app = QtWidgets.QApplication([])
application = Lab5()
application.show()
sys.exit(app.exec())