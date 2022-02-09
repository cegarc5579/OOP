'''
import InsectClass as ic



def main():
    myins = ic.Insect(2,4)

    for fl in range(10):
        myins.flightlength()
        print("Flight length is:", myins.get_length())
main()
'''

#the following is the code Professor B did and how it should be
#above code did not work right, or it did, but it simply printed it out 
#10 times instead of 1 single time
import InsectClass as ic
myins = ic.Insect(2,4)
myins.flightlength()
print('The insect can fly up to', myins.get_length(),'miles')