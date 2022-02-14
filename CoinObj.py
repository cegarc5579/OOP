import CoinClass as c
def show_coin_status(coin_obj):
    print("This side of the coin is up", coin_obj.get_sideup())

def flip(coin_obj):
    coin_obj.toss()
#the following line creates an instance  
my_coin = c.Coin()
#my_coin is the instance so that's what you pass it through in the bottom () 
#show_coin_status(my_coin)
#flip it through my_coin because its the object
for i in range(10):
    flip(my_coin)
    show_coin_status(my_coin)