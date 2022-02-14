import CellPhoneClass as pc 


def main():



    manname = input("What is the manufacturer name?")
    phmodel = input("Enter the model number:")
    rprice = input("Enter the price of the phone:")

    phone = pc.cellphone(manname,phmodel,rprice)
    print("Manufacturer:" + phone.get__manufact())
    print("Model Number:" + phone.get__model())
    print("Retail Price: $" + '%.2f'% phone.get__retail_price())

main()