##List for Items on Menu and Price, share the same corrosponding index##
#DONE BY: AIK YU CHEN
MacDonaldBF = ["Sausage McMuffin", "Chicken McMuffin", "Hotcakes", "Breakfast Wrap"]
PMacDonaldBF = ["$2.50", "$2.50", "$4.50", "$3.50"]
MacDonaldL = ["McChicken", "McSpicy", "Filet-O-Fish", "Cheeseburger", "Double McSpicy Feast", "Double CheeseBurger Feast"]
PMacDonaldL = ["$2.00", "$4.50", "$4.50", "$2.00","$11.65","$8.90"]

SubwayBF = ["Chicken Ham Flatbread", "Chicken Sausage Flatbread", "Egg Flatbread", "Add-on Egg"]
PSubwayBF = ["$5.50", "$5.50", "$3.00", "$1.00"]
SubwayL= ["Chicken Teriyaki Sub", "Egg Mayo Sub", "Cold Cut Trio Sub", "Subway Club Sub", " Chatpata Chickpea Sub", "Roast Beef Sub"]
PSubwayL= ["$5.50", "$4.50", "$6.50", "$6.50", "$ 5.70","$7.50"]

ChickenRiceStore = ["Steamed Chicken Rice", "Roasted Chicken Rice", "Braised Egg", "Braised Tofu", "Shredded Chicken Congee", "Thai Sauce Chicken Rice"]
PChickenRiceStore = ["$3.00", "$3.00", "$0.70", "$1.00","$4.30", "$4.70"]

WesternFoodStore = ["Chicken Chop", "Lamb Chop", "Fish and Chips", "Spaghetti w Meatball", "Cheesy Wedges", "Hawaiian Grill Fish"]
PWesternFoodStore = ["$6.00", "$6.50", "$7.00", "$5.50", "$3.50", "$4.70"]

DrinksStore = ["Ice Kopi", "Ice Tea", "Orange Juice", "Coke"]
PDrinksStore = ["$1.20", "$1.20", "$1.50", "$1.70"]

##DataBase for Items Price on Menu##
NorthSpineCanteen ={("MacDonald","Breakfast"):MacDonaldBF, ("MacDonald","Lunch"):MacDonaldL,
                    ("Subway","Breakfast"):SubwayBF, ("Subway","Lunch"):SubwayL,
                    ("ChickenRiceStore","AllDay"):ChickenRiceStore,
                    ("WesternFoodStore","AllDay"):WesternFoodStore,
                    ("DrinksStore","AllDay"):DrinksStore}

PNorthSpineCanteen ={("MacDonald","Breakfast"):PMacDonaldBF, ("MacDonald","Lunch"):PMacDonaldL,
                     ("Subway","Breakfast"):PSubwayBF, ("Subway","Lunch"):PSubwayL,
                     ("ChickenRiceStore","AllDay"):PChickenRiceStore,
                     ("WesternFoodStore","AllDay"):PWesternFoodStore,
                     ("DrinksStore","AllDay"):PDrinksStore}
    

#Database of North Spine Canteen, includes different store's menu and price
#Methods to get the items and price on each menu
#Input of dataBase to select which database NorthSpineCanteen > Items, PNorthSpineCanteen > Price
#Input of store to select store, eg. MacDonald/Subway etc..
#Input of meal to choose meal, eg. Breakfast/Lunch/AllDay
#Input of choice to select index on the list
#DONE BY: Aik Yu Chen
def GetFoodORPrice(dataBase, store, meal, choice):
    if dataBase == "NorthSpineCanteen":
        return NorthSpineCanteen[(store,meal)][choice]
    if dataBase == "PNorthSpineCanteen":
        return PNorthSpineCanteen[(store,meal)][choice]

