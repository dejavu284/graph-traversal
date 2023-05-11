import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from ui import Ui_MainWindow
import random
import copy
from typing import List, Dict
import heapq


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
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\Я\Desktop\читы жизнь\Study\Programming\0_Jupyter\GUI Apps\lab5\snap.png'))

        
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

        self.ui.go_btn.clicked.connect(self.goTravel)

        self.ui.Random_btn.clicked.connect(self.setRandom)

        self.ui.weightRB.toggled.connect(self.clickedRB_first)
        self.ui.notweightRB.toggled.connect(self.clickedRB_first)

        self.ui.stackRB.toggled.connect(self.clickedRB_second)
        self.ui.queueRB.toggled.connect(self.clickedRB_second)
        self.ui.daRB.toggled.connect(self.clickedRB_second)
        self.ui.aaRB.toggled.connect(self.clickedRB_second)


    def dijkstra(graph: Dict[str, Dict[str, int]], start_node: str) -> List[int]:
        """
        Реализация алгоритма Дейкстры для нахождения кратчайшего пути в ориентированном графе с неотрицательными весами
        ребер от заданной начальной вершины до всех остальных вершин графа.

        :param graph: словарь, представляющий ориентированный граф с неотрицательными весами ребер;
                    ключами являются названия вершин графа, а значениями словари, в которых ключами являются названия
                    смежных вершин, а значениями - веса соответствующих ребер;
                    например, {'A': {'B': 2, 'C': 5}, 'B': {'D': 3}, 'C': {'D': 1}, 'D': {}}
        :param start_node: название начальной вершины графа
        :return: список длин кратчайших путей от начальной вершины до всех остальных вершин графа,
                в котором на i-ой позиции находится длина кратчайшего пути от начальной вершины до i-ой вершины графа
        """

        # Инициализация списка длин кратчайших путей и списка предшествующих вершин
        distances = {node: float('inf') for node in graph}
        distances[start_node] = 0
        predecessors = {node: None for node in graph}

        # Инициализация очереди с приоритетами
        pq = [(0, start_node)]

        while pq:
            # Извлечение вершины с наименьшим расстоянием из начальной вершины из очереди с приоритетами
            current_distance, current_node = heapq.heappop(pq)

            # Если текущее расстояние до текущей вершины меньше, чем значение в списке длин кратчайших путей,
            # то обновляем список длин кратчайших путей для текущей вершины и список предшествующих вершин
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Возвращаем список длин кратчайших путей от начальной вершины до всех остальных вершин графа
        return list(distances.values())


    def clickedRB_first(self): self.flag_1 = True
    def clickedRB_second(self): self.flag_2 = True


    # def createTable(self):



    def prepare_one_rew_data(self, table):
        column_container = []
        try:
            for x in range(0, table.rowCount()):
                for y in range(0, table.columnCount()):    
                    column_container.append(table.item(x,y).text())
            return column_container
        except:
            return column_container
    
    def goTravel(self):
        self.graphTraversal(self.ui.tableWidget)


    def setStr(self, Dict):
        string = ''
        for d in Dict:
            string += f'{d}: {Dict[d]}'
            string += '\n'
        return string
    

    def countWay(self):
        counter = 0
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(self.ui.tableWidget.columnCount()):
                if self.ui.tableWidget.item(i,j).text() != "0":
                    counter += 1
        counter = counter//2 + counter % 2
        return counter


    def graphTraversal(self, table):
        temp = []
        Dict = dict()
        for i in range(0, table.rowCount()):
            for j in range(0, table.columnCount()):
                if table.item(i,j).text() != "0":
                    temp.append(f'{j+1}')
            Dict[f'{i+1}'] = copy.deepcopy(temp)
            temp = []
        self.ui.graphTravel_2.setText(self.setStr(Dict))
        print(self.setStr(Dict))
        print(f'Dict is: {Dict}')

        queue = []; traversal = []; checked = []
        d = '1' 
        if self.ui.stackRB.isChecked():
            self.travelIn(d, traversal, checked, queue, Dict, self.stack, self.pop, self.travelIn)
        elif self.ui.queueRB.isChecked():
            self.travelIn(d, traversal, checked, queue, Dict, self.queue, self.dequeue, self.travelIn)
            
        if len(traversal) != self.countValue:
            for i in range(1, self.countValue + 1):
                if i not in traversal:
                    traversal.append(i)

        self.ui.wayCount.setText(str(self.countWay()))
        self.ui.graphTravel.setText(str(traversal))


    def travelIn(self, d, traversal, checked, queue1, Dict, foo1, foo2, foo3):
        if int(d) not in traversal:
            traversal.append(int(d))
        if int(d) not in checked:
            checked.append(int(d))
        for i in Dict[d]:
            if int(i) not in checked:
                foo1(queue1, int(i))
                checked.append(int(i))
        d = str(foo2(queue1))
        if d != 'None':
            foo3(d, traversal, checked, queue1, Dict, foo1, foo2, foo3)


    def stack(self, arr, item):
        arr.append(item)


    def pop(self, arr):
        if len(arr) != 0:
            item = arr[-1]
            arr.pop(-1)
            return item


    def queue(self, arr, item):
        arr.append(item)


    def dequeue(self, arr):
        if len(arr) != 0:
            item = arr[0]
            arr.pop(0)
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


    def is_text(self):
        if self.ui.countLine.text() != '':
            # if self.ui.startLine.text() != '':
            #     if self.ui.stopLine.text() != '':
            #         if self.ui.rangLine.text() != '': 
            return True
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
            self.ui.graphTravel.setText('------------------------')
            self.ui.wayCount.setText('------------------------')
            self.setText(True)
            self.changeText(True, False)


# class graph:
    # def __init__(self):


app = QtWidgets.QApplication([])
application = Lab5()
application.show()
sys.exit(app.exec())