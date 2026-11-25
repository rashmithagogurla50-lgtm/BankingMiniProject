# Main program - run this file

import logging
from bank import Bank
from exceptions import BankError


logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    bank = Bank()

    while True:
        print("\n===== PYBANK =====")
        print("1. Open account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Mini statement")
        print("6. Quit")

        choice = input("Enter your choice: ")

        try:
            match choice:
                case "1":
                    name = input("Enter customer name: ")
                    account_type = input("Savings or Current: ")
                    balance = float(input("Enter opening balance: "))

                    account = bank.open_account(
                        account_type, name, balance
                    )

                    print("Account opened successfully.")
                    print("Account number:", account.account_number)

                case "2":
                    number = input("Enter account number: ")
                    amount = float(input("Enter deposit amount: "))

                    account = bank.find_account(number)
                    account.deposit(amount)

                    print("Deposit successful.")
                    print("Balance:", account.get_balance())

                case "3":
                    number = input("Enter account number: ")
                    amount = float(input("Enter withdrawal amount: "))

                    account = bank.find_account(number)
                    account.withdraw(amount)

                    print("Withdrawal successful.")
                    print("Balance:", account.get_balance())

                case "4":
                    sender = input("Enter sender account number: ")
                    receiver = input("Enter receiver account number: ")
                    amount = float(input("Enter transfer amount: "))

                    bank.transfer(sender, receiver, amount)
                    print("Transfer successful.")

                case "5":
                    number = input("Enter account number: ")
                    account = bank.find_account(number)

                    for line in account.mini_statement():
                        print(line)

                case "6":
                    print("Thank you for using PyBank.")
                    break

                case _:
                    print("Invalid choice. Try again.")
                    logging.warning("Invalid menu choice: %s", choice)

        except (ValueError, BankError) as error:
            print("Error:", error)
            logging.error("Operation failed: %s", error)


if __name__ == "__main__":
    main()
