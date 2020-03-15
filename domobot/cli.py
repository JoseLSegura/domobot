import logging
import sys

from aiogram import Bot, Dispatcher, executor

from domobot.config import load_config
from domobot.handlers import welcome, open_door, close_door
from domobot.motor import get_door


def domobot_main():
    """Handler for domobot entry point."""
    logging.basicConfig(filename='log', level=logging.DEBUG)

    if len(sys.argv) != 2:
        logging.error("Missing configuration file")
        return 1

    config_path = sys.argv[1]
    config = load_config(config_path)
    print(config_path)
    bot = Bot(token=config["telegram"]["token"])
    dispatcher = Dispatcher(bot)

    get_door(config["garage_door"])

    dispatcher.register_message_handler(welcome, commands=['start'])
    dispatcher.register_message_handler(open_door, commands=['open'])
    dispatcher.register_message_handler(close_door, commands=['close'])
    executor.start_polling(dispatcher, skip_updates=True)

    return 0
