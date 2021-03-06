from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

#Database import from NorthSpineCanteenDatabase.py
#with method GetFoodORPrice() to get the menu's item and price
from NorthSpineCanteenDataBase import GetFoodORPrice

import datetime

class Ui_UIDrinksStoreMenu(object):
    #Methods used for calculating waiting time DONE BY: AKSHITA
    def Calculate_button(self):
      try:
        inputValue = int(self.InputBox.text())

      except:
        self.OutputBox.setText("Error!")

      else:
         if inputValue<0:
                self.OutputBox.setText("Error!")
         else:
             estimatedTime = (inputValue) * 1
             Time_hr = estimatedTime//60
             Time_min = estimatedTime-Time_hr*60
             estimate = str(Time_hr) +"hrs" +str(Time_min) +"mins"
             self.OutputBox.setText(estimate)

    #Code for the interface and main program         
    def setupUi(self, UIDrinksStoreMenu):
        UIDrinksStoreMenu.setObjectName("UIDrinksStoreMenu")
        UIDrinksStoreMenu.resize(540, 555)
        UIDrinksStoreMenu.setStyleSheet("background-color: rgb(58, 45, 37)")
        
        self.NorthSpineCanteen = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(70, 40, 421, 41))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")

        self.DrinksLabel = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.DrinksLabel.setGeometry(QtCore.QRect(70, 70, 421, 41))
        self.DrinksLabel.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DrinksLabel.setFont(font)
        self.DrinksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DrinksLabel.setObjectName("Drinks Store's Menu")

        self.OperatingLabel = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.OperatingLabel.setGeometry(QtCore.QRect(120, 110, 311, 30))
        self.OperatingLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OperatingLabel.setFont(font)
        self.OperatingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OperatingLabel.setObjectName("Operating Hours")
        
        self.Item1 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Item1.setGeometry(QtCore.QRect(80, 190, 221, 41))
        self.Item1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item1.setFont(font)
        self.Item1.setFrameShape(QtWidgets.QFrame.Box)
        self.Item1.setAlignment(QtCore.Qt.AlignCenter)
        self.Item1.setObjectName("Item1")

        self.Item2 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Item2.setGeometry(QtCore.QRect(80, 240, 221, 41))
        self.Item2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item2.setFont(font)
        self.Item2.setAutoFillBackground(True)
        self.Item2.setFrameShape(QtWidgets.QFrame.Box)
        self.Item2.setAlignment(QtCore.Qt.AlignCenter)
        self.Item2.setObjectName("Item2")
        
        self.Item3 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Item3.setGeometry(QtCore.QRect(80, 290, 221, 41))
        self.Item3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item3.setFont(font)
        self.Item3.setFrameShape(QtWidgets.QFrame.Box)
        self.Item3.setAlignment(QtCore.Qt.AlignCenter)
        self.Item3.setObjectName("Item3")
        
        self.Item4 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Item4.setGeometry(QtCore.QRect(80, 340, 221, 41))
        self.Item4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item4.setFont(font)
        self.Item4.setFrameShape(QtWidgets.QFrame.Box)
        self.Item4.setAlignment(QtCore.Qt.AlignCenter)
        self.Item4.setObjectName("Item4")
        
        self.Price1 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Price1.setGeometry(QtCore.QRect(320, 190, 131, 41))
        self.Price1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price1.setFont(font)
        self.Price1.setFrameShape(QtWidgets.QFrame.Box)
        self.Price1.setAlignment(QtCore.Qt.AlignCenter)
        self.Price1.setObjectName("Price1")

        self.Price2 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Price2.setGeometry(QtCore.QRect(320, 240, 131, 41))
        self.Price2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price2.setFont(font)
        self.Price2.setAutoFillBackground(True)
        self.Price2.setFrameShape(QtWidgets.QFrame.Box)
        self.Price2.setAlignment(QtCore.Qt.AlignCenter)
        self.Price2.setObjectName("Price2")
        
        self.Price3 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Price3.setGeometry(QtCore.QRect(320, 290, 131, 41))
        self.Price3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price3.setFont(font)
        self.Price3.setFrameShape(QtWidgets.QFrame.Box)
        self.Price3.setAlignment(QtCore.Qt.AlignCenter)
        self.Price3.setObjectName("Price3")
        
        self.Price4 = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.Price4.setGeometry(QtCore.QRect(320, 340, 131, 41))
        self.Price4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price4.setFont(font)
        self.Price4.setFrameShape(QtWidgets.QFrame.Box)
        self.Price4.setAlignment(QtCore.Qt.AlignCenter)
        self.Price4.setObjectName("Price4")
        
        self.InputLabel = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.InputLabel.setGeometry(QtCore.QRect(90, 410, 221, 41))
        self.InputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.InputLabel.setFont(font)
        self.InputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InputLabel.setObjectName("InputLabel")
        
        self.InputBox = QtWidgets.QLineEdit(UIDrinksStoreMenu)
        self.InputBox.setGeometry(QtCore.QRect(300, 410, 90, 30))
        self.InputBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InputBox.setFont(font)
        self.InputBox.setObjectName("InputBox")

        self.OutputLabel = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.OutputLabel.setGeometry(QtCore.QRect(100, 440, 221, 61))
        self.OutputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputLabel.setObjectName("OutputLabel")

        self.OutputBox = QtWidgets.QLabel(UIDrinksStoreMenu)
        self.OutputBox.setGeometry(QtCore.QRect(300, 450, 90, 30))
        self.OutputBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OutputBox.setFont(font)
        self.OutputBox.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputBox.setObjectName("OutputBox")
        
        self.CalculateButton = QtWidgets.QPushButton(UIDrinksStoreMenu)
        self.CalculateButton.setGeometry(QtCore.QRect(400, 410, 90, 30))
        self.CalculateButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setObjectName("CalculateButton")
        self.CalculateButton.clicked.connect(self.Calculate_button)
        #Upon cliked, execute the calculate method
        
        self.BackButton = QtWidgets.QPushButton(UIDrinksStoreMenu)
        self.BackButton.setGeometry(QtCore.QRect(5, 505, 80, 40))
        self.BackButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(UIDrinksStoreMenu.close)
        #Upon clicked, close this interface
        
        self.retranslateUi(UIDrinksStoreMenu)
        QtCore.QMetaObject.connectSlotsByName(UIDrinksStoreMenu)

    def retranslateUi(self, UIDrinksStoreMenu):
        _translate = QtCore.QCoreApplication.translate
        UIDrinksStoreMenu.setWindowTitle(_translate("UIDrinksStoreMenu", "DrinksStore's Menu"))
        self.NorthSpineCanteen.setText(_translate("UIDrinksStoreMenu", "North Spine Canteen"))
        self.DrinksLabel.setText(_translate("UIDrinksStoreMenu", "Drinks Store's Menu"))
        self.OperatingLabel.setText(_translate("UIDrinksStoreMenu", "Operating Hours: 7AM-8PM (MON-FRI)"))

        #Displaying the menu's item using the methods imported from the database
        self.Item1.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",0)))
        self.Item2.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",1)))
        self.Item3.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",2)))
        self.Item4.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("NorthSpineCanteen","DrinksStore","AllDay",3)))
        #Displaying the item's price using the methods imported from the database
        self.Price1.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",0)))
        self.Price2.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",1)))
        self.Price3.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",2)))
        self.Price4.setText(_translate("UIDrinksStoreMenu", GetFoodORPrice("PNorthSpineCanteen","DrinksStore","AllDay",3)))
            
        self.InputLabel.setText(_translate("UIDrinksStoreMenu", "Input Customer in Queue:"))
        self.OutputLabel.setText(_translate("UIDrinksStoreMenu", "Estimated Waiting Time: "))
        self.CalculateButton.setText(_translate("UIDrinksStoreMenu", "Calculate"))
        self.BackButton.setText(_translate("UIDrinksStoreMenu", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIDrinksStoreMenu = QtWidgets.QDialog()
    ui = Ui_UIDrinksStoreMenu()
    ui.setupUi(UIDrinksStoreMenu)
    
    UIDrinksStoreMenu.show()
    sys.exit(app.exec_())
