from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == '__main__':
    code = '5252'
    state = State.LOCKED
    entry = ''

    while True:
        if state == State.LOCKED:
            entry += input(entry)

            if entry == code:
                state = State.UNLOCKED
            if not code.startswith(entry):
                state = State.FAILED

        elif state == State.FAILED:
            print('FAILED')
            entry = ''
            state = State.LOCKED

        elif state == State.UNLOCKED:
            print('UNLOCKED')
            break