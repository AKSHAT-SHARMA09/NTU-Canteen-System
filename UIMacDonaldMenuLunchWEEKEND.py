from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

#Database import from NorthSpineCanteenDatabase.py
#with method GetFoodORPrice() to get the menu's item and price
from NorthSpineCanteenDataBase import GetFoodORPrice

import datetime

class Ui_UIMacDonaldMenuLunchWEEKEND(object):
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
             estimatedTime = (inputValue) * 3
             Time_hr = estimatedTime//60
             Time_min = estimatedTime-Time_hr*60
             estimate = str(Time_hr) +"hrs" +str(Time_min) +"mins"
             self.OutputBox.setText(estimate)

   #Code for the interface and main program
    def setupUi(self, UIMacDonaldMenuLunchWEEKEND):
        UIMacDonaldMenuLunchWEEKEND.setObjectName("UIMacDonaldMenuLunchWEEKEND")
        UIMacDonaldMenuLunchWEEKEND.resize(540, 555)
        UIMacDonaldMenuLunchWEEKEND.setStyleSheet("background-color: rgb(58, 45, 37)")

        self.NorthSpineCanteen = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(70, 35, 421, 41))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")

        self.MCDLabel = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.MCDLabel.setGeometry(QtCore.QRect(70, 65, 421, 41))
        self.MCDLabel.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MCDLabel.setFont(font)
        self.MCDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MCDLabel.setObjectName("MacDonald's Menu")

        self.OperatingLabel = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.OperatingLabel.setGeometry(QtCore.QRect(120, 100, 330, 71))
        self.OperatingLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.OperatingLabel.setFont(font)
        self.OperatingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OperatingLabel.setObjectName("Operating Hours")

        self.Item1 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Item1.setGeometry(QtCore.QRect(80, 170, 221, 35))
        self.Item1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item1.setFont(font)
        self.Item1.setFrameShape(QtWidgets.QFrame.Box)
        self.Item1.setAlignment(QtCore.Qt.AlignCenter)
        self.Item1.setObjectName("Item1")

        self.Item2 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Item2.setGeometry(QtCore.QRect(80, 210, 221, 35))
        self.Item2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item2.setFont(font)
        self.Item2.setAutoFillBackground(True)
        self.Item2.setFrameShape(QtWidgets.QFrame.Box)
        self.Item2.setAlignment(QtCore.Qt.AlignCenter)
        self.Item2.setObjectName("Item2")

        self.Item3 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Item3.setGeometry(QtCore.QRect(80, 250, 221, 35))
        self.Item3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item3.setFont(font)
        self.Item3.setFrameShape(QtWidgets.QFrame.Box)
        self.Item3.setAlignment(QtCore.Qt.AlignCenter)
        self.Item3.setObjectName("Item3")

        self.Item4 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Item4.setGeometry(QtCore.QRect(80, 290, 221, 35))
        self.Item4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item4.setFont(font)
        self.Item4.setFrameShape(QtWidgets.QFrame.Box)
        self.Item4.setAlignment(QtCore.Qt.AlignCenter)
        self.Item4.setObjectName("Item4")

        self.Item5 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Item5.setGeometry(QtCore.QRect(80, 330, 221, 35))
        self.Item5.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item5.setFont(font)
        self.Item5.setFrameShape(QtWidgets.QFrame.Box)
        self.Item5.setAlignment(QtCore.Qt.AlignCenter)
        self.Item5.setObjectName("Item5")

        self.Item6 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Item6.setGeometry(QtCore.QRect(80, 370, 221, 35))
        self.Item6.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Item6.setFont(font)
        self.Item6.setFrameShape(QtWidgets.QFrame.Box)
        self.Item6.setAlignment(QtCore.Qt.AlignCenter)
        self.Item6.setObjectName("Item6")

        self.Price1 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Price1.setGeometry(QtCore.QRect(320, 170, 131, 35))
        self.Price1.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price1.setFont(font)
        self.Price1.setFrameShape(QtWidgets.QFrame.Box)
        self.Price1.setAlignment(QtCore.Qt.AlignCenter)
        self.Price1.setObjectName("Price1")

        self.Price2 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Price2.setGeometry(QtCore.QRect(320, 210, 131, 35))
        self.Price2.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price2.setFont(font)
        self.Price2.setAutoFillBackground(True)
        self.Price2.setFrameShape(QtWidgets.QFrame.Box)
        self.Price2.setAlignment(QtCore.Qt.AlignCenter)
        self.Price2.setObjectName("Price2")

        self.Price3 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Price3.setGeometry(QtCore.QRect(320, 250, 131, 35))
        self.Price3.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price3.setFont(font)
        self.Price3.setFrameShape(QtWidgets.QFrame.Box)
        self.Price3.setAlignment(QtCore.Qt.AlignCenter)
        self.Price3.setObjectName("Price3")

        self.Price4 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Price4.setGeometry(QtCore.QRect(320, 290, 131, 35))
        self.Price4.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price4.setFont(font)
        self.Price4.setFrameShape(QtWidgets.QFrame.Box)
        self.Price4.setAlignment(QtCore.Qt.AlignCenter)
        self.Price4.setObjectName("Price4")

        self.Price5 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Price5.setGeometry(QtCore.QRect(320, 330, 131, 35))
        self.Price5.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price5.setFont(font)
        self.Price5.setFrameShape(QtWidgets.QFrame.Box)
        self.Price5.setAlignment(QtCore.Qt.AlignCenter)
        self.Price5.setObjectName("Price5")

        self.Price6 = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.Price6.setGeometry(QtCore.QRect(320, 370, 131, 35))
        self.Price6.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Price6.setFont(font)
        self.Price6.setFrameShape(QtWidgets.QFrame.Box)
        self.Price6.setAlignment(QtCore.Qt.AlignCenter)
        self.Price6.setObjectName("Price5")

        self.InputLabel = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.InputLabel.setGeometry(QtCore.QRect(90, 410, 221, 41))
        self.InputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.InputLabel.setFont(font)
        self.InputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InputLabel.setObjectName("InputLabel")

        self.InputBox = QtWidgets.QLineEdit(UIMacDonaldMenuLunchWEEKEND)
        self.InputBox.setGeometry(QtCore.QRect(300, 410, 90, 30))
        self.InputBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.InputBox.setFont(font)
        self.InputBox.setObjectName("InputBox")

        self.OutputLabel = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.OutputLabel.setGeometry(QtCore.QRect(100, 440, 221, 61))
        self.OutputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputLabel.setObjectName("OutputLabel")

        self.OutputBox = QtWidgets.QLabel(UIMacDonaldMenuLunchWEEKEND)
        self.OutputBox.setGeometry(QtCore.QRect(300, 450, 90, 30))
        self.OutputBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.OutputBox.setFont(font)
        self.OutputBox.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputBox.setObjectName("OutputBox")

        self.CalculateButton = QtWidgets.QPushButton(UIMacDonaldMenuLunchWEEKEND)
        self.CalculateButton.setGeometry(QtCore.QRect(400, 410, 90, 30))
        self.CalculateButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setObjectName("CalculateButton")
        self.CalculateButton.clicked.connect(self.Calculate_button)
        #Upon cliked, execute the calculate method

        self.BackButton = QtWidgets.QPushButton(UIMacDonaldMenuLunchWEEKEND)
        self.BackButton.setGeometry(QtCore.QRect(5, 505, 80, 40))
        self.BackButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(UIMacDonaldMenuLunchWEEKEND.close)
        #Upon clicked, close this interface

        self.retranslateUi(UIMacDonaldMenuLunchWEEKEND)
        QtCore.QMetaObject.connectSlotsByName(UIMacDonaldMenuLunchWEEKEND)

    def retranslateUi(self, UIMacDonaldMenuLunchWEEKEND):
        _translate = QtCore.QCoreApplication.translate
        UIMacDonaldMenuLunchWEEKEND.setWindowTitle(_translate("UIMacDonaldMenuLunchWEEKEND", "MacDonald's Menu"))
        self.NorthSpineCanteen.setText(_translate("UIMacDonaldMenuLunchWEEKEND", "North Spine Canteen"))
        self.MCDLabel.setText(_translate("UIMacDonaldMenuLunchWEEKEND", "MacDonald's Lunch/Dinner Menu"))
        self.OperatingLabel.setText(_translate("UIMacDonaldMenuLunchNONPEAK", "Operating Hours: 6AM-11PM Daily \n Breakfast: 6AM-11AM  Lunch: 11AM-11PM \n Peak Hours: 11AM - 2PM \n Special Menu: SAT,SUN"))

        #Displaying the menu's item using the methods imported from the database
        self.Item1.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("NorthSpineCanteen", "MacDonald", "Lunch",0)))
        self.Item2.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("NorthSpineCanteen", "MacDonald", "Lunch",1)))
        self.Item3.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("NorthSpineCanteen", "MacDonald", "Lunch",2)))
        self.Item4.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("NorthSpineCanteen", "MacDonald", "Lunch",3)))
        self.Item5.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("NorthSpineCanteen", "MacDonald", "Lunch",4)))
        self.Item6.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("NorthSpineCanteen", "MacDonald", "Lunch",5)))
        #Displaying the item's price using the methods imported from the database
        self.Price1.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("PNorthSpineCanteen", "MacDonald", "Lunch",0)))
        self.Price2.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("PNorthSpineCanteen", "MacDonald", "Lunch",1)))
        self.Price3.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("PNorthSpineCanteen", "MacDonald", "Lunch",2)))
        self.Price4.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("PNorthSpineCanteen", "MacDonald", "Lunch",3)))
        self.Price5.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("PNorthSpineCanteen", "MacDonald", "Lunch",4)))
        self.Price6.setText(_translate("UIMacDonaldMenuLunchWEEKEND", GetFoodORPrice("PNorthSpineCanteen", "MacDonald", "Lunch",5)))

        self.InputLabel.setText(_translate("UIMacDonaldMenuLunchWEEKEND", "Input Customer in Queue:"))
        self.OutputLabel.setText(_translate("UIMacDonaldMenuLunchWEEKEND", "Estimated Waiting Time: "))
        self.CalculateButton.setText(_translate("UIMacDonaldMenuLunchWEEKEND", "Calculate"))
        self.BackButton.setText(_translate("UIMacDonaldMenuLunchWEEKEND", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIMacDonaldMenuLunchWEEKEND = QtWidgets.QDialog()
    ui = Ui_UIMacDonaldMenuLunchWEEKEND()
    ui.setupUi(UIMacDonaldMenuLunchWEEKEND)
    UIMacDonaldMenuLunchWEEKEND.show()
    sys.exit(app.exec_())
