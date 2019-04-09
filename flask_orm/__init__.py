from typing import Optional, TypeVar, Generic
from flask import Flask, current_app, _app_ctx_stack

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.base import Engine
from .base_model import BaseModel
from .orm_settings import setup_settings, ConfigSetup


class FlaskOrm(object):
    settings = None     # type: Optional[ConfigSetup]
    engine = None       # type: Optional[Engine]
    session = None      # type: Optional[scoped_session]

    def __init__(self, app=None):
        # type: (Optional[Flask]) -> None
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app=None):
        # type: (Optional[Flask]) -> None
        self.settings = setup_settings(app.config)
        app.teardown_appcontext(self.teardown)
        app.before_first_request(self.setup_engine)
        app.before_request(self.setup_request)

    def teardown(self):
        # type: () -> None
        self.session.remove()

    def setup_engine(self):
        # type: () -> None
        self.engine = create_engine(self.settings.database, **self.settings.extra)

    def setup_request(self):
        # type: () -> None
        pass
