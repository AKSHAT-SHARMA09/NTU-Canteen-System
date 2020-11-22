from PyQt5 import QtCore, QtGui, QtWidgets

#Import the interface file to display for each store's Menu
from UIMacDonaldMenuBreakfast import Ui_UIMacDonaldMenuBreakfast
from UIMacDonaldMenuLunchNONPEAK import Ui_UIMacDonaldMenuLunchNONPEAK
from UIMacDonaldMenuLunchPEAK import Ui_UIMacDonaldMenuLunchPEAK
from UIMacDonaldMenuLunchWEEKEND import Ui_UIMacDonaldMenuLunchWEEKEND

from UISubwayMenuBreakfast import Ui_UISubwayMenuBreakfast
from UISubwayMenuLunchNONPEAK import Ui_UISubwayMenuLunchNONPEAK
from UISubwayMenuLunchPEAK import Ui_UISubwayMenuLunchPEAK
from UISubwayMenuLunchWEEKEND import Ui_UISubwayMenuLunchWEEKEND

from UIChickenRiceStoreMenuNONPEAK import Ui_UIChickenRiceStoreMenuNONPEAK
from UIChickenRiceStoreMenuPEAK import Ui_UIChickenRiceStoreMenuPEAK
from UIChickenRiceStoreMenuSPECIAL import Ui_UIChickenRiceStoreMenuSPECIAL

from UIWesternFoodStoreMenuNONPEAK import Ui_UIWesternFoodStoreMenuNONPEAK
from UIWesternFoodStoreMenuPEAK import Ui_UIWesternFoodStoreMenuPEAK
from UIWesternFoodStoreMenuSPECIAL import Ui_UIWesternFoodStoreMenuSPECIAL

from UIDrinksStoreMenu import Ui_UIDrinksStoreMenu

import datetime

