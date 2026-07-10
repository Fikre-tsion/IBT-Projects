class Account:
    def _init_(self,owner,account_number,balance=0):
        self.owner=owner
        self.account_number=account_number
        self.__balance=balance