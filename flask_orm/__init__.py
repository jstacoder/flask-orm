from typing import Optional, TypeVar, Generic, Union
from flask import Flask, current_app, _app_ctx_stack, Response

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.base import Engine

from flask_orm.base_query import QueryProperty
from .base_model import Model
from .orm_settings import setup_settings, ConfigSetup
from .engine import get_engine_session, get_app_engine


class FlaskOrm(object):
    settings: Optional[ConfigSetup] = None
    engine: Optional[Engine] = None
    session: Optional[scoped_session] = None
    Model: declarative_base = Model

    def __init__(self, app: Optional[Flask]=None) -> None:
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app: Optional[Flask]=None) -> None:
        self.settings = setup_settings(app.config)
        self.setup_engine()
        self.setup_session()
        self.make_base()
        app.teardown_appcontext(self.teardown)
        app.before_first_request(self.setup_engine)
        app.before_request(self.setup_request)

    def teardown(self, resp_or_exc: Union[Response, Exception]) -> None:
        self.session.remove()

    def setup_engine(self) -> None:
        self.engine = get_app_engine(app=self.app)
        self.Model.metadata.bind = self.engine

    def setup_session(self) -> None:
        self.session = get_engine_session(self.engine)

    def set_query_property(self, model_class):
        model_class.query = QueryProperty(self.session)

    def make_base(self):
        self.set_query_property(self.Model)

    def setup_request(self) -> None:
        pass
