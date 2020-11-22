from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

#Import the interface file for Current Operating Restaurants
#and User Input Operating Restaurants
from CurrentResturantSelection import Ui_CurrentResturantSelection
from UserInputSelection import Ui_UserInputSelection

import datetime

class Ui_MainInterface(object):
    #Methods used to open the Current Operating Restaurants Interface DONE BY: AKSHAT
    def current_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_CurrentResturantSelection()
        self.ui.setupUi(self.window)
        MainInterface.hide()
        self.window.exec()
        MainInterface.show()
        
    #Methods used to open the User Input Operating Resturants Interface DONE BY: AKSHAT
    def userinput_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UserInputSelection()
        self.ui.setupUi(self.window)
        MainInterface.hide()
        self.window.exec()
        MainInterface.show()

    #Methods used to display current system time, date and day DONE BY: AIK YU CHEN
    def showTime(self):
        now = datetime.datetime.now()
        self.DayDateTimeLabel.setText(now.strftime("%a" + " " + "%d-%h-%Y" + " " + "%H:%M:%S"))

    #Code for the interface and main program   
    def setupUi(self, MainInterface):
        MainInterface.setObjectName("MainInterface")
        MainInterface.resize(540, 555)
        MainInterface.setStyleSheet("background-color: rgb(58, 45, 37)")

        
        self.DayDateTimeLabel = QtWidgets.QLabel(MainInterface)
        self.DayDateTimeLabel.setGeometry(QtCore.QRect(10, 10, 521, 61))
        self.DayDateTimeLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DayDateTimeLabel.setFont(font)
        self.DayDateTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DayDateTimeLabel.setObjectName("DayDateTimeLabel")
        
        self.NorthSpineCanteen = QtWidgets.QLabel(MainInterface)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(10, 100, 521, 71))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")  
        
        
        self.CurrentResturantButton = QtWidgets.QPushButton(MainInterface)
        self.CurrentResturantButton.setGeometry(QtCore.QRect(150, 330, 265, 50))
        self.CurrentResturantButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CurrentResturantButton.setFont(font)
        self.CurrentResturantButton.setObjectName("CurrentResturantButton")
        self.CurrentResturantButton.clicked.connect(self.current_button)
        #Upon clicked, execute method to display Current Operating Restaurant Interface
        
        self.UserInputButton = QtWidgets.QPushButton(MainInterface)
        self.UserInputButton.setGeometry(QtCore.QRect(150, 410, 265, 50))
        self.UserInputButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UserInputButton.setFont(font)
        self.UserInputButton.setObjectName("UserInputButton")
        self.UserInputButton.clicked.connect(self.userinput_button)
        #Upon clicked, execute method to display User Input Operating Restaurant Interface
        
        timer = QTimer(MainInterface)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        #Timer used to update and execute the time methood every 1s
        
        self.retranslateUi(MainInterface)
        QtCore.QMetaObject.connectSlotsByName(MainInterface)
  
    def retranslateUi(self, MainInterface):
        _translate = QtCore.QCoreApplication.translate
        MainInterface.setWindowTitle(_translate("MainInterface", "NorthSpineCanteen"))
        self.NorthSpineCanteen.setText(_translate("MainInterface", "North Spine Canteen"))
        self.CurrentResturantButton.setText(_translate("MainInterface", "Current Restaurant"))
        self.UserInputButton.setText(_translate("MainInterface", "Select Restaurant By Date"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainInterface = QtWidgets.QDialog()
    ui = Ui_MainInterface()
    ui.setupUi(MainInterface)
    MainInterface.show()
    sys.exit(app.exec_())
