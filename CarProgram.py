
import CarClass as cc 

def main():
    vehicle = cc.Car(2019, "Ford Fusion")

    for c in range(1,6):
        vehicle.accelerate()
        print("The car is moving:", vehicle.get_speed())
   
    for ca in range(1,6):
        vehicle.brake()
        print("The car is moving:", vehicle.get_speed())
main()        

