"""fake_garage_door includes a fake GarageDoor controller in order to test."""

import time


class FakeGarageDoor:
    """Defines a GarageDoor class that doesn't do anything."""

    # pylint: disable=unused-argument
    def __init__(self, delay=20.0, **kwargs):
        """Initialize the FakeGarageDoor ignoring all the arguments."""
        self.delay = delay

    def open_door(self):
        """Simulate open_door method."""
        print("Opening door")
        time.sleep(self.delay)

    def close_door(self):
        """Simulate close door method."""
        print("Closing door")
        time.sleep(self.delay)
