import argparse
import logging

from aiogram import Bot, Dispatcher, executor

from .handlers import welcome, open_door, close_door
from .motor import get_door


def domobot_main():
    logging.basicConfig(filename='log', level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--token', type=str, required=True,
        help='Telegram bot API token to be used'
    )
    parser.add_argument(
        '--pin_lock', type=int, required=True,
        help='Integer indicating the GPIO pin used for electric lock'
    )
    parser.add_argument(
        '--pin_motor_open', type=int, required=True,
        help='Integer indicating the GPIO pin used for controlling open motor'
    )
    parser.add_argument(
        '--pin_motor_close', type=int, required=False,
        help='Integer indicating the GPIO pin used for controlling close motor'
    )

    args = parser.parse_args()
    bot = Bot(token=args.token)
    dispatcher = Dispatcher(bot)

    get_door(args)

    dispatcher.register_message_handler(welcome, commands=['start'])
    dispatcher.register_message_handler(open_door, commands=['open'])
    dispatcher.register_message_handler(close_door, commands=['close'])
    executor.start_polling(dispatcher, skip_updates=True)

    return 0
