"""domobot.motor module includes the motor factory."""

from enum import Enum

from garage_door_controller import GarageDoor


Status = Enum("Status", ["OPENED", "CLOSED"])


class StatusGarageDoor:
    """Store a `GarageDoor` and a best guess for its status."""

    def __init__(self, garage_door_config):
        """Initialize the `GarageDoor` object for the given configuration."""
        self.door = GarageDoor(**garage_door_config)
        self.status = Status.CLOSED

    def open_door(self):
        """Open the `GarageDoor` and update the status."""
        self.door.open_door()
        self.status = Status.OPENED

    def close_door(self):
        """Close the `GarageDoor` and update the status."""
        self.door.close_door()
        self.status = Status.CLOSED

    def get_guessed_status(self):
        """Return the guessed status of the door."""
        return self.status

    def set_status(self, status: Status):
        """Set the current status of the door."""
        self.status = status
