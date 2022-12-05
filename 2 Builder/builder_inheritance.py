# Builder inheritance example


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth}' + \
            f' and works as {self.position}'


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonNameBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonNameBuilder):
    def works_as(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born_at(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    person = pb.born_at('1/1/1979').works_as('engineer').called('Mike').build()
    print(person)
