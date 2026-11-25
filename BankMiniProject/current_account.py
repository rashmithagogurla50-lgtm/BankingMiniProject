# Current account child class

from account import BankAccount


class CurrentAccount(BankAccount):
    overdraft_limit = 5000

    # Current account can go up to Rs. 5000 below zero.
    def withdraw_allowed(self, amount):
        return self.get_balance() - amount >= -self.overdraft_limit
