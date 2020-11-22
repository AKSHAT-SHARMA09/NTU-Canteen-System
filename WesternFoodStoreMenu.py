from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

#Database import from NorthSpineCanteenDatabase.py
#with method GetFoodORPrice() to get the menu's item and price
from NorthSpineCanteenDataBase import GetFoodORPrice

import datetime

class Ui_WesternFoodStoreMenu(object):
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
             now = datetime.datetime.now()
             hour = int(now.strftime("%H"))
             day = str(now.strftime("%a"))
             if hour >= 11 and hour <= 13:
                 estimatedTime = (inputValue) * 5
             else:
                 estimatedTime = (inputValue) * 3
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
        if hour >= 10 and hour <= 18 and day != "Sat" and day != "Sun":
            self.NorthSpineCanteen.setText("North Spine Canteen")
            self.WesternFoodLabel.setText("Henry Western's Store Menu")
            self.InputBox.show()
            self.InputLabel.show()
            self.OutputLabel.show()
            self.Output.show()
            self.CalculateButton.show()
            self.Item1.show()
            self.Item2.show()
            self.Item3.show()
            self.Item4.show()
            self.Item5.show()
            self.Item6.show()
            self.Price1.show()
            self.Price2.show()
            self.Price3.show()
            self.Price4.show()
            self.Price5.show()
            self.Price6.show()
            #Display normal Menu
            if day == "Mon" or day == "Tue" or day == "Thu":
                #Displaying the menu's item using the methods imported from the database
                self.Item1.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",0))
                self.Item2.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",1))
                self.Item3.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",2))
                self.Item4.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",3))
                self.Item1.setGeometry(QtCore.QRect(80, 200, 221, 35))
                self.Item2.setGeometry(QtCore.QRect(80, 260, 221, 35))
                self.Item3.setGeometry(QtCore.QRect(80, 320, 221, 35))
                self.Item4.setGeometry(QtCore.QRect(80, 380, 221, 35))
                self.Item5.hide()
                self.Item6.hide()
                #Displaying the item's price using the methods imported from the database
                self.Price1.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",0))
                self.Price2.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",1))
                self.Price3.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",2))
                self.Price4.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",3))
                self.Price1.setGeometry(QtCore.QRect(320, 200, 131, 35))
                self.Price2.setGeometry(QtCore.QRect(320, 260, 131, 35))
                self.Price3.setGeometry(QtCore.QRect(320, 320, 131, 35))
                self.Price4.setGeometry(QtCore.QRect(320, 380, 131, 35))
                self.Price5.hide()
                self.Price6.hide()
            #Display Special Menu
            else:
                #Displaying the menu's item using the methods imported from the database
                self.Item1.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",0))
                self.Item2.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",1))
                self.Item3.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",2))
                self.Item4.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",3))
                self.Item5.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",4))
                self.Item6.setText(GetFoodORPrice("NorthSpineCanteen","WesternFoodStore","AllDay",5))
                self.Item1.setGeometry(QtCore.QRect(80, 180, 221, 35))
                self.Item2.setGeometry(QtCore.QRect(80, 220, 221, 35))
                self.Item3.setGeometry(QtCore.QRect(80, 260, 221, 35))
                self.Item4.setGeometry(QtCore.QRect(80, 300, 221, 35))
                self.Item5.setGeometry(QtCore.QRect(80, 340, 221, 35))
                self.Item6.setGeometry(QtCore.QRect(80, 380, 221, 35))
                #Displaying the item's price using the methods imported from the database
                self.Price1.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",0))
                self.Price2.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",1))
                self.Price3.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",2))
                self.Price4.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",3))
                self.Price5.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",4))
                self.Price6.setText(GetFoodORPrice("PNorthSpineCanteen","WesternFoodStore","AllDay",5))
                self.Price1.setGeometry(QtCore.QRect(320, 180, 131, 35))
                self.Price2.setGeometry(QtCore.QRect(320, 220, 131, 35))
                self.Price3.setGeometry(QtCore.QRect(320, 260, 131, 35))
                self.Price4.setGeometry(QtCore.QRect(320, 300, 131, 35))
                self.Price5.setGeometry(QtCore.QRect(320, 340, 131, 35))
                self.Price6.setGeometry(QtCore.QRect(320, 380, 131, 35))
        #Display Restaurant is close
        else:
            self.NorthSpineCanteen.setText("RESTAURANT IS CLOSED")
            self.WesternFoodLabel.setText("Henry Western's Menu")
            self.InputBox.hide()
            self.InputLabel.hide()
            self.OutputLabel.hide()
            self.Output.hide()
            self.CalculateButton.hide()
            self.Item1.hide()
            self.Item2.hide()
            self.Item3.hide()
            self.Item4.hide()
            self.Item5.hide()
            self.Item6.hide()
            self.Price1.hide()
            self.Price2.hide()
            self.Price3.hide()
            self.Price4.hide()
            self.Price5.hide()
            self.Price6.hide()

    #Code for the interface and main program
    def setupUi(self, WesternFoodStoreMenu):
        WesternFoodStoreMenu.setObjectName("WesternFoodStoreMenu")
        WesternFoodStoreMenu.resize(540, 555)
        WesternFoodStoreMenu.setStyleSheet("background-color: rgb(58, 45, 37)")

        self.DayDateTimeLabel = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.DayDateTimeLabel.setGeometry(QtCore.QRect(10, 10, 521, 61))
        self.DayDateTimeLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DayDateTimeLabel.setFont(font)
        self.DayDateTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DayDateTimeLabel.setObjectName("DayDateTimeLabel")

        self.NorthSpineCanteen = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(10, 50, 521, 71))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")

        self.WesternFoodLabel = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.WesternFoodLabel.setGeometry(QtCore.QRect(10, 95, 521, 20))
        self.WesternFoodLabel.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WesternFoodLabel.setFont(font)
        self.WesternFoodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WesternFoodLabel.setObjectName("WesternFoodStore's Menu")

        self.OperatingLabel = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.OperatingLabel.setGeometry(QtCore.QRect(110, 115, 330, 60))
        self.OperatingLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OperatingLabel.setFont(font)
        self.OperatingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OperatingLabel.setObjectName("Operating Hours")

        self.Item1 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Item1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item1.setFont(font)
        self.Item1.setFrameShape(QtWidgets.QFrame.Box)
        self.Item1.setAlignment(QtCore.Qt.AlignCenter)
        self.Item1.setObjectName("Item1")

        self.Item2 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Item2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(7)
        self.Item2.setFont(font)
        self.Item2.setAutoFillBackground(True)
        self.Item2.setFrameShape(QtWidgets.QFrame.Box)
        self.Item2.setAlignment(QtCore.Qt.AlignCenter)
        self.Item2.setObjectName("Item2")

        self.Item3 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Item3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item3.setFont(font)
        self.Item3.setFrameShape(QtWidgets.QFrame.Box)
        self.Item3.setAlignment(QtCore.Qt.AlignCenter)
        self.Item3.setObjectName("Item3")

        self.Item4 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Item4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item4.setFont(font)
        self.Item4.setFrameShape(QtWidgets.QFrame.Box)
        self.Item4.setAlignment(QtCore.Qt.AlignCenter)
        self.Item4.setObjectName("Item4")

        self.Item5 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Item5.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item5.setFont(font)
        self.Item5.setFrameShape(QtWidgets.QFrame.Box)
        self.Item5.setAlignment(QtCore.Qt.AlignCenter)
        self.Item5.setObjectName("Item5")

        self.Item6 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Item6.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item6.setFont(font)
        self.Item6.setFrameShape(QtWidgets.QFrame.Box)
        self.Item6.setAlignment(QtCore.Qt.AlignCenter)
        self.Item6.setObjectName("Item6")

        self.Price1 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Price1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price1.setFont(font)
        self.Price1.setFrameShape(QtWidgets.QFrame.Box)
        self.Price1.setAlignment(QtCore.Qt.AlignCenter)
        self.Price1.setObjectName("Price1")

        self.Price2 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Price2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price2.setFont(font)
        self.Price2.setAutoFillBackground(True)
        self.Price2.setFrameShape(QtWidgets.QFrame.Box)
        self.Price2.setAlignment(QtCore.Qt.AlignCenter)
        self.Price2.setObjectName("Price2")

        self.Price3 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Price3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price3.setFont(font)
        self.Price3.setFrameShape(QtWidgets.QFrame.Box)
        self.Price3.setAlignment(QtCore.Qt.AlignCenter)
        self.Price3.setObjectName("Price3")

        self.Price4 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Price4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price4.setFont(font)
        self.Price4.setFrameShape(QtWidgets.QFrame.Box)
        self.Price4.setAlignment(QtCore.Qt.AlignCenter)
        self.Price4.setObjectName("Price4")

        self.Price5 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Price5.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price5.setFont(font)
        self.Price5.setFrameShape(QtWidgets.QFrame.Box)
        self.Price5.setAlignment(QtCore.Qt.AlignCenter)
        self.Price5.setObjectName("Price5")

        self.Price6 = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Price6.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price6.setFont(font)
        self.Price6.setFrameShape(QtWidgets.QFrame.Box)
        self.Price6.setAlignment(QtCore.Qt.AlignCenter)
        self.Price6.setObjectName("Price6")

        self.InputLabel = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.InputLabel.setGeometry(QtCore.QRect(90, 430, 221, 41))
        self.InputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.InputLabel.setFont(font)
        self.InputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InputLabel.setObjectName("InputLabel")

        self.InputBox = QtWidgets.QLineEdit(WesternFoodStoreMenu)
        self.InputBox.setGeometry(QtCore.QRect(300, 430, 90, 30))
        self.InputBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InputBox.setFont(font)
        self.InputBox.setObjectName("InputBox")

        self.OutputLabel = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.OutputLabel.setGeometry(QtCore.QRect(100, 460, 221, 61))
        self.OutputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputLabel.setObjectName("OutputLabel")

        self.Output = QtWidgets.QLabel(WesternFoodStoreMenu)
        self.Output.setGeometry(QtCore.QRect(300, 470, 90, 30))
        self.Output.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Output.setFont(font)
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setObjectName("Output")

        self.CalculateButton = QtWidgets.QPushButton(WesternFoodStoreMenu)
        self.CalculateButton.setGeometry(QtCore.QRect(430, 456, 93, 28))
        self.CalculateButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setObjectName("CalculateButton")
        self.CalculateButton.clicked.connect(self.Calculate_button)
        #Upon cliked, execute the calculate method

        self.BackButton = QtWidgets.QPushButton(WesternFoodStoreMenu)
        self.BackButton.setGeometry(QtCore.QRect(5, 505, 80, 40))
        self.BackButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(WesternFoodStoreMenu.close)
        #Upon clicked, close this interface

        timer = QTimer(WesternFoodStoreMenu)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        #Timer used to update and execute the time methood every 1s

        self.retranslateUi(WesternFoodStoreMenu)
        QtCore.QMetaObject.connectSlotsByName(WesternFoodStoreMenu)

    def retranslateUi(self, WesternFoodStoreMenu):
        _translate = QtCore.QCoreApplication.translate
        WesternFoodStoreMenu.setWindowTitle(_translate("WesternFoodStoreMenu", "WesternFoodStore's Menu"))
        self.NorthSpineCanteen.setText(_translate("WesternFoodStoreMenu", "North Spine Canteen"))
        self.WesternFoodLabel.setText(_translate("WesternFoodStoreMenu", "Henry Western's Menu"))
        self.OperatingLabel.setText(_translate("WesternFoodStoreMenu", "Operating Hours: 10AM-7PM (MON-FRI) \n Peak Hours: 11AM - 2PM \n (Special Menu: WED,FRI)"))

        self.InputLabel.setText(_translate("WesternFoodStoreMenu", "Input Customer in Queue:"))
        self.OutputLabel.setText(_translate("WesternFoodStoreMenu", "Estimated Waiting Time:"))
        self.CalculateButton.setText(_translate("WesternFoodStoreMenu", "Calculate"))
        self.BackButton.setText(_translate("WesternFoodStoreMenu", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WesternFoodStoreMenu = QtWidgets.QDialog()
    ui = Ui_WesternFoodStoreMenu()
    ui.setupUi(WesternFoodStoreMenu)
    WesternFoodStoreMenu.show()
    sys.exit(app.exec_())
