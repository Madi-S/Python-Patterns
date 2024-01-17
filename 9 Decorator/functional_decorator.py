# Decorator allows add additional behaviour to classes withouth changing classes/functions themselves or inheritance
# The use of decorators supports OCP, SRP
# It allows to interact with low-level structures
# Decorator is a class that refers to the object you want decorate
# This is an mistake.
import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took {int(end-start)*1000} ms')
        return result
    return wrapper


@time_it
def some_operation():
    print('Starting operation')
    time.sleep(1)
    print('We are finished')
    return 123


if __name__ == '__main__':
    # some_operation()
    # time_it(some_operation)()
    some_operation()
