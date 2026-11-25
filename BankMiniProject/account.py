# Parent class for all bank accounts

import logging
from transaction import create_transaction
from exceptions import InsufficientFunds


class BankAccount:
    account_count = 1000

    def __init__(self, name, opening_balance):
        BankAccount.account_count += 1

        self.account_number = "AC" + str(BankAccount.account_count)
        self.name = name
        self.__balance = opening_balance
        self.transactions = []

    def get_balance(self):
        return self.__balance

    def add_transaction(self, transaction_type, amount):
        transaction = create_transaction(
            transaction_type,
            amount,
            self.__balance
        )
        self.transactions.append(transaction)

    def deposit(self, amount, transaction_type="Deposit", write_log=True):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.__balance = self.__balance + amount
        self.add_transaction(transaction_type, amount)

        if write_log:
            logging.info("%s: %s deposited Rs. %s",
                         self.account_number, self.name, amount)

    # Child classes can change this rule.
    def withdraw_allowed(self, amount):
        return self.__balance - amount >= 0

    def withdraw(self, amount, transaction_type="Withdraw", write_log=True):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if not self.withdraw_allowed(amount):
            raise InsufficientFunds("Not enough balance.")

        self.__balance = self.__balance - amount
        self.add_transaction(transaction_type, amount)

        if write_log:
            logging.info("%s: %s withdrew Rs. %s",
                         self.account_number, self.name, amount)

    def mini_statement(self):
        yield "----- MINI STATEMENT -----"
        yield "Account number: " + self.account_number
        yield "Name: " + self.name

        # Show only the last five transactions.
        for transaction in self.transactions[-5:]:
            yield (
                transaction.date + " | " +
                transaction.transaction_type + " | Rs. " +
                str(transaction.amount) + " | Balance: Rs. " +
                str(transaction.balance_after)
            )

        yield "Closing balance: Rs. " + str(self.__balance)
