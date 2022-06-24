# class BankAccount:
#     # class attribute
#     bank_name = "First National Dojo"
#     all_accounts = []
#     def __init__(self, int_rate,balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.all_accounts.append(self)
#     # class method to change the name of the bank
#     @classmethod
#     def change_bank_name(cls,name):
#         cls.bank_name = name
#     # class method to get balance of all accounts
#     @classmethod
#     def all_balances(cls):
#         sum = 0
#         # we use cls to refer to the class
#         for account in cls.all_accounts:
#             sum += account.balance
#         return sum

class BankAccount:
    int_rate = 0.69
    balance = 1000
    bank_name = "First National Dojo"

    def __init__(self, name, int_rate=0.69, balance=1000):
        self.int_rate = int_rate
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if self.balance < amount:
            self.balance - 5
            print("insuffcient funds")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.name, self.balance, self.int_rate)
        return self

    def yield_interest(self, int_rate):
        self.balance += self.balance * int_rate
        return self


Checking = BankAccount("checking", 0.69, 1000)
Saving = BankAccount("Saving", 0.69, 1000)

Checking.deposit(750).deposit(850).deposit(
    950).withdrawl(350).display_account_info()

Saving.withdrawl(900).deposit(950).deposit(5050).withdrawl(
    850).withdrawl(100).withdrawl(100).display_account_info()
