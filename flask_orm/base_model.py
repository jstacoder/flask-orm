from sqlalchemy import Column, Integer
from typing import Optional, ClassVar, TypeVar, Generic, AnyStr, Type
from sqlalchemy.ext.declarative import declarative_base, declared_attr, as_declarative

from .base_query import BaseQuery


Q = TypeVar('Q')


class GenericBaseModel:
    query = None  # type: Q

    @property
    def session(self):
        # type: ()-> Q.session
        return self.query.session

    @declared_attr
    def __tablename__(cls):
        # type: ()-> str
        return cls.__name__

    @declared_attr
    def id(self):
        # type: ()-> Column
        return Column(Integer, primary_key=True)

    @classmethod
    def all(cls):
        # type: ()-> Q
        return cls.query.all()

    def save(self, commit=True):
        # type: (bool) -> Type['GenericBaseModel']
        self.session.add(self)
        if commit:
            self.session.commit()
        return self

    def delete(self):
        # type: ()-> None
        self.session.delete(self)
        self.session.commit()


@as_declarative()
class Model(GenericBaseModel):
    pass