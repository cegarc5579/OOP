from datetime import date

class Student: 
    
    def __init__(self, studentid, name, dateob, classif):
        self.__studentID = studentid
        self.__name = name 
        self.__dateofb = dateob
        self.__classification = classif
        self.__age = 0

    def age(self):
        today = date.today()
        self.__age = today.year-int(self.__dateofb)
    
    def get_age(self):
        return self.__age
    
    def registrate(self):
        if self.__classification == 'F':
            print("Registration Open: 11/10-11/12")
        elif self.__classification == 'Jr':
            print("Registration Open: 11/4-11/6")
        else:
            print("Registration Open: 11/1-11/3")
    
    
