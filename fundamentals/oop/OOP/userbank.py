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

# class User:
#     # other methods
#     def make_deposit(self, amount):
#     	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore

# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes


class BankAccount:
    int_rate = 0.69
    balance = 1000
    bank_name = "First National Dojo"

    def __init__(self, name, int_rate=0.15, balance=1000):
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


Checking = BankAccount("Checking")
Saving = BankAccount("Saving")

Checking.yield_interest(.15).display_account_info()
Saving.yield_interest(.45).display_account_info()

# Checking.deposit(750).deposit(850).deposit(
#     950).withdrawl(350).display_account_info()

# Saving.withdrawl(900).deposit(950).deposit(5050).withdrawl(
#     850).withdrawl(100).withdrawl(100).display_account_info()


class User:
    def __init__(self, name, age):
        self.first_name = name
        self.age = age
        self.account = BankAccount(name, int_rate=0.15, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdraw(self, amount):
        self.account.withdrawl(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(self.first_name, self.account.balance)
        return self


betty = User("Betty", 35)
bill = User("Bill", 13)

betty.make_deposit(400).display_user_balance()
bill.make_withdraw(34).display_user_balance()
