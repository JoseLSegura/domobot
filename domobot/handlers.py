"""Telegram handlers module."""

from aiogram import types

from domobot.config import check_authorized_user
from domobot.motor_factory import GarageDoorFactory


async def welcome(msg: types.Message):
    """Handle for start command."""
    await msg.answer("Hello dude!")


async def open_door(msg: types.Message):
    """Handle for opening the door."""
    if not check_authorized_user(msg.from_user):
        return

    door = GarageDoorFactory.get_garage_door()
    await msg.answer("Opening the door...")
    door.open_door()
    await msg.answer("Stop the motor. Door is open")


async def close_door(msg: types.Message):
    """Handle flor closing the door."""
    if not check_authorized_user(msg.from_user):
        return

    door = GarageDoorFactory.get_garage_door()
    await msg.answer("Closing the door...")
    door.close_door()
    await msg.answer("Stop the motor. Door is closed")


async def door_status(msg: types.Message):
    """Handle for getting the guessed status of the door."""
    if not check_authorized_user(msg.from_user):
        return

    status = GarageDoorFactory.get_garage_door().get_status()
    await msg.reply(status)
