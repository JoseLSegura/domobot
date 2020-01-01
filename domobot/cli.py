import argparse
import logging

from aiogram import Bot, Dispatcher, executor

from .handlers import welcome, open_door
from .motor import get_motor


def domobot_main():
    logging.basicConfig(filename='log', level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--token', type=str, required=True,
        help='Telegram bot API token to be used'
    )

    args = parser.parse_args()
    bot = Bot(token=args.token)
    dispatcher = Dispatcher(bot)

    m = get_motor()
    print(f'Motor id: {id(m)}')

    dispatcher.register_message_handler(welcome, commands=['start'])
    dispatcher.register_message_handler(open_door, commands=['open'])
    executor.start_polling(dispatcher, skip_updates=True)

    return 0
