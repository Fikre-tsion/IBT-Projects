class Account:
    def __init__(self,owner,account_number,balance=0):
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
            if amount > self.__balance:
                raise ValueError(f"Withdrawal request rejected. The amount must be less than or equal to {self.__balance}")

            self.__balance -= amount

x= Account("Abebe","1000374876997",2000)
x.withdraw(500)
x.deposit(700)
print(f"{x.owner}'s current balance is {x.balance}")

y= Account("Kebede","1000394676097",1250)
y.withdraw(500)
y.deposit(675)
print(f"{y.owner}'s current balance is {y.balance}")

