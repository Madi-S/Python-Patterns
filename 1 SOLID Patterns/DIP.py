# DIP - Dependency Inversion Principle


from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# Low-level module, because it is responsible for stroing data
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# Reserach class should be dependendt on relationships implementation (like list methods)
# High-level module
class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0] == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child {r[2]}')
    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child {p}')


if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Alex')
    child2 = Person('Lexi')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)
    Research(relationships)