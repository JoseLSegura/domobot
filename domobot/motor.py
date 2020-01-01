from enum import Enum, auto


MOTOR = None


def get_motor():
    global MOTOR
    if MOTOR is None:
        MOTOR = Motor()

    return MOTOR


class MotorStatus(Enum):
    CLOSED = auto()
    OPENING = auto()
    OPENED = auto()
    CLOSING = auto()
    OPENING_STOPPED = auto()
    CLOSING_STOPPED = auto()


class Motor:
    def __init__(self):
        self.status = MotorStatus.CLOSED

    def open(self):
        if self.status is MotorStatus.OPEN:
            return

        if self.status is MotorStatus.CLOSED:
            # lock.open()
            pass
