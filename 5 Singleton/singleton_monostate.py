# This approach of suing monostate class is not recommende (its a bit messy)
# Its better to use decorator or metaclass approach


class CEO:
    __shared_state = {
        'name': 'Bob',
        'age': 48
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CTO(Monostate):
    def __init__(self):
        self.name = ''
        self.salary = 1000000

    def __str__(self):
        return f'Name: {self.name}, salary: ${self.salary}'


if __name__ == '__main__':
    # ceo1 = CEO()
    # ceo2 = CEO()

    # print(ceo1)

    # ceo2.age = 55

    # print(ceo1)
    # print(ceo2)
    cto1 = CTO()
    cto1.name = 'Tim'
    cto1.salary = 2000000

    print(cto1)

    cto2 = CTO()
    cto2.name = 'Alex'
    cto2.salary = 3000000

    print(cto1, cto2, sep='\n')
