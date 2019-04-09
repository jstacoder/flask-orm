from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_app_engine(app: Flask) -> Engine:
    return create_engine(app.config['DATABASE_URI'])


def get_engine_session(engine: Engine=None) -> scoped_session:
    return scoped_session(sessionmaker(bind=engine))

