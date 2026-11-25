# Savings account child class

from account import BankAccount


class SavingsAccount(BankAccount):
    minimum_balance = 1000
    interest_rate = 0.04

    def __init__(self, name, opening_balance):
        if opening_balance < self.minimum_balance:
            raise ValueError("Savings account needs at least Rs. 1000.")

        super().__init__(name, opening_balance)

    # Savings account must keep Rs. 1000 after withdrawal.
    def withdraw_allowed(self, amount):
        return self.get_balance() - amount >= self.minimum_balance

    def add_monthly_interest(self):
        interest = self.get_balance() * self.interest_rate / 12
        self.deposit(interest, "Monthly interest")
        print("Monthly interest added:", interest)
