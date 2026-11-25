# Custom error classes

class BankError(Exception):
    pass


class InsufficientFunds(BankError):
    pass


class AccountNotFound(BankError):
    pass
