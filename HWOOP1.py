import random
import shelve
from datetime import datetime


# 1
class BankAccount:
    def __init__(self, account_id, full_name_owner, balance):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance
        self.time_stamp = datetime.now()

    def __str__(self):
        return (f"BankAccount; account_id: {self.account_id}, full_name_owner: {self.full_name_owner}, "
                f"balance: {self.balance}, time created: {self.time_stamp}")

    def __repr__(self):
        return f"BankAccount({self.account_id}, {self.full_name_owner}, {self.balance})"

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        return BankAccount(random.randint(self.account_id + other.account_id, 10 ** 10),
                           self.full_name_owner + ' & ' + other.full_name_owner, self.balance + other.balance)

    def __sub__(self, other):
        return self.balance - other.balance

    def __mul__(self, other):
        return self.balance * other.balance

    def __len__(self):
        return int((datetime.now() - self.time_stamp).total_seconds() // 60)


b1 = BankAccount(8676230, "arya stark", 28000)
bg = BankAccount(6875533, "golum", 28000)
b2 = BankAccount(5979982, "jon snow", 79011)
print(bg == b1)  # True
print(b1 != b2)  # False
print(b1 > b2)  # False because 28000 is not bigger than 79011
print(b1 < b2)  # True because 28000 is smaller than 79011
b3 = b1 + b2  # will create a new account:
print(b3, repr(b3))
# account_id=random number,
# full_name_owner=“arya stark and jon snow”
# balance=28000+79011=107,011
print(b2 - b1)  # 51,011
print(b2 * b1)  # 2,212,308,000

# 2

print(len(b3))

# 3

accounts = shelve.open('accounts.db')

# accounts['b3'] = b3

print(accounts['b3'])

accounts.close()
