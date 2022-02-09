# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
      #balance is an argument coming in from the user 
        self.__balance = bal

      # The deposit method makes a deposit into the
      # account.
  #deposit method allows us to receive an amount and change the balance in the savings account
    def deposit(self, amount):
        self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.
#expecting a variable from user and then it does a calculation
    def withdraw(self, amount):
      #this if statement means the user can't put in a number less than zero
      #aka a negative number
      if amount <= 0:
        print("You fool!")
      else:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

      # The get_balance method returns the
      # account balance.
#this get_balance method returns the value of the balance attribute
    def get_balance(self):
        return self.__balance



    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')
