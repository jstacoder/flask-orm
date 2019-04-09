from sqlalchemy import Column, Integer
from typing import Optional, ClassVar, TypeVar, Generic
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from .base_query import BaseQuery


class BaseModel:
    query: BaseQuery = None

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    @declared_attr
    def id(self) -> Column:
        return Column(Integer, primary_key=True)

    @classmethod
    def all(cls) -> BaseQuery:
        return cls.query.all()

    def save(self, commit: bool=True) -> None:
        self.query.session.add(self)
        if commit:
            self.query.session.commit()



Model = declarative_base(cls=BaseModel)
