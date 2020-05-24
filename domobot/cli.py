"""domobot.cli contains handlers for CLI entry points defined for the bot."""

import logging
import sys

from aiogram import Bot, Dispatcher, executor

from domobot.config import Config
from domobot.handlers import close_door, door_status, open_door, welcome
from domobot.motor_factory import GarageDoorFactory


def domobot_main():
    """Handle for domobot entry point."""
    logging.basicConfig(filename="log", level=logging.DEBUG)

    if len(sys.argv) != 2:
        logging.error("Missing configuration file")
        return 1

    config_path = sys.argv[1]
    config = Config.load_config(config_path)
    print(config_path)
    bot = Bot(token=config["telegram"]["token"])
    dispatcher = Dispatcher(bot)

    GarageDoorFactory.configure_garage_door(config["garage_door"])

    dispatcher.register_message_handler(welcome, commands=["start"])
    dispatcher.register_message_handler(open_door, commands=["open"])
    dispatcher.register_message_handler(close_door, commands=["close"])
    dispatcher.register_message_handler(door_status, commands=["status"])
    executor.start_polling(dispatcher, skip_updates=True)

    return 0
