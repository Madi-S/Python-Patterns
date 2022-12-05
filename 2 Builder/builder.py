

class Person:
    def __init__(self):
        # Address
        self.street_address = None
        self.postcode = None
        self.city = None

        # Employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address {self.street_address} {self.postcode} {self.city}\n' + \
            f'Employment {self.company_name} {self.position} {self.annual_income}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person
        print('Person init')

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAdressuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at_company(self, company_name):
        self.person.ompany_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def with_income(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAdressuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at_street(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    person = pb\
        .lives.at_street('High Road 32').in_city('Dublin').with_postcode('023312')\
        .works.at_company('Google').as_a('Designer').with_income(140_000)\
        .build()

    print(person)
