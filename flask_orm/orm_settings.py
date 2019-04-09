from typing import Generic, TypeVar, Optional
from flask.config import Config


class ConfigSetup:
    config = None  # type: Optional[Config]

    def __init__(self, config=None):
        # type: (Optional[Config]) -> None
        self.config = config


def setup_settings(app_config):
    # type: (Config) -> ConfigSetup
    return ConfigSetup(config=app_config)
