
class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as balance_file:
            self.balance=int(balance_file.read())


    def withdraw(self, amount):
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            self.write_balance(self.balance)
            print("Balance is: ",self.balance)
        else:
            print("insufficient funds to complete this transaction... transaction cancelled")

    def deposit(self, amount):
        self.balance=self.balance+amount
        self.write_balance(self.balance)
        print("Balance is: ",self.balance)


    def write_balance(self,balance):
        with open(self.filepath,'w') as balance_file:
            balance_file.write(str(balance))







account=Account("balance.txt")
account.withdraw(100)
account.deposit(200)
