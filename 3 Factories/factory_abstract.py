

from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('Drinking Tea ...')


class Coffee(HotDrink):
    def consume(self):
        print('Drinking Coffee ...')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Preparing tea ...\nPouring {amount}ml of tea ...')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Preparing coffee ...\nPouring {amount}ml of coffee')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        TEA = auto()
        COFFEE = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            for drink in self.AvailableDrink:
                name = drink.name.capitalize()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))
            self.initialized = True

    def make_drink(self):
        print('Available drinks')
        for f in self.factories:
            print(f[0])

        entry = int(
            input(f'Please pic a drink (0-{len(self.factories) - 1}): '))
        amount = int(input('Specify amount: '))

        return self.factories[entry][1].prepare(amount)
        # return self.factories[entry][1].prepare(amount).consume()


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
