import logging
import sys

from aiogram import Bot, Dispatcher, executor

from domobot.config import load_config
from domobot.handlers import welcome, open_door
from domobot.motor import get_motor


def domobot_main():
    logging.basicConfig(filename='log', level=logging.DEBUG)

    if len(sys.argv) != 2:
        logging.error("Missing configuration file")
        return 1

    config_path = sys.argv[1]
    config = load_config(config_path)
    bot = Bot(token=config["telegram"]["token"])
    dispatcher = Dispatcher(bot)

    m = get_motor()
    dispatcher.register_message_handler(welcome, commands=['start'])
    dispatcher.register_message_handler(open_door, commands=['open'])
    executor.start_polling(dispatcher, skip_updates=True)

    return 0
