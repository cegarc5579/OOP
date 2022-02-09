import random
#COIN CLASS IS THE CLASS DEFINITION FILE
#THIS IS THE BLUE PRINT FOR COIN TOSS
# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.
    #this is always going to be the first def 
    #self tells it to operate on this instance
    #sideup is the attribute we came up with 
    #and all our coins are starting with heads up
    #self.____ are attributes
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    #randint (0,1) is the range and the range is 0
    #to 1
    #WE DONT WANT USER TO VIEW THIS SO THAT'S WHAT COIN TOSS 
    #IS FOR AND THEY HAVE TO CALL TOSS IN COIN TOSS FILE

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.
    #THIS METHOD RETURNS THE VALUE OF THE ATTRIBUTE SIDEUP
    def get_sideup(self):
            return self.sideup
