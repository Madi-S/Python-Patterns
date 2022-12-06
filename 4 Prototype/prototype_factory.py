

import copy


class Address:
    def __init__(self, street_address, city,  suite):
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 Highway', 'New York', 0))
    aux_office_employee = Employee('', Address('123A Highway', 'New York', 0))

    @staticmethod
    def __new_employee(prototype, name, suite):
        prototype_copy = copy.deepcopy(prototype)
        prototype_copy.name = name
        prototype_copy.address.suite = suite
        return prototype_copy

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


if __name__ == '__main__':
    tim = EmployeeFactory.new_main_office_employee('Tim', 32)
    darya = EmployeeFactory.new_aux_office_employee('Darya', 90)

    print(tim)
    print(darya)
