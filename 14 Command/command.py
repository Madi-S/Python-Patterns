from abc import ABC
from enum import Enum, auto


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount) -> bool:
        self.balance += amount
        print(f'Deposited: {amount}\nBalance: {self.balance}')
        return True

    def withdraw(self, amount) -> bool:
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'Withdrew: {amount}\nBalance: {self.balance}')
            return True
        return False

    def __str__(self):
        return f'Balance: {self.balance}'


class Command(ABC):
    def __init__(self):
        self.success = None

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = auto()
        WITHDRAW = auto()

    def __init__(self, account, action, amount):
        super().__init__()
        self.action = action
        self.amount = amount
        self.account = account

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if self.success:
            if self.action == self.Action.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action == self.Action.WITHDRAW:
                self.account.deposit(self.amount)


if __name__ == '__main__':
    ba = BankAccount()
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 1000
    )
    cmd.invoke()
    print(f'After $1000 deposit: {ba}')
    cmd.undo()
    print(f'After $100 deposit undone: {ba}')

    illegal_cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.WITHDRAW, 1000
    )
    illegal_cmd.invoke()
    illegal_cmd.undo()
