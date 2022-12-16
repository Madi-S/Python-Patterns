

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls._instances.get(cls, None) is None:
            cls._instances[cls] = super(Singleton, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database ...')


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)
    # Loading database ...
    # True
