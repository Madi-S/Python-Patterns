import copy


class Address:
    def __init__(self, street_address, city,  country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


if __name__ == '__main__':
    # address = Address('123 Highway', 'New York', 'USA')
    # bob=Person('Bob', address)
    # jane=Person('Jane', address)
    # jane.address.street_address = '1222 Highway'
    # Address object reference the same address object
    # print(bob)
    # print(jane)

    bob = Person('Bob', Address('123 Highway', 'New York', 'USA'))
    jane = copy.deepcopy(bob)
    jane.name = 'Jane'
    jane.address.street_address = '124 Highway'
    print(bob)
    print(jane)

    # if copy.copy
    # Bob lives at 124 Highway, New York, USA
    # Jane lives at 124 Highway, New York, USA
    # Thus, we need deepcopy
