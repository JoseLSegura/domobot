import logging

from gpiozero import DigitalOutputDevice
from garage_door_controller import GarageDoor


DOOR = None


def get_door(args=None):
    global DOOR

    if not DOOR:
        if not args:
            logging.error(
                "The GarageDoor object needs configuration for the first time")
            return None

        DOOR = GarageDoor(args.pin_lock, args.pin_motor_open, args.pin_motor_close)
        return DOOR

    if args:
        logging.warning(
            "Garage door already configured. Ignoring configuration")

    return DOOR
