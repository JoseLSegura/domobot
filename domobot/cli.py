"""domobot.cli contains handlers for CLI entry points defined for the bot."""

import logging
import sys

from aiogram import executor

from domobot.config import Config
from domobot.status_garage_door_controller import StatusGarageController
from domobot.fake_garage_door import FakeGarageDoor


def domobot_main():
    """Handle for domobot entry point."""
    logging.basicConfig(filename="log", level=logging.DEBUG)

    if len(sys.argv) != 2:
        logging.error("Missing configuration file")
        return 1

    config_path = sys.argv[1]
    config = Config.load_config(config_path)
    garage_door = StatusGarageController(config)
    executor.start_polling(garage_door.dispatcher, skip_updates=True)

    return 0
