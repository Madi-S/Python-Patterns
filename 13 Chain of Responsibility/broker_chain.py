# event broker
# cqs


from abc import ABC
from enum import Enum


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class DoubleDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.DEFENSE:
            query.value *= 2


class Creature:
    def __init__(self, game, name, attack, defense):
        self.name = name
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f'Creature: {self.name} ({self.attack}|{self.defense})'


if __name__ == '__main__':
    game = Game()
    giant = Creature(game, 'Stone Giant', 5, 20)
    ddm = DoubleDefenseModifier(game, giant)
    print(giant)
    # Creature: Stone Giant (5|40)

    with DoubleAttackModifier(game, giant) as dam:
        print(giant)
        # Creature: Stone Giant (10|40)

    print(giant)
    # Creature: Stone Giant (5|40)
