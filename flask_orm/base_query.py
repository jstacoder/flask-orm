from sqlalchemy import orm
from sqlalchemy.orm import Query, scoped_session, class_mapper
from typing import Type, TypeVar, Optional


class QueryProperty:
    def __init__(self, session):
        # type (scoped_session)-> None
        self.session = session

    def __get__(self, model, Model):
        # type: (Model, Type[Model]) -> Optional[Type['QueryProperty']]
        mapper = class_mapper(Model)

        if mapper:
            if not getattr(Model, 'query_class', None):
                Model.query_class = BaseQuery
            query_property = Model.query_class(mapper, session=self.session())
            return query_property


class BaseQuery(Query):
    pass
