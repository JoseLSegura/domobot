"""Module containing the schema for the configuration file."""


CONFIG_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "telegram": {
            "type": "object",
            "properties": {
                "token": {"type": "string"},
                "authorized_users": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["token"],
        },
        "garage_door": {
            "type": "object",
            "properties": {
                "lock_pin": {"type": "integer"},
                "open_pin": {"type": "integer"},
                "close_pin": {"type": "integer"},
                "open_time": {"type": "number"},
                "close_time": {"type": "number"},
            },
            "required": ["lock_pin", "open_pin", "close_pin"]
        }
    }
}
