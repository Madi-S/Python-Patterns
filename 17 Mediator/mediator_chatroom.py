

class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def say(self, message):
        self.room.broadcast(self.name, message)

    def receive(self, sender, msg):
        s = f'{sender}: {msg}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def private_msg(self, who, msg):
        self.room.message(self.name, who, msg)


class ChatRoom:
    def __init__(self):
        self.people = []

    def broadcast(self, source, msg):
        for person in self.people:
            if person.name != source:
                person.receive(source, msg)

    def join(self, person):
        join_msg = f'{person.name} has joined the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source, destination, msg):
        for person in self.people:
            if person == destination:
                person.receive(source, msg)


if __name__ == '__main__':
    room = ChatRoom()

    p1 = Person('Alex')
    p2 = Person('Thomas')
    p3 = Person('Stephanie')

    room.join(p1)
    room.join(p2)
    room.join(p3)

    p1.say('Hello everyone')
    p2.say('Hey Alex')
    p3.say('Howdy Alex and Thomas')

    p1.private_msg(p2, 'Stephanie seems suspicious')
