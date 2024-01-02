# flyweight is an optimization method, which is used to save memory by storing not the same objects but storing refs to that same objects
# flyweight is used to avoid data duplicates
import string
import random


class User:
    def __init__(self, name):
        self.name = name


# Flyweight applied
class User2:
    strings = []

    def __init__(self, full_name):
        def get_or_add_index(s):
            # return existing name index
            if s in self.strings:
                return self.strings.index(s)
            # add that name and return current last index
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        # store name not as string but as refs
        self.name_ids = [get_or_add_index(name)
                         for name in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[name_id] for name_id in self.name_ids])


def get_random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for _ in range(8)])


if __name__ == '__main__':
    users = []
    first_names = [get_random_string() for _ in range(100)]
    last_names = [get_random_string() for _ in range(100)]

    # 10,000 different entries
    # 10,000 memory entities should be used
    # but we will use only 200 with flyweight
    for first_name in first_names:
        for last_name in last_names:
            # user = User(f'{first_name} {last_name}')
            # users.append(user)
            user = User2(f'{first_name} {last_name}')
            users.append(user)

    print(users[1])
