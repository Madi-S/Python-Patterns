

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if instances.get(class_, None) is None:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database ...')


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 == db2)

    # Loading database ...
    # True
    # Hooray, init is called only once
