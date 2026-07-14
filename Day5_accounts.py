from abc import abstractmethod, ABC
from typing import override


class Account(ABC):
    def __init__(self,owner,account_number,balance):
        self.owner=owner
        self.account_number=account_number
        self.__balance=balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self,amount):
            if (amount < 0):
                raise ValueError ("Amount must be greater than 0. Please insert positive number.")
            self.__balance += amount
    def withdraw(self,amount):
            if(amount<0):
                raise ValueError ("Amount must be greater than 0. Please insert positive number.")
            if (amount
                    > self.__balance):
                raise ValueError(f"Withdrawal request rejected. The amount must be less than or equal to {self.__balance}")

            self.__balance -= amount

    @abstractmethod
    def statement(self):
        pass

    def interest(self):
        pass

class SavingAccount(Account):
    def __init__(self,owner,account_number,balance,rate):
        super().__init__(owner,account_number,balance)
        self.rate=rate

    def add_interest(self):
        return self.__balance

    def statement(self):
        print(f"This saving account is owned by {self.owner} with a balance of {self.balance}")

    def interest(self):
        return self.balance * 0.05

class CurrentAccount(Account):
    def __init__(self,owner,account_number,balance,overdraft):
        super().__init__(owner,account_number,balance)
        self.overdraft=overdraft

    @override
    def withdraw(self,amount):
        if amount < 0:
            print("Amount can not be negative.")
        elif amount >= self.__balance + self.overdraft:
            print(f"the amount must be less than {self.balance + self.overdraft}.")
        elif amount <= self.__balance + self.overdraft:
            self.__balance -= amount
            print(f"Dear {self.owner}, your current balance is {self.__balance}")
        return self.__balance

    def statement(self):
        print(f"This current account is owned by {self.owner} with a balance of {self.balance}")

    def interest(self):
        return 0


accounts=[
    SavingAccount("Fikre",1000374876997,2000,0.10),
    CurrentAccount("Dawit",1000123412342,10000,1000)
]

# dawit = CurrentAccount("Dawit",1000123412342,10000,1000)
# CurrentAccount.withdraw(dawit,11000)

for acct in accounts:
    acct.statement()

print(accounts[1].withdraw(1000))