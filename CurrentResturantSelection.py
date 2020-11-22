from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

#Import the interface file to display for each store's Menu
from MacdonaldMenu import Ui_MacDonaldMenu
from SubwayMenu import Ui_SubwayMenu
from ChickenRiceStoreMenu import Ui_ChickenRiceStoreMenu
from WesternFoodStoreMenu import Ui_WesternFoodStoreMenu
from DrinksStoreMenu import Ui_DrinksStoreMenu

import datetime

class Ui_CurrentResturantSelection(object):
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def DrinksStore_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_DrinksStoreMenu()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def WesternFoodStore_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_WesternFoodStoreMenu()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def ChickenRiceStore_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_ChickenRiceStoreMenu()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def Subway_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_SubwayMenu()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def MacDonald_button(self):
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_MacDonaldMenu()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to display current system time, date and day DONE BY: AIK YU CHEN
    def showTime(self):
        now = datetime.datetime.now()
        self.DayDateTimeLabel.setText(now.strftime("%a" + " " + "%d-%h-%Y" + " " + "%H:%M:%S"))

    #Code for the interface and main program
    def setupUi(self, CurrentResturantSelection):
        CurrentResturantSelection.setObjectName("CurrentResturantSelection")
        CurrentResturantSelection.resize(540, 555)
        CurrentResturantSelection.setStyleSheet("background-color: rgb(58, 45, 37)")

        self.DayDateTimeLabel = QtWidgets.QLabel(CurrentResturantSelection)
        self.DayDateTimeLabel.setGeometry(QtCore.QRect(10, 10, 521, 61))
        self.DayDateTimeLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DayDateTimeLabel.setFont(font)
        self.DayDateTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DayDateTimeLabel.setObjectName("DayDateTimeLabel")

        self.NorthSpineCanteen = QtWidgets.QLabel(CurrentResturantSelection)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(10, 100, 521, 71))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")

        self.MacDonaldButton = QtWidgets.QPushButton(CurrentResturantSelection)
        self.MacDonaldButton.setGeometry(QtCore.QRect(200, 180, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MacDonaldButton.setFont(font)
        self.MacDonaldButton.setObjectName("MacDonaldButton")
        self.MacDonaldButton.setIcon(QtGui.QIcon("Macdonald.png"))
        self.MacDonaldButton.setIconSize(QtCore.QSize(50,50))
        self.MacDonaldButton.setStyleSheet("background-color: red;")
        self.MacDonaldButton.clicked.connect(self.MacDonald_button)
        #Upon clicked, execute method to display restaurant's menu interface

        self.SubwayButton = QtWidgets.QPushButton(CurrentResturantSelection)
        self.SubwayButton.setGeometry(QtCore.QRect(200, 250, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SubwayButton.setFont(font)
        self.SubwayButton.setObjectName("SubwayButton")
        self.SubwayButton.setIcon(QtGui.QIcon("subway.png"))
        self.SubwayButton.setIconSize(QtCore.QSize(100,100))
        self.SubwayButton.setStyleSheet("background-color: green;")
        self.SubwayButton.clicked.connect(self.Subway_button)
        #Upon clicked, execute method to display restaurant's menu interface

        self.ChickenRiceStoreButton = QtWidgets.QPushButton(CurrentResturantSelection)
        self.ChickenRiceStoreButton.setGeometry(QtCore.QRect(200, 320, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ChickenRiceStoreButton.setFont(font)
        self.ChickenRiceStoreButton.setIcon(QtGui.QIcon("ChickenRiceStore.png"))
        self.ChickenRiceStoreButton.setIconSize(QtCore.QSize(140,250))
        self.ChickenRiceStoreButton.setStyleSheet("background-color: black;")
        self.ChickenRiceStoreButton.clicked.connect(self.ChickenRiceStore_button)
        #Upon clicked, execute method to display restaurant's menu interface

        self.WesternFoodStoreButton = QtWidgets.QPushButton(CurrentResturantSelection)
        self.WesternFoodStoreButton.setGeometry(QtCore.QRect(200, 390, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WesternFoodStoreButton.setFont(font)
        self.WesternFoodStoreButton.setObjectName("WesternFoodStoreButton")
        self.WesternFoodStoreButton.setIcon(QtGui.QIcon("WesternFoodStore.png"))
        self.WesternFoodStoreButton.setIconSize(QtCore.QSize(160,160))
        self.WesternFoodStoreButton.setStyleSheet("background-color: black;")
        self.WesternFoodStoreButton.clicked.connect(self.WesternFoodStore_button)
        #Upon clicked, execute method to display restaurant's menu interface

        self.DrinksStoreButton = QtWidgets.QPushButton(CurrentResturantSelection)
        self.DrinksStoreButton.setGeometry(QtCore.QRect(200, 460, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DrinksStoreButton.setFont(font)
        self.DrinksStoreButton.setObjectName("DrinksStoreButton")
        self.DrinksStoreButton.setIcon(QtGui.QIcon("DrinksStore.png"))
        self.DrinksStoreButton.setIconSize(QtCore.QSize(160,160))
        self.DrinksStoreButton.setStyleSheet("background-color: black;")
        self.DrinksStoreButton.clicked.connect(self.DrinksStore_button)
        #Upon clicked, execute method to display restaurant's menu interface

        self.BackButton = QtWidgets.QPushButton(CurrentResturantSelection)
        self.BackButton.setGeometry(QtCore.QRect(5, 505, 80, 40))
        self.BackButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(CurrentResturantSelection.close)
        self.BackButton.clicked.connect(CurrentResturantSelection.close)
        #Upon clicked, close this interface

        timer = QTimer(CurrentResturantSelection)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        #Timer used to update and execute the time methood every 1s

        self.retranslateUi(CurrentResturantSelection)
        QtCore.QMetaObject.connectSlotsByName(CurrentResturantSelection)

    def retranslateUi(self, CurrentResturantSelection):
        _translate = QtCore.QCoreApplication.translate
        CurrentResturantSelection.setWindowTitle(_translate("CurrentResturantSelection", "NorthSpineCanteen"))
        self.NorthSpineCanteen.setText(_translate("CurrentResturantSelection", "North Spine Canteen"))
        self.BackButton.setText(_translate("CurrentResturantSelection", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentResturantSelection = QtWidgets.QDialog()
    ui = Ui_CurrentResturantSelection()
    ui.setupUi(CurrentResturantSelection)
    CurrentResturantSelection.show()
    sys.exit(app.exec_())
