"""
domobot.motor_factory module.

Contains the class and methods necessary to avoid creating several
`GarageDoor` objects at the same time.
"""

from domobot.motor import StatusGarageDoor


class GarageDoorInitException(Exception):
    """Exception related to handling a `StatusGarageDoor`."""


class GarageDoorFactory:
    """Factory class for accesing a single motor."""

    DOOR = None

    @classmethod
    def configure_garage_door(cls, garage_door_config: dict):
        """Configure a `StatusGarageDoor`."""
        if not garage_door_config:
            raise GarageDoorInitException(
                "The GarageDoor object needs configuration for the first time"
            )

        cls.DOOR = StatusGarageDoor(**garage_door_config)

    @classmethod
    def get_garage_door(cls):
        """Return a `StatusGarageDoor` instance."""
        if not cls.DOOR:
            raise GarageDoorInitException(
                "The GarageDoor object is not configured"
            )

        return cls.DOOR
