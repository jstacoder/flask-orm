from typing import Generic, TypeVar, Optional
from flask.config import Config

C = TypeVar('C')


class ConfigSetup(Generic[C]):
    config = None  # type: C

    def __init__(self, config=None):
        # type: (Optional[C]) -> None
        self.config = config


def setup_settings(app_config):
    # type: (C) -> ConfigSetup
    return ConfigSetup(config=app_config)
