import CellPhoneClass as pc 


def main():



    manname = input("What is the manufacturer name?")
    phmodel = input("Enter the model number:")
    rprice = float(input("Enter the price of the phone:"))

    phone = pc.cellphone(manname,phmodel,rprice)
    print("Manufacturer:" + phone.get_manufact())
    print("Model Number:" + phone.get_model())
    print("Retail Price: $" + '%.2f'% phone.get_retail_price())

main()