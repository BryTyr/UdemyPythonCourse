
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


class SavingsAccount(Account):

    def __init__(self,filepath,string):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        if self.balance-amount>=0:
            self.balance=self.balance-amount
            self.write_balance(self.balance)
            print("transfer sucessful: Balance is: ",self.balance)
        else:
            print("insufficient funds to complete this transaction... transfer cancelled")


# account=Account("balance.txt")
# account.withdraw(100)
# account.deposit(200)

saving_account1=SavingsAccount("balance.txt","one")
saving_account1.withdraw(150)
saving_account1.deposit(300)

saving_account2=SavingsAccount("balance.txt","two")
saving_account2.withdraw(150)
saving_account2.deposit(300)
