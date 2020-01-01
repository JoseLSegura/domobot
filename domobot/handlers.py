import asyncio

from aiogram import types

from .motor import get_motor


async def welcome(msg: types.Message):
    await msg.answer('Hello dude!')


async def open_door(msg: types.Message):
    m = get_motor()
    await msg.answer('Opening the door...')
    print(f'Motor id: {id(m)}')
    m.open()
    await asyncio.sleep(5)
    await msg.answer('Stop the motor. Door is open')

