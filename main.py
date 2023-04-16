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
        self.ui.input_2.setToolTip('Взвешенный/невзвешанный')

        self.ui.input_3.setPlaceholderText('Способ обхода:')
        self.ui.input_3.setToolTip('В глубину/ширину/Дейкстры/...')

        self.ui.input_4.setPlaceholderText('Ранг графа:')
        self.ui.input_4.setToolTip('1/2/...')

        self.ui.Clear_btn.clicked.connect(self.clean_out)
        self.ui.Clear_btn.setToolTip('Очистить поля')

        self.ui.Create_btn.clicked.connect(self.create_matrix)

        self.ui.Random_btn.clicked.connect(self.setRandom)


    def prepare_one_rew_data(self, table):
        column_container = []
        try:
            for x in range(0, table.rowCount()):
                for y in range(0, table.columnCount()):    
                    column_container.append(table.item(x,y).text())
            return column_container
        except:
            return column_container
    

   # def setOutput(self):
        

    
    def setRandom(self):
        if self.is_text():
            self.n_top = int(self.ui.input_1.text())
            self.type_graph = self.ui.input_2.text()
            self.method = self.ui.input_3.text()
            self.rang = self.ui.input_4.text()
            self.ui.tableWidget.setRowCount(self.n_top)
            self.ui.tableWidget.setColumnCount(self.n_top)
            if self.type_graph == 'невзвешенный':
                self.counter = self.getRandomCell(self.n_top, False)
            else:
                self.counter = self.getRandomCell(self.n_top, True)
            self.ui.wayCount.setText(str(self.counter))
            self.ui.tableWidget.resizeColumnsToContents()
            self.changeText(False, True)


    def getRandomCell(self, n_top, weight):
        counter = 0
        for i in range(n_top):
            for j in range(i, n_top):
                if weight:
                    if i == j:
                        self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(0)))
                    else:
                        value = random.randrange(0,20)
                        self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
                        self.ui.tableWidget.setItem(j, i, QTableWidgetItem(str(value)))
                        if value != 0:
                            counter += 1 
                else:
                    if i == j:
                        self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(0)))
                    else:
                        value = random.randrange(0,2)
                        self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
                        self.ui.tableWidget.setItem(j, i, QTableWidgetItem(str(value)))
                        if value != 0:
                            counter += 1

        return counter


    def create_matrix(self):
        if self.is_text():
            self.setText(False)
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


    def setText(self, isClear):#, isClear,  n_top, type_graph, method, rang):
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
        self.setText(False)
        

    def changeText(self, isClear, isRandom):
        if isClear:
            self.ui.input_1.setText(None)
            self.ui.input_2.setText(None)
            self.ui.input_3.setText(None)
            self.ui.input_4.setText(None)
        elif isRandom:
            self.ui.input_1.setText(str(self.n_top))
            self.ui.input_2.setText(self.type_graph)
            self.ui.input_3.setText(self.method)
            self.ui.input_4.setText(str(self.rang))


    def clean_out(self):
        self.setText(True)
        self.changeText(True, False)


# class graph:
    # def __init__(self):


app = QtWidgets.QApplication([])
application = Lab5()
application.show()
sys.exit(app.exec())