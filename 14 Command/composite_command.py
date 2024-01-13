import unittest
from command import *


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for cmd in self:
            cmd.invoke()

    def undo(self):
        for cmd in reversed(self):
            cmd.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_account, to_account, amount):
        super().__init__([
            BankAccountCommand(
                from_account, BankAccountCommand.Action.WITHDRAW, amount
            ),
            BankAccountCommand(
                to_account, BankAccountCommand.Action.DEPOSIT, amount
            )
        ])
    
    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok

class TestSuite(unittest.TestCase):
    def test_composite_deposite(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 100
        )
        deposit2 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 150
        )
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(f'After invoke {ba}')
        composite.undo()
        print(f'After undo {ba}')
    
    def test_transfter_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        
        amount = 1000
        wc = BankAccountCommand(
            ba1, BankAccountCommand.Action.WITHDRAW, amount
        )
        dc = BankAccountCommand(
            ba2, BankAccountCommand.Action.DEPOSIT, amount
        )
        
        transfer_composite = CompositeBankAccountCommand([wc, dc])
        transfer_composite.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')
        transfer_composite.undo()
        print(f'ba1: {ba1}, ba2: {ba2}')
    
    def test_transfer_success(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        
        amount = 100 # works for 1000 as well
        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')
        transfer.undo()
        print(f'ba1: {ba1}, ba2: {ba2}')
        print(f'Transfer success: {transfer.success}')
    
if __name__ == '__main__':
    unittest.main()