

class Creature:
    # indices for values of self.stats
    # this way it is much easier to add new properties
    # withouth chaning the existing code
    _strength = 0
    _agility = 1
    _intellegence = 2

    def __init__(self):
        # properties aligned in an iterable object
        # where every number (value) has a designated index
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intellegence(self):
        return self.stats[Creature._intellegence]

    @intellegence.setter
    def intellegence(self, value):
        self.stats[Creature._intellegence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def min_stat(self):
        return min(self.stats)

    @property
    def average_stat(self):
        return float(self.sum_of_stats / len(self.stats))
