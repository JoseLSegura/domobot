"""Module for loading the configuration file."""

import json
import logging

import jsonschema
from aiogram.types.user import User

from domobot.schema import CONFIG_JSON_SCHEMA


LOGGER = logging.getLogger(__name__)


class Config:
    """Class containing configuration related methods."""

    CONFIG = None

    @classmethod
    def load_config(cls, file_path):
        """Load a configuration from the file `file_path`."""
        if cls.CONFIG is not None:
            return cls.CONFIG

        with open(file_path, "r") as config_file:
            cls.CONFIG = json.loads(config_file.read())
            try:
                jsonschema.validate(cls.CONFIG, CONFIG_JSON_SCHEMA)

            except jsonschema.ValidationError:
                LOGGER.error(
                    "Error validating the configuration file %s", file_path
                )
                return None

        authorized_users = cls.CONFIG.get("telegram", dict()).get(
            "authorized_users", list()
        )
        int_authorized_users = list

        for authorized_user in authorized_users:
            if authorized_user.isnumeric():
                user_id = int(authorized_user)
                int_authorized_users.append(user_id)

        cls.CONFIG.get("telegram", dict())[
            "authorized_users"
        ] = int_authorized_users

        return cls.CONFIG

    @classmethod
    def get_config(cls) -> dict:
        """Return the loaded config or None if no config is loaded."""
        return cls.CONFIG


def check_authorized_user(user: User) -> bool:
    """Check if the given user is authorized in configuration."""
    authorized_users = (
        Config.get_config()
        .get("telegram", dict())
        .get("authorized_users", list())
    )
    return user.id in authorized_users or user.username in authorized_users
