class Car():

    def __init__(self, year, carmake):
        self.__year_model = year
        self.__make = carmake 
        self.__speed = 0

    def get_yearmodel(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def accelerate(self):
        self.__speed += 5
        return self.__speed
   
    def brake(self):
        self.__speed -= 5
        return self.__speed
    
    
    def get_speed(self):
        return self.__speed
