# Bank class manages all customer accounts

import logging
from savings_account import SavingsAccount
from current_account import CurrentAccount
from exceptions import AccountNotFound, InsufficientFunds


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_type, name, opening_balance):
        if account_type.lower() == "savings":
            account = SavingsAccount(name, opening_balance)

        elif account_type.lower() == "current":
            account = CurrentAccount(name, opening_balance)

        else:
            raise ValueError("Choose Savings or Current account.")

        self.accounts[account.account_number] = account
        logging.info("New account opened: %s", account.account_number)

        return account

    def find_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFound("Account number does not exist.")

        return self.accounts[account_number]

    def transfer(self, from_number, to_number, amount):
        # First find both accounts.
        sender = self.find_account(from_number)
        receiver = self.find_account(to_number)

        if from_number == to_number:
            raise ValueError("Cannot transfer to the same account.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Check sender before moving any money.
        if not sender.withdraw_allowed(amount):
            raise InsufficientFunds("Not enough balance to transfer.")

        # Now move the money.
        sender.withdraw(amount, "Transfer sent", False)
        receiver.deposit(amount, "Transfer received", False)

        logging.info("Transfer Rs. %s from %s to %s",
                     amount, from_number, to_number)
