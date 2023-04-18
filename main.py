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
        self.countValue = 6
        self.startValue = 'g'
        self.stopValue = 'g'
        self.rang = 1
        self.flag_1 = False
        self.flag_1 = False

        self.setWindowTitle('Обход Графа')
        self.setWindowIcon(QIcon('Discord.ico'))

        self.ui.countLine.setPlaceholderText('Кол-во:')
        self.ui.countLine.setToolTip('Введите желаемое количество вершин')

        self.ui.startLine.setPlaceholderText('От:')
        self.ui.startLine.setToolTip('От какой вершины совершить обход')

        self.ui.stopLine.setPlaceholderText('До:')
        self.ui.stopLine.setToolTip('До какой вершины совершить обход')

        self.ui.rangLine.setPlaceholderText('Ранг:')
        self.ui.rangLine.setToolTip('1/2/...')

        self.ui.Clear_btn.clicked.connect(self.clean_out)
        self.ui.Clear_btn.setToolTip('Очистить поля')

        self.ui.go_btn.clicked.connect(self.foo)

        self.ui.Random_btn.clicked.connect(self.setRandom)

        self.ui.weightRB.toggled.connect(self.clickedRB_first)
        self.ui.notweightRB.toggled.connect(self.clickedRB_first)

        self.ui.stackRB.toggled.connect(self.clickedRB_second)
        self.ui.queueRB.toggled.connect(self.clickedRB_second)
        self.ui.daRB.toggled.connect(self.clickedRB_second)
        self.ui.aaRB.toggled.connect(self.clickedRB_second)


    def clickedRB_first(self): self.flag_1 = True
    def clickedRB_second(self): self.flag_2 = True


    def prepare_one_rew_data(self, table):
        column_container = []
        try:
            for x in range(0, table.rowCount()):
                for y in range(0, table.columnCount()):    
                    column_container.append(table.item(x,y).text())
            return column_container
        except:
            return column_container
    
    def foo(self):
        self.graphTraversal(self.ui.tableWidget)

    def graphTraversal(self, table):
        arr = []
        for i in range(0, table.rowCount()):
            arr.append(f'{i+1}:')
            for j in range(0, table.columnCount()):
                if table.item(i,j).text() == "1":
                    arr.append(j+1)
            arr.append('|')
        print(arr)


    def queue(self, arr, item):
        arr.insert(0, item)
    

    def dequeue(self, arr):
        item = arr[0]
        arr.delete(0)
        return item

    
    def setRandom(self):
        if self.is_text():
            self.countValue = int(self.ui.countLine.text())
            self.startValue = self.ui.startLine.text()
            self.stopValue = self.ui.stopLine.text()
            self.rang = self.ui.rangLine.text()

            if self.flag_1:
                self.ui.tableWidget.setRowCount(self.countValue)
                self.ui.tableWidget.setColumnCount(self.countValue)
                if self.ui.notweightRB.isChecked():
                    self.counter = self.getRandomCell(self.countValue, False)
                else:
                    self.counter = self.getRandomCell(self.countValue, True)

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


    def go_travel(self):
        if self.is_text():
            self.setText(False)
            
            #for i in range(self.n_top):
            #   self.ui.tableWidget.setColumnWidth(i, 50)


    def is_text(self):
        if self.ui.countLine.text() != '':
            if self.ui.startLine.text() != '':
                if self.ui.stopLine.text() != '':
                    if self.ui.rangLine.text() != '': return True
        else: return False


    def setText(self, isClear):
        flag = False
        if isClear:
            self.countValue = None
            self.startValue = None
            self.stopValue = None
            self.rang = None

        elif self.is_text():
            self.countValue = int(self.ui.countLine.text())
            self.startValue = self.ui.startLine.text()
            self.stopValue = self.ui.stopLine.text()
            self.rang = int(self.ui.rangLine.text())
            flag = True
        
        return flag

    def getText(self):
        self.setText(False)
        

    def changeText(self, isClear, isRandom):
        if isClear:
            self.ui.countLine.setText(None)
            self.ui.startLine.setText(None)
            self.ui.stopLine.setText(None)
            self.ui.rangLine.setText(None)
        elif isRandom:
            self.ui.countLine.setText(str(self.countValue))
            self.ui.startLine.setText(self.startValue)
            self.ui.stopLine.setText(self.stopValue)
            self.ui.rangLine.setText(str(self.rang))


    def clean_out(self):
        if self.is_text():    
            for i in range(self.countValue):
                self.ui.tableWidget.removeRow(0)
                self.ui.tableWidget.removeColumn(0)
            self.setText(True)
            self.changeText(True, False)


# class graph:
    # def __init__(self):


app = QtWidgets.QApplication([])
application = Lab5()
application.show()
sys.exit(app.exec())