# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Oct 25 16:01:34 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView = GarphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rootComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.rootComboBox.setObjectName("rootComboBox")
        self.horizontalLayout.addWidget(self.rootComboBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scaleComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.scaleComboBox.setObjectName("scaleComboBox")
        self.horizontalLayout_2.addWidget(self.scaleComboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tuningComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.tuningComboBox.setObjectName("tuningComboBox")
        self.horizontalLayout_4.addWidget(self.tuningComboBox)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.boxPatternRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.boxPatternRadioButton.setChecked(True)
        self.boxPatternRadioButton.setObjectName("boxPatternRadioButton")
        self.verticalLayout.addWidget(self.boxPatternRadioButton)
        self.threeNotesRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.threeNotesRadioButton.setObjectName("threeNotesRadioButton")
        self.verticalLayout.addWidget(self.threeNotesRadioButton)
        self.fourNotesRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.fourNotesRadioButton.setObjectName("fourNotesRadioButton")
        self.verticalLayout.addWidget(self.fourNotesRadioButton)
        self.oneStringRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.oneStringRadioButton.setObjectName("oneStringRadioButton")
        self.verticalLayout.addWidget(self.oneStringRadioButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.firstPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.firstPushButton.setObjectName("firstPushButton")
        self.verticalLayout_2.addWidget(self.firstPushButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.prevPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevPushButton.setObjectName("prevPushButton")
        self.horizontalLayout_3.addWidget(self.prevPushButton)
        self.nextPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextPushButton.setObjectName("nextPushButton")
        self.horizontalLayout_3.addWidget(self.nextPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.allPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.allPushButton.setObjectName("allPushButton")
        self.verticalLayout_2.addWidget(self.allPushButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 2, 1)
        self.startAnimPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startAnimPushButton.setObjectName("startAnimPushButton")
        self.gridLayout.addWidget(self.startAnimPushButton, 3, 2, 2, 1)
        self.closePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.closePushButton.setObjectName("closePushButton")
        self.gridLayout.addWidget(self.closePushButton, 4, 0, 2, 1)
        self.stopAnimPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopAnimPushButton.setObjectName("stopAnimPushButton")
        self.gridLayout.addWidget(self.stopAnimPushButton, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCompare = QtWidgets.QAction(MainWindow)
        self.actionCompare.setObjectName("actionCompare")
        self.actionSave_To_File = QtWidgets.QAction(MainWindow)
        self.actionSave_To_File.setObjectName("actionSave_To_File")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionCompare)
        self.menuFile.addAction(self.actionSave_To_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.label.setBuddy(self.rootComboBox)
        self.label_2.setBuddy(self.scaleComboBox)

        self.retranslateUi(MainWindow)
        self.closePushButton.clicked.connect(MainWindow.close)
        self.firstPushButton.clicked.connect(MainWindow.drawFirstPos)
        self.prevPushButton.clicked.connect(MainWindow.drawPrevPos)
        self.nextPushButton.clicked.connect(MainWindow.drawNextPos)
        self.allPushButton.clicked.connect(MainWindow.drawAllPos)
        self.startAnimPushButton.clicked.connect(MainWindow.startAnimation)
        self.stopAnimPushButton.clicked.connect(MainWindow.stopAnimation)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graphicsView, self.rootComboBox)
        MainWindow.setTabOrder(self.rootComboBox, self.scaleComboBox)
        MainWindow.setTabOrder(self.scaleComboBox, self.boxPatternRadioButton)
        MainWindow.setTabOrder(self.boxPatternRadioButton, self.threeNotesRadioButton)
        MainWindow.setTabOrder(self.threeNotesRadioButton, self.fourNotesRadioButton)
        MainWindow.setTabOrder(self.fourNotesRadioButton, self.oneStringRadioButton)
        MainWindow.setTabOrder(self.oneStringRadioButton, self.firstPushButton)
        MainWindow.setTabOrder(self.firstPushButton, self.prevPushButton)
        MainWindow.setTabOrder(self.prevPushButton, self.nextPushButton)
        MainWindow.setTabOrder(self.nextPushButton, self.allPushButton)
        MainWindow.setTabOrder(self.allPushButton, self.startAnimPushButton)
        MainWindow.setTabOrder(self.startAnimPushButton, self.stopAnimPushButton)
        MainWindow.setTabOrder(self.stopAnimPushButton, self.closePushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guitar"))
        self.label.setText(_translate("MainWindow", "Root Note"))
        self.label_2.setText(_translate("MainWindow", "Scale Name"))
        self.label_3.setText(_translate("MainWindow", "Tuning"))
        self.boxPatternRadioButton.setText(_translate("MainWindow", "Box Pattern"))
        self.threeNotesRadioButton.setText(_translate("MainWindow", "Three Notes Per String"))
        self.fourNotesRadioButton.setText(_translate("MainWindow", "Four Notes Per Sting"))
        self.oneStringRadioButton.setText(_translate("MainWindow", "One String"))
        self.firstPushButton.setText(_translate("MainWindow", "Show First"))
        self.prevPushButton.setText(_translate("MainWindow", "Previous"))
        self.nextPushButton.setText(_translate("MainWindow", "Next"))
        self.allPushButton.setText(_translate("MainWindow", "Show All"))
        self.startAnimPushButton.setText(_translate("MainWindow", "Start Animation"))
        self.closePushButton.setText(_translate("MainWindow", "Close"))
        self.stopAnimPushButton.setText(_translate("MainWindow", "Stop Animation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionCompare.setText(_translate("MainWindow", "Compare"))
        self.actionSave_To_File.setText(_translate("MainWindow", "Save To File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

from GarphicsView import GarphicsView
