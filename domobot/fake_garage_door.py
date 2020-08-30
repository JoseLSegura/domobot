class FakeGarageDoor:
    """Defines a GarageDoor class that doesn't do anything."""
    def __init__(self, **kwargs):
        """Initialize the FakeGarageDoor ignoring all the arguments."""

    def open_door(self):
        print("Opening door")

    def close_door(self):
        print("Closing door")
