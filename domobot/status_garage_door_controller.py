"""domobot.status_garage_door_controller module includes the motor factory."""

import asyncio
from enum import Enum

from aiogram import Bot, Dispatcher, types
from garage_door_controller import GarageDoor

from domobot.config import check_authorized_user
from domobot.fake_garage_door import FakeGarageDoor


Status = Enum("Status", ["OPENED", "CLOSED"])


class StatusGarageController:
    """Store a `GarageDoor` and a best guess for its status."""

    def __init__(self, config):
        """Initialize the `GarageDoor` object for the given configuration."""
        garage_door_config = config["garage_door"]

        if garage_door_config.get("fake", False):
            door_cls = FakeGarageDoor

        else:
            door_cls = GarageDoor

        self.door = door_cls(**config.get("garage_door", dict()))
        self.status = Status.CLOSED
        self.bot = Bot(config["telegram"]["token"])
        self.__dispatcher = Dispatcher(self.bot)

        self.__dispatcher.register_message_handler(
            self.welcome, commands=["start"]
        )
        self.__dispatcher.register_message_handler(
            self.open_handler, commands=["open"]
        )
        self.__dispatcher.register_message_handler(
            self.close_handler, commands=["close"]
        )
        self.__dispatcher.register_message_handler(
            self.door_status, commands=["status"]
        )
        self.__dispatcher.register_callback_query_handler(self.keyboard_answer)

    def open_door(self):
        """Open the `GarageDoor` and update the status."""
        self.door.open_door()
        self.status = Status.OPENED

    def close_door(self):
        """Close the `GarageDoor` and update the status."""
        self.door.close_door()
        self.status = Status.CLOSED

    def get_guessed_status(self):
        """Return the guessed status of the door."""
        return self.status

    def set_status(self, status: Status):
        """Set the current status of the door."""
        self.status = status

    @property
    def dispatcher(self):
        """Get the Dispatcher object."""
        return self.__dispatcher

    async def welcome(self, msg: types.Message):
        """Handle for start command."""
        await self.show_keyboard(msg)

    async def show_keyboard(self, msg: types.Message):
        """Handle command keyboard for showing a buttons keyboard."""
        keyboard_markup = types.InlineKeyboardMarkup()
        text_and_data = {
            "Open": "open",
            "Close": "close",
        }

        row_btns = (
            types.InlineKeyboardButton(text, callback_data=data)
            for text, data in text_and_data.items()
        )
        keyboard_markup.row(*row_btns)
        await msg.answer(
            "What do you want to do?", reply_markup=keyboard_markup
        )

    async def keyboard_answer(self, callback_query: types.CallbackQuery):
        """Handle the answer to the keyboard."""
        if not check_authorized_user(callback_query.from_user):
            return

        print(callback_query.data)
        if callback_query.data == "open":
            msg_text = "Opening door..."
            action = self.open_door

        elif callback_query.data == "close":
            msg_text = "Closing door..."
            action = self.close_door

        new_msg = await callback_query.message.answer(msg_text)
        action()

        await callback_query.answer()
        await asyncio.sleep(5)
        await new_msg.delete()

    # pylint: disable=unused-argument
    async def open_handler(self, msg: types.Message):
        """Handle the open command."""
        self.open_door()

    # pylint: disable=unused-argument
    async def close_handler(self, msg: types.Message):
        """Handle the close command."""
        self.close_door()

    async def door_status(self, msg: types.Message):
        """Handle the status command."""
        await msg.answer(self.status)
