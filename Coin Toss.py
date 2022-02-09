import CoinClass as c
#import CoinClass not COIN
#you have to import the entire class definition file
# c is the alias for CoinClass


# The main function.
def main():
       # Create an object from the Coin class.
       # coin is the name of the class
       #the following line of code creates an instance of the CoinClass
       #my_coin is an object that belong to coinclass
       #wouldn't use Coin anymroe because its the object ur dealing with
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')

       #the following code flips the coin 10 times
       for count in range(10):
           my_coin.toss()
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
