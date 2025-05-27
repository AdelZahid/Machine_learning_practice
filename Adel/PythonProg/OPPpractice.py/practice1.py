class Account:
    __acc_pass = "nothing"  # private class attribute


    @staticmethod
    def creating():
        print("Account has been created successfully")


    def __init__(self, accn, balance):
        self.accn = accn
        self.balance = balance
        self.__acc_pass = ""  # initialize instance-level private attribute


    def setPass(self, password):
        self.__acc_pass = password  # instance-level password setter


    @property
    def getPass(self):
        print(self.__acc_pass)  # instance-level password getter


    @classmethod
    def change_pass(cls, password):
        cls.__acc_pass = password  # changes the class-level private attribute


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful")
        else:
            print("Insufficient balance")


    def print_balance(self):
        print(f"The current balance is: {self.balance} in account {self.accn}")
        

# Test the Account class
A1 = Account("As#05%fk.565", 10000)
A1.creating()
A1.setPass("Adel143.%")

deposit_amount = int(input("Enter the amount to deposit: "))
A1.deposit(deposit_amount)

withdraw_amount = int(input("Enter the amount to withdraw: "))
A1.withdraw(withdraw_amount)

A1.print_balance()
A1.getPass  # Get the private password

print(A1.accn)

# Deleting account number attribute
del A1.accn
try:
    print(A1.accn)
except AttributeError:
    print("Account number deleted")

# Changing the class-level password
A1.change_pass("Fucking143.")
A1.getPass
