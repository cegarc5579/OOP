class RetailItem():

    def __init__(self,descrip,unitsinv,price):
        self.__itemdescrip = descrip 
        self.__unitsinv = unitsinv
        self.__price = price
    
    def get_itemdescrip(self):
        return self.__itemdescrip
    def get_unitsininven(self):
        return self.__unitsinv 
    def get_price(self):
        return self.__price 