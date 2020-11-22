from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

#Database import from NorthSpineCanteenDatabase.py
#with method GetFoodORPrice() to get the menu's item and price
from NorthSpineCanteenDataBase import GetFoodORPrice

import datetime

class Ui_DrinksStoreMenu(object):
    #Methods used for calculating waiting time DONE BY: AKSHITA
    def Calculate_button(self):
      try:
        inputValue = int(self.InputBox.text())

      except:
        self.Output.setText("Error!")

      else:
         if inputValue<0:
                self.Output.setText("Error!")
         else:
             estimatedTime = (inputValue) * 1
             Time_hr = estimatedTime//60
             Time_min = estimatedTime-Time_hr*60
             estimate = str(Time_hr) +"hrs" +str(Time_min) +"mins"
             self.Output.setText(estimate)

    #Methods used to display current system time, date and day
    #By comparing the day and hour, display menu when the resturant is open DONE BY: AIK YU CHEN
    def showTime(self):
        now = datetime.datetime.now()
        hour = int(now.strftime("%H"))
        day = now.strftime("%a")
        self.DayDateTimeLabel.setText(now.strftime("%a" + " " + "%d-%h-%Y" + " " + "%H:%M:%S"))

        #Display Menu store is open
        if hour >= 7 and hour <= 19 and day != "Sat" and day != "Sun" :
            self.NorthSpineCanteen.setText("North Spine Canteen")
            self.InputBox.show()
            self.InputLabel.show()
            self.OutputLabel.show()
            self.Output.show()
            self.CalculateButton.show()
            #Displaying the menu's item using the methods imported from the database
            self.Item1.setText(GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",0))
            self.Item2.setText(GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",1))
            self.Item3.setText(GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",2))
            self.Item4.setText(GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",3))
            #Displaying the item's price using the methods imported from the database
            self.Price1.setText(GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",0))
            self.Price2.setText(GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",1))
            self.Price3.setText(GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",2))
            self.Price4.setText(GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",3))
        #Display Restaurant is close
        else:
            self.NorthSpineCanteen.setText("RESTURANT IS CLOSED")
            self.InputBox.hide()
            self.InputLabel.hide()
            self.OutputLabel.hide()
            self.Output.hide()
            self.CalculateButton.hide()
            self.Item1.hide()
            self.Item2.hide()
            self.Item3.hide()
            self.Item4.hide()
            self.Price1.hide()
            self.Price2.hide()
            self.Price3.hide()
            self.Price4.hide()
            
    #Code for the interface and main program
    def setupUi(self, DrinksStoreMenu):
        DrinksStoreMenu.setObjectName("DrinksStoreMenu")
        DrinksStoreMenu.resize(540, 555)
        DrinksStoreMenu.setStyleSheet("background-color: rgb(58, 45, 37)")
        
        self.DayDateTimeLabel = QtWidgets.QLabel(DrinksStoreMenu)
        self.DayDateTimeLabel.setGeometry(QtCore.QRect(10, 10, 521, 61))
        self.DayDateTimeLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DayDateTimeLabel.setFont(font)
        self.DayDateTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DayDateTimeLabel.setObjectName("DayDateTimeLabel")
        
        self.NorthSpineCanteen = QtWidgets.QLabel(DrinksStoreMenu)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(10, 50, 521, 71))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")

        self.DrinksLabel = QtWidgets.QLabel(DrinksStoreMenu)
        self.DrinksLabel.setGeometry(QtCore.QRect(10, 95, 521, 20))
        self.DrinksLabel.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DrinksLabel.setFont(font)
        self.DrinksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DrinksLabel.setObjectName("Drinks Store's Menu")

        self.OperatingLabel = QtWidgets.QLabel(DrinksStoreMenu)
        self.OperatingLabel.setGeometry(QtCore.QRect(110, 115, 330, 60))
        self.OperatingLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OperatingLabel.setFont(font)
        self.OperatingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OperatingLabel.setObjectName("Operating Hours")
        
        self.Item1 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Item1.setGeometry(QtCore.QRect(80, 190, 150, 50))
        self.Item1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item1.setFont(font)
        self.Item1.setFrameShape(QtWidgets.QFrame.Box)
        self.Item1.setAlignment(QtCore.Qt.AlignCenter)
        self.Item1.setObjectName("Item1")

        self.Item2 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Item2.setGeometry(QtCore.QRect(80, 250, 150, 50))
        self.Item2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item2.setFont(font)
        self.Item2.setAutoFillBackground(True)
        self.Item2.setFrameShape(QtWidgets.QFrame.Box)
        self.Item2.setAlignment(QtCore.Qt.AlignCenter)
        self.Item2.setObjectName("Item2")
        
        self.Item3 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Item3.setGeometry(QtCore.QRect(80, 310, 150, 50))
        self.Item3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item3.setFont(font)
        self.Item3.setFrameShape(QtWidgets.QFrame.Box)
        self.Item3.setAlignment(QtCore.Qt.AlignCenter)
        self.Item3.setObjectName("Item3")
        
        self.Item4 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Item4.setGeometry(QtCore.QRect(80, 370, 150, 50))
        self.Item4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item4.setFont(font)
        self.Item4.setFrameShape(QtWidgets.QFrame.Box)
        self.Item4.setAlignment(QtCore.Qt.AlignCenter)
        self.Item4.setObjectName("Item4")
        
        self.Price1 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Price1.setGeometry(QtCore.QRect(300, 190, 150, 50))
        self.Price1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price1.setFont(font)
        self.Price1.setFrameShape(QtWidgets.QFrame.Box)
        self.Price1.setAlignment(QtCore.Qt.AlignCenter)
        self.Price1.setObjectName("Price1")

        self.Price2 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Price2.setGeometry(QtCore.QRect(300, 250, 150, 50))
        self.Price2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price2.setFont(font)
        self.Price2.setAutoFillBackground(True)
        self.Price2.setFrameShape(QtWidgets.QFrame.Box)
        self.Price2.setAlignment(QtCore.Qt.AlignCenter)
        self.Price2.setObjectName("Price2")
        
        self.Price3 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Price3.setGeometry(QtCore.QRect(300, 310, 150, 50))
        self.Price3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price3.setFont(font)
        self.Price3.setFrameShape(QtWidgets.QFrame.Box)
        self.Price3.setAlignment(QtCore.Qt.AlignCenter)
        self.Price3.setObjectName("Price3")
        
        self.Price4 = QtWidgets.QLabel(DrinksStoreMenu)
        self.Price4.setGeometry(QtCore.QRect(300, 370, 150, 50))
        self.Price4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price4.setFont(font)
        self.Price4.setFrameShape(QtWidgets.QFrame.Box)
        self.Price4.setAlignment(QtCore.Qt.AlignCenter)
        self.Price4.setObjectName("Price4")
        
        self.InputLabel = QtWidgets.QLabel(DrinksStoreMenu)
        self.InputLabel.setGeometry(QtCore.QRect(90, 430, 221, 41))
        self.InputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.InputLabel.setFont(font)
        self.InputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InputLabel.setObjectName("InputLabel")
        
        self.InputBox = QtWidgets.QLineEdit(DrinksStoreMenu)
        self.InputBox.setGeometry(QtCore.QRect(300, 430, 90, 30))
        self.InputBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InputBox.setFont(font)
        self.InputBox.setObjectName("InputBox")

        self.OutputLabel = QtWidgets.QLabel(DrinksStoreMenu)
        self.OutputLabel.setGeometry(QtCore.QRect(100, 460, 221, 61))
        self.OutputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputLabel.setObjectName("OutputLabel")

        self.Output = QtWidgets.QLabel(DrinksStoreMenu)
        self.Output.setGeometry(QtCore.QRect(300, 470, 90, 30))
        self.Output.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Output.setFont(font)
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setObjectName("Output")
        
        self.CalculateButton = QtWidgets.QPushButton(DrinksStoreMenu)
        self.CalculateButton.setGeometry(QtCore.QRect(400, 430, 90, 30))
        self.CalculateButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setObjectName("CalculateButton")
        self.CalculateButton.clicked.connect(self.Calculate_button)
        #Upon cliked, execute the calculate method
        
        self.BackButton = QtWidgets.QPushButton(DrinksStoreMenu)
        self.BackButton.setGeometry(QtCore.QRect(5, 505, 80, 40))
        self.BackButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(DrinksStoreMenu.close)
        #Upon clicked, close this interface

        timer = QTimer(DrinksStoreMenu)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        #Timer used to update and execute the time methood every 1s
        
        self.retranslateUi(DrinksStoreMenu)
        QtCore.QMetaObject.connectSlotsByName(DrinksStoreMenu)

    def retranslateUi(self, DrinksStoreMenu):
        _translate = QtCore.QCoreApplication.translate
        DrinksStoreMenu.setWindowTitle(_translate("DrinksStoreMenu", "DrinksStore's Menu"))
        self.NorthSpineCanteen.setText(_translate("DrinksStoreMenu", "North Spine Canteen"))
        self.DrinksLabel.setText(_translate("DrinksStoreMenu", "Drinks Store's Menu"))
        self.OperatingLabel.setText(_translate("DrinksStoreMenu", "Operating Hours: 7AM-8PM (MON-FRI)"))
            
        self.InputLabel.setText(_translate("DrinksStoreMenu", "Input Customer in Queue:"))
        self.OutputLabel.setText(_translate("DrinksStoreMenu", "Estimated Waiting Time:"))
        self.CalculateButton.setText(_translate("DrinksStoreMenu", "Calculate"))
        self.BackButton.setText(_translate("DrinksStoreMenu", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DrinksStoreMenu = QtWidgets.QDialog()
    ui = Ui_DrinksStoreMenu()
    ui.setupUi(DrinksStoreMenu)
    
    DrinksStoreMenu.show()
    sys.exit(app.exec_())
