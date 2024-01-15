

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            # items here are callable objects ~ functions
            # `call_doctor`
            item(*args, **kwargs)


class Person:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.addr)


def call_doctor(name, addr):
    print(f'{name} need a doctor at {addr}')


if __name__ == '__main__':
    person = Person('Bob', 'St Avenue 42')
    person.falls_ill.append(call_doctor)
    person.falls_ill.append(
        lambda name, addr: print(f'{name} is ill')
    )

    person.catch_a_cold()
    # >>> Bob need a doctor at St Avenue 42
    # >>> Bob is ill

    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()
    # >>> Bob is ill
