"""Telegram handlers module."""

from aiogram import types

from domobot.config import check_authorized_user
from domobot.motor import get_door


async def welcome(msg: types.Message):
    """Handler for start command."""
    await msg.answer('Hello dude!')


async def open_door(msg: types.Message):
    """Handler for opening the door."""

    if not check_authorized_user(msg.from_user):
        return

    door = get_door()
    await msg.answer('Opening the door...')
    door.open_door()
    await msg.answer('Stop the motor. Door is open')


async def close_door(msg: types.Message):
    """Handler flor closing the door."""

    if not check_authorized_user(msg.from_user):
        return

    door = get_door()
    await msg.answer('Closing the door...')
    door.close_door()
    await msg.answer('Stop the motor. Door is closed')
