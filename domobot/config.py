"""Module for loading the configuration file."""

import json
import logging

import jsonschema
from aiogram.types.user import User

from domobot.schema import CONFIG_JSON_SCHEMA


CONFIG = None
LOGGER = logging.getLogger(__name__)


def load_config(file_path):
    """Open the file pointed by `file_path` argument and load the
    configuration."""

    global CONFIG

    if CONFIG is not None:
        return CONFIG

    with open(file_path, 'r') as config_file:
        CONFIG = json.loads(config_file.read())
        try:
            jsonschema.validate(CONFIG, CONFIG_JSON_SCHEMA)

        except jsonschema.ValidationError:
            LOGGER.error("Error validating the configuration file %s",
                         file_path)
            return None

    for authorized_user in CONFIG["telegram"]["authorized_users"]:
        if authorized_user.isnumeric():
            user_id = int(authorized_user)
            CONFIG["telegram"]["authorized_users"].remove(authorized_user)
            CONFIG["telegram"]["authorized_users"].append(user_id)

    return CONFIG


def get_config():
    """Return the loaded config or None if no config is loaded."""

    global CONFIG
    return CONFIG


def check_authorized_user(user: User) -> bool:
    """Check if the given user is authorized in configuration."""

    authorized_users = CONFIG["telegram"]["authorized_users"]
    return user.id in authorized_users or user.username in authorized_users