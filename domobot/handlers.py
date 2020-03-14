import asyncio

from aiogram import types

from .motor import get_door


async def welcome(msg: types.Message):
    await msg.answer('Hello dude!')


async def open_door(msg: types.Message):
    m = get_door()
    await msg.answer('Opening the door...')
    print(f'Motor id: {id(m)}')
    m.open_door()
    await msg.answer('Stop the motor. Door is open')

async def close_door(msg: types.Message):
    m = get_door()
    await msg.answer('Closing the door...')
    m.close_door()
    await msg.answer('Stop the motor. Door is closed')
