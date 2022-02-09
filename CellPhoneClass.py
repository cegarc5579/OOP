class cellphone():


    def __init__(self,manname,phmodel,rprice):
        self.__manufact = manname
        self.__model = phmodel
        self.__retail_price = rprice
    

    def set_manufact(self, manname):
        self.__manufact = manname
    
    def set_model(self, phmodel):
        self.__model = phmodel

    def set_retail_price(self, rprice):
        self.__retail_price = rprice
    
    def get_manufact(self):
        return self.__manufact 

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

        
