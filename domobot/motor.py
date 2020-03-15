import logging

from garage_door_controller import GarageDoor


DOOR = None


def get_door(garage_door_config=None):
    global DOOR

    if not DOOR:
        if not garage_door_config:
            logging.error(
                "The GarageDoor object needs configuration for the first time")
            return None

        DOOR = GarageDoor(**garage_door_config)
        return DOOR

    if garage_door_config:
        logging.warning(
            "Garage door already configured. Ignoring configuration")

    return DOOR
