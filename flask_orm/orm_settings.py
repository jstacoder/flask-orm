from typing import Generic, TypeVar, Optional
from flask.config import Config

from typing_extensions import TypingMeta

C = TypeVar('C')  # represents Type of config class


class ConfigSetup(Generic[C]):
    config_class = None  # type: Optional[C]

    def __init__(self, config_class=None):
        # type: (Optional[C]) -> None
        self.config_class = config_class


def setup_settings(app_config):
    # type: (Config) -> ConfigSetup
    return ConfigSetup[app_config.__class__](app_config)
