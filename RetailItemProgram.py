import RetailItemClass as ric 

def main():
    #descrip = {"Jacket", "Designer Jeans", "shirt"}
    #unitsinv = {"12","40","20"}
    #price = {"$59.95", "$34.95", "$24.95"}


    item1 = ric.RetailItem("Jacket","12", "$59.95")
    item2 = ric.RetailItem("Designer Jeans","40", "$34.95")
    item3 = ric.RetailItem("Shirt","20","$24.95")

    print("Item 1" + '\n' + "Description:", item1.get_itemdescrip()+ '\n' + "Units in Inventory:", item1.get_unitsininven() + '\n'+ "Price:", item1.get_price())
    print("Item 2" + '\n' + "Description:", item2.get_itemdescrip()+ '\n' + "Units in Inventory:", item2.get_unitsininven() + '\n'+ "Price:", item2.get_price())
    print("Item 3" + '\n' + "Description:", item3.get_itemdescrip()+ '\n' + "Units in Inventory:", item3.get_unitsininven() + '\n'+ "Price:", item3.get_price())


main()