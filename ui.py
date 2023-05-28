# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 820)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color:#22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setToolTip("")
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: white\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 1, 1920, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableWidget::item{\n"
"background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"border-color:green;\n"
"}\n"
"\n"
"\n"
"QTableWidget::item:selected{\n"
"background-color: red;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"border-color:blue;\n"
"color: green;\n"
"}\n"
"")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.graphTravel_2 = QtWidgets.QLabel(self.tab_3)
        self.graphTravel_2.setGeometry(QtCore.QRect(0, 0, 571, 221))
        self.graphTravel_2.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graphTravel_2.setFont(font)
        self.graphTravel_2.setText("")
        self.graphTravel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphTravel_2.setObjectName("graphTravel_2")
        self.minWay = QtWidgets.QLabel(self.tab_3)
        self.minWay.setGeometry(QtCore.QRect(0, 220, 571, 201))
        self.minWay.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.minWay.setFont(font)
        self.minWay.setText("")
        self.minWay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.minWay.setObjectName("minWay")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineHeuristic = QtWidgets.QLineEdit(self.frame)
        self.lineHeuristic.setText("")
        self.lineHeuristic.setObjectName("lineHeuristic")
        self.verticalLayout_4.addWidget(self.lineHeuristic)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.graphTravel = QtWidgets.QLabel(self.frame)
        self.graphTravel.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graphTravel.setFont(font)
        self.graphTravel.setObjectName("graphTravel")
        self.horizontalLayout_4.addWidget(self.graphTravel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.wayCount = QtWidgets.QLabel(self.frame)
        self.wayCount.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wayCount.setFont(font)
        self.wayCount.setObjectName("wayCount")
        self.horizontalLayout_5.addWidget(self.wayCount)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addWidget(self.frame)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.countLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countLine.sizePolicy().hasHeightForWidth())
        self.countLine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.countLine.setFont(font)
        self.countLine.setToolTip("")
        self.countLine.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 10;\n"
"color: white")
        self.countLine.setText("")
        self.countLine.setAlignment(QtCore.Qt.AlignCenter)
        self.countLine.setObjectName("countLine")
        self.verticalLayout_3.addWidget(self.countLine)
        self.startLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLine.sizePolicy().hasHeightForWidth())
        self.startLine.setSizePolicy(sizePolicy)
        self.startLine.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 10;\n"
"color: white")
        self.startLine.setAlignment(QtCore.Qt.AlignCenter)
        self.startLine.setObjectName("startLine")
        self.verticalLayout_3.addWidget(self.startLine)
        self.stopLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopLine.sizePolicy().hasHeightForWidth())
        self.stopLine.setSizePolicy(sizePolicy)
        self.stopLine.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 10;\n"
"color: white")
        self.stopLine.setAlignment(QtCore.Qt.AlignCenter)
        self.stopLine.setObjectName("stopLine")
        self.verticalLayout_3.addWidget(self.stopLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("color:white")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.notweightRB = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notweightRB.sizePolicy().hasHeightForWidth())
        self.notweightRB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.notweightRB.setFont(font)
        self.notweightRB.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.195219 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border: 1px solid rgba(255, 14, 23, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.notweightRB.setObjectName("notweightRB")
        self.verticalLayout.addWidget(self.notweightRB)
        self.weightRB = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightRB.sizePolicy().hasHeightForWidth())
        self.weightRB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weightRB.setFont(font)
        self.weightRB.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.195219 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border: 1px solid rgba(255, 14, 23, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.weightRB.setCheckable(True)
        self.weightRB.setChecked(False)
        self.weightRB.setObjectName("weightRB")
        self.verticalLayout.addWidget(self.weightRB)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet("color:white")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackRB = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackRB.sizePolicy().hasHeightForWidth())
        self.stackRB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stackRB.setFont(font)
        self.stackRB.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.195219 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border: 1px solid rgba(255, 14, 23, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.stackRB.setObjectName("stackRB")
        self.verticalLayout_2.addWidget(self.stackRB)
        self.queueRB = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queueRB.sizePolicy().hasHeightForWidth())
        self.queueRB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.queueRB.setFont(font)
        self.queueRB.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.195219 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border: 1px solid rgba(255, 14, 23, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.queueRB.setObjectName("queueRB")
        self.verticalLayout_2.addWidget(self.queueRB)
        self.daRB = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daRB.sizePolicy().hasHeightForWidth())
        self.daRB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.daRB.setFont(font)
        self.daRB.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.195219 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border: 1px solid rgba(255, 14, 23, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.daRB.setObjectName("daRB")
        self.verticalLayout_2.addWidget(self.daRB)
        self.aaRB = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aaRB.sizePolicy().hasHeightForWidth())
        self.aaRB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.aaRB.setFont(font)
        self.aaRB.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.195219 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border: 1px solid rgba(255, 14, 23, 255);\n"
"border-radius: 5px;\n"
"border-style: outset;")
        self.aaRB.setObjectName("aaRB")
        self.verticalLayout_2.addWidget(self.aaRB)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.go_btn.setFont(font)
        self.go_btn.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.651741 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #fb5b5d\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: #fa4244\n"
"}")
        self.go_btn.setFlat(False)
        self.go_btn.setObjectName("go_btn")
        self.horizontalLayout.addWidget(self.go_btn)
        self.Clear_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Clear_btn.setFont(font)
        self.Clear_btn.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.651741 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #fb5b5d\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: #fa4244\n"
"}")
        self.Clear_btn.setObjectName("Clear_btn")
        self.horizontalLayout.addWidget(self.Clear_btn)
        self.Random_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Random_btn.setFont(font)
        self.Random_btn.setStyleSheet("QPushButton {\n"
"color: white;\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.651741 rgba(255, 14, 23, 255), stop:1 rgba(0, 0, 0, 0));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #fb5b5d\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: #fa4244\n"
"}")
        self.Random_btn.setObjectName("Random_btn")
        self.horizontalLayout.addWidget(self.Random_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_7)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ОБХОД ГРАФА"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab2"))
        self.label_2.setText(_translate("MainWindow", "Обход:"))
        self.graphTravel.setText(_translate("MainWindow", "----------------"))
        self.label_3.setText(_translate("MainWindow", "Количество путей:"))
        self.wayCount.setText(_translate("MainWindow", "-------------------------"))
        self.groupBox.setTitle(_translate("MainWindow", "Тип графа"))
        self.notweightRB.setText(_translate("MainWindow", "Невзвешанный"))
        self.weightRB.setText(_translate("MainWindow", "Взвешанный"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Метод обхода"))
        self.stackRB.setText(_translate("MainWindow", "В глубину"))
        self.queueRB.setText(_translate("MainWindow", "В ширину"))
        self.daRB.setText(_translate("MainWindow", "Дейкстры"))
        self.aaRB.setText(_translate("MainWindow", "А star"))
        self.go_btn.setText(_translate("MainWindow", "GO"))
        self.Clear_btn.setText(_translate("MainWindow", "Clear"))
        self.Random_btn.setText(_translate("MainWindow", "Random"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
