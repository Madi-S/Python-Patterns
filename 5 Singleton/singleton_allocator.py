from random import randint


class Database:
    _instance = None

    def __init__(self):
        i = randint(1, 100)
        print('Loading database ...', i)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()

    print(db1 == db2)
    # Loading database ...  98
    # Loading database ...  52
    # True
    # Because init is always called after __new__
