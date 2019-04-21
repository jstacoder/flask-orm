from tst.app import app, User
from flask_orm.engine import get_app_engine, get_engine_session
import pytest


class DbContext:
    def __init__(self, metadata, engine):
        self.metadata = metadata
        self.engine = engine

    def __enter__(self):
        if self.metadata.bind is None:
            self.metadata.bind = self.engine
        self.metadata.create_all()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.metadata.bind is None:
            self.metadata.bind = self.engine
        self.metadata.drop_all()


@pytest.fixture
def engine():
    return get_app_engine(app)


@pytest.fixture
def test_app_context():
    with app.test_request_context() as ctx:
        yield ctx


@pytest.fixture
def add_db(test_app_context, engine):
    with DbContext(User.metadata, engine):
        yield


@pytest.fixture
def test_user(add_db):
    return User(name='hank').save(commit=True)


def test_orm(test_app_context):
    assert test_app_context is not None


def test_model_saves_name(test_user):
    assert User.query.filter(User.name=='hank').one().name == 'hank'


def test_model_count(test_user):
    assert User.query.count() == 1


def test_delete_method(test_user):
    test_user.delete()
    assert User.query.count() == 0
