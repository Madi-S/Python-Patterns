# SRP - Single Responsibility Principle
# Every class or function should be defined to execute a single action
# Every class should have 1 reason to be modified


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        self.entries.pop(pos)

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     with open(filename, 'w') as f:
    #         f.write(str(self))

    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass


# Third-party class defined for file handling
class PersistenceManager:
    @staticmethod
    def save_to_file(filename, journal):
        with open(filename, 'w') as f:
            f.write(str(journal))


if __name__ == '__main__':
    j = Journal()
    j.add_entry('Hello, world')
    j.add_entry('Everything is alright')
    print('Journal:\n', j)

    file = 'test/journal.txt'
    PersistenceManager.save_to_file(file, j)
