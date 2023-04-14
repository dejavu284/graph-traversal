import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

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
        self.ui.input_2.setPlaceholderText('Тип графа:')
        self.ui.input_3.setPlaceholderText('Способ обхода:')
        self.ui.input_4.setPlaceholderText('Ранг графа:')

        self.ui.Clear_btn.clicked.connect(self.clean_out)


    def is_text(self):
        if(
            (self.ui.input_1.text() is not None) | 
            (self.ui.input_2.text() is not None) | 
            (self.ui.input_3.text() is not None) | 
            (self.ui.input_4.text() is not None)):
            return True
        else: return False

    
    def setText(self, isClear,  n_top, type_graph, method, rang):
        if self.is_text():
            self.n_top = n_top
            self.type_graph = type_graph
            self.method = method
            self.rang = rang

    def getText(self):
        self.setText(
            self.ui.input_1.text(),
            self.ui.input_2.text(),
            self.ui.input_3.text(),
            self.ui.input_4.text())
        

    def clean_out(self):
        self.setText(None, None, None, None)
        self.ui.input_1.setText(None)
        self.ui.input_2.setText(None)
        self.ui.input_3.setText(None)
        self.ui.input_4.setText(None)


app = QtWidgets.QApplication([])
application = Lab5()
application.show()
sys.exit(app.exec())