#assignment
class BankAccount:
    def __init__(self, account_number:str, balance:float,owner:str,type:str):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

        
        
class Bank:
    def __init__(self, name:str, accounts:list):
        self.name = name
        self.accounts = accounts
        accounts=["savings account","current account","students account","fixed account"]


class Customer:
    def __init__(self,name:str, accounts:list):
        self.name = name
        self.accounts = accounts
        accounts=["savings account","current account","students account","fixed account"]
    def speak(self):
        print(f"The {self.name} is done")


      
class Transactions:
    def __init__ (self,account:BankAccount, amount:float, type:str):
        self.account = account
        self.amount = amount
        self.type = type


def __create_account(
    new_customer=Customer,
    new_BankAccount = BankAccount,
    new_Bank = Bank):
    return f"{new_Bank}  has allowed a new {new_BankAccount}"


