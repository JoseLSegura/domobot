"""Module for loading the configuration file."""

import json
import logging

import jsonschema

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

    return CONFIG