class Ui_UserInputSelection(object):
    #Method to check for any new input and display operating restaurant according to user's input DONE BY: AIK YU CHEN
    def DateTimeInput(self):
        Date = self.DateInput.date()
        Day = Date.toString("ddd")
        Time = self.TimeInput.time()
        HourStr = Time.toString("hh")
        Hour = int(HourStr)

        if Hour < 9 or Hour > 19 or Day == "Sat" or Day == "Sun":
            self.ChickenRiceStoreButton.hide()
        else:
            self.ChickenRiceStoreButton.show()

        if Hour < 10 or Hour > 18 or Day == "Sat" or Day == "Sun":
            self.WesternFoodStoreButton.hide()
        else:
            self.WesternFoodStoreButton.show()

        if Hour < 7 or Hour > 19 or Day == "Sat" or Day == "Sun":
            self.DrinksStoreButton.hide()
        else:
            self.DrinksStoreButton.show()

        if Hour < 6 or Hour > 22:
            self.MacDonaldButton.hide()
        else:
            self.MacDonaldButton.show()

        if Hour < 8 or Hour > 22:
            self.SubwayButton.hide()
        else:
            self.SubwayButton.show()

    #Methods used to check to display respective menu's interface DONE BY: AIK YU CHEN
    def DisplayMacMenu(self):
        Date = self.DateInput.date()
        Day = Date.toString("ddd")
        Time = self.TimeInput.time()
        HourStr = Time.toString("hh")
        Hour = int(HourStr)
        if (Hour >=8 and Hour <= 10) and (Day == "Sat" or Day == "Sun"):
            self.MacDonaldBreakfast_button()
        elif Day == "Sat" or Day == "Sun":
            self.MacDonaldWEEKEND_button()
        elif Hour >= 8 and Hour <= 10:
            self.MacDonaldBreakfast_button()
        elif Hour >=11 and Hour <= 13 and Day != "Sat" and Day != "Sun" :
            self.MacDonaldLunchPEAK_button()
        elif Day != "Sat" and Day != "Sun" and Hour >= 14 and Hour <=22:
            self.MacDonaldLunchNONPEAK_button()
            
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def MacDonaldBreakfast_button(self):
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_UIMacDonaldMenuBreakfast()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def MacDonaldLunchNONPEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_UIMacDonaldMenuLunchNONPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def MacDonaldLunchPEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_UIMacDonaldMenuLunchPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()
        
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def MacDonaldWEEKEND_button(self):
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_UIMacDonaldMenuLunchWEEKEND()
        self.ui.setupUi(self.window)
        self.window.exec_()
        
    #Methods used to check to display respective menu's interface DONE BY: AIK YU CHEN
    def DisplaySubMenu(self):
        Date = self.DateInput.date()
        Day = Date.toString("ddd")
        Time = self.TimeInput.time()
        HourStr = Time.toString("hh")
        Hour = int(HourStr)
        if (Hour >=8 and Hour <= 10) and (Day == "Sat" or Day == "Sun") :
             self.SubwayBreakfast_button()
        elif Day == "Sat" or Day == "Sun":
            self.SubwayLunchWEEKEND_button()
        elif Hour >= 8 and Hour <= 10:
            self.SubwayBreakfast_button()
        elif Hour >=11 and Hour <= 13 and Day != "Sat" and Day != "Sun" :
            self.SubwayLunchPEAK_button()
        elif Day != "Sat" and Day != "Sun" and Hour >= 14 and Hour <=22:
            self.SubwayLunchNONPEAK_button()
            
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def SubwayBreakfast_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UISubwayMenuBreakfast()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def SubwayLunchNONPEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UISubwayMenuLunchNONPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()
        
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def SubwayLunchPEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UISubwayMenuLunchNONPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()
        
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def SubwayLunchWEEKEND_button(self):
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_UISubwayMenuLunchWEEKEND()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to check to display respective menu's interface DONE BY: AKSHAT
    def DisplayChickenRiceMenu(self):
        Date = self.DateInput.date()
        Day = Date.toString("ddd")
        Time = self.TimeInput.time()
        HourStr = Time.toString("hh")
        Hour = int(HourStr)
        if  Day == "Tue" or Day == "Thu":
            self.ChickenRiceStoreSPECIAL_button()
        elif (Hour >= 11 and Hour <= 13) and (Day == "Mon" or Day == "Wed" or Day == "Fri"):
            self.ChickenRiceStorePEAK_button()
        elif (Hour >= 14 and Hour <= 19) and  (Day == "Mon" or Day == "Wed" or Day == "Fri"):
            self.ChickenRiceStoreNONPEAK_button()
        elif Hour == 10:
            self.ChickenRiceStoreNONPEAK_button()
             
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def ChickenRiceStoreNONPEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIChickenRiceStoreMenuNONPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def ChickenRiceStorePEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIChickenRiceStoreMenuPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def ChickenRiceStoreSPECIAL_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIChickenRiceStoreMenuSPECIAL()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to check to display respective menu's interface DONE BY: AKSHAT
    def DisplayWesternFoodMenu(self):
        Date = self.DateInput.date()
        Day = Date.toString("ddd")
        Time = self.TimeInput.time()
        HourStr = Time.toString("hh")
        Hour = int(HourStr)
        if  Day == "Wed" or Day == "Fri":
            self.WesternFoodStoreMenuSPECIAL_button()
        elif (Hour >= 11 and Hour <= 13) and (Day == "Mon" or Day == "Tue" or Day == "Thu"):
            self.WesternFoodStorePEAK_button()
        elif (Hour >= 14 and Hour <= 19) and  (Day == "Mon" or Day == "Tue" or Day == "Thu"):
            self.WesternFoodStoreNONPEAK_button()
        elif Hour == 10:
            self.WesternFoodStoreNONPEAK_button()
            
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def WesternFoodStoreNONPEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIWesternFoodStoreMenuNONPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()
        
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def WesternFoodStorePEAK_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIWesternFoodStoreMenuNONPEAK()
        self.ui.setupUi(self.window)
        self.window.exec_()
        
    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def WesternFoodStoreMenuSPECIAL_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIWesternFoodStoreMenuSPECIAL()
        self.ui.setupUi(self.window)
        self.window.exec_()

    #Methods used to open the store's menu interface DONE BY: AKSHAT
    def DrinksStore_button(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_UIDrinksStoreMenu()
        self.ui.setupUi(self.window)
        self.window.exec_()    

    #Code for the interface and main program
    def setupUi(self, UserInputSelection):
        UserInputSelection.setObjectName("UserInputSelection")
        UserInputSelection.resize(540, 555)
        UserInputSelection.setStyleSheet("background-color: rgb(58, 45, 37)")

        self.DateInput = QtWidgets.QDateEdit(UserInputSelection)
        self.DateInput.setGeometry(QtCore.QRect(114, 100, 160, 35))
        self.DateInput.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DateInput.setFont(font)
        self.DateInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateInput.setCalendarPopup(True)
        self.DateInput.setObjectName("DateInput")

        self.TimeInput = QtWidgets.QTimeEdit(UserInputSelection)
        self.TimeInput.setGeometry(QtCore.QRect(360, 100, 160, 35))
        self.TimeInput.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TimeInput.setFont(font)
        self.TimeInput.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(10, 0, 0)))
        self.TimeInput.setObjectName("TimeInput")

        self.DateInputLabel = QtWidgets.QLabel(UserInputSelection)
        self.DateInputLabel.setGeometry(QtCore.QRect(25, 100, 75, 40))
        self.DateInputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.DateInputLabel.setFont(font)
        self.DateInputLabel.setObjectName("DateInputLabel")

        self.TimeInputLabel = QtWidgets.QLabel(UserInputSelection)
        self.TimeInputLabel.setGeometry(QtCore.QRect(280, 100, 75, 40))
        self.TimeInputLabel.setStyleSheet("color: rgb(227, 178, 111)")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(50)
        self.TimeInputLabel.setFont(font)
        self.TimeInputLabel.setObjectName("TimeInputLabel")

        self.NorthSpineCanteen = QtWidgets.QLabel(UserInputSelection)
        self.NorthSpineCanteen.setGeometry(QtCore.QRect(10, 10, 520, 50))
        self.NorthSpineCanteen.setStyleSheet("color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NorthSpineCanteen.setFont(font)
        self.NorthSpineCanteen.setAlignment(QtCore.Qt.AlignCenter)
        self.NorthSpineCanteen.setObjectName("NorthSpineCanteen")

        self.MacDonaldButton = QtWidgets.QPushButton(UserInputSelection)
        self.MacDonaldButton.setGeometry(QtCore.QRect(200, 180, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MacDonaldButton.setFont(font)
        self.MacDonaldButton.setObjectName("MacDonaldButton")
        self.MacDonaldButton.setIcon(QtGui.QIcon("Macdonald.png"))
        self.MacDonaldButton.setIconSize(QtCore.QSize(50,50))
        self.MacDonaldButton.setStyleSheet("background-color: red;")
        self.MacDonaldButton.clicked.connect(self.DisplayMacMenu)
        #Upon clicked, execute method to check which restaurant's menu interface to display

        self.SubwayButton = QtWidgets.QPushButton(UserInputSelection)
        self.SubwayButton.setGeometry(QtCore.QRect(200, 250, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SubwayButton.setFont(font)
        self.SubwayButton.setObjectName("SubwayButton")
        self.SubwayButton.setIcon(QtGui.QIcon("subway.png"))
        self.SubwayButton.setIconSize(QtCore.QSize(100,100))
        self.SubwayButton.setStyleSheet("background-color: green;")
        self.SubwayButton.clicked.connect(self.DisplaySubMenu)
        #Upon clicked, execute method to check which restaurant's menu interface to display

        self.ChickenRiceStoreButton = QtWidgets.QPushButton(UserInputSelection)
        self.ChickenRiceStoreButton.setGeometry(QtCore.QRect(200, 320, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ChickenRiceStoreButton.setFont(font)
        self.ChickenRiceStoreButton.setIcon(QtGui.QIcon("ChickenRiceStore.png"))
        self.ChickenRiceStoreButton.setIconSize(QtCore.QSize(140,250))
        self.ChickenRiceStoreButton.setStyleSheet("background-color: black;")
        self.ChickenRiceStoreButton.clicked.connect(self.DisplayChickenRiceMenu)
        #Upon clicked, execute method to check which restaurant's menu interface to display

        self.WesternFoodStoreButton = QtWidgets.QPushButton(UserInputSelection)
        self.WesternFoodStoreButton.setGeometry(QtCore.QRect(200, 390, 150, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WesternFoodStoreButton.setFont(font)
        self.WesternFoodStoreButton.setObjectName("WesternFoodStoreButton")
        self.WesternFoodStoreButton.setIcon(QtGui.QIcon("WesternFoodStore.png"))
        self.WesternFoodStoreButton.setIconSize(QtCore.QSize(160,160))
        self.WesternFoodStoreButton.setStyleSheet("background-color: black;")
        self.WesternFoodStoreButton.clicked.connect(self.DisplayWesternFoodMenu)
        #Upon clicked, execute method to check which restaurant's menu interface to display

        self.DrinksStoreButton = QtWidgets.QPushButton(UserInputSelection)
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

        self.BackButton = QtWidgets.QPushButton(UserInputSelection)
        self.BackButton.setGeometry(QtCore.QRect(5, 505, 80, 40))
        self.BackButton.setStyleSheet("background-color: rgb(236, 112, 42)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(UserInputSelection.close)
        #Upon clicked, close this interface

        self.retranslateUi(UserInputSelection)
        QtCore.QMetaObject.connectSlotsByName(UserInputSelection)

    def retranslateUi(self, UserInputSelection):
        _translate = QtCore.QCoreApplication.translate
        UserInputSelection.setWindowTitle(_translate("UserInputSelection", "NorthSpineCanteen"))
        self.NorthSpineCanteen.setText(_translate("UserInputSelection", "North Spine Canteen"))
        self.BackButton.setText(_translate("UserInputSelection", "Back"))
        self.DateInput.setDisplayFormat(_translate("UserInputSelection", "d/M/yyyy ddd"))
        self.TimeInput.setDisplayFormat(_translate("UserInputSelection", "hh:mm"))
        self.DateInputLabel.setText(_translate("UserInputSelection", "Select Date"))
        self.TimeInputLabel.setText(_translate("UserInputSelection", "Select Time"))

        self.DateInput.dateChanged.connect(self.DateTimeInput)
        self.TimeInput.timeChanged.connect(self.DateTimeInput)
        self.DateTimeInput()
        #Check and update everytime Date or Time Input is changed through the method
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserInputSelection = QtWidgets.QDialog()
    ui = Ui_UserInputSelection()
    ui.setupUi(UserInputSelection)
    UserInputSelection.show()
    sys.exit(app.exec_())
