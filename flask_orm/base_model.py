import sqlalchemy as sa
from typing import Optional, ClassVar
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from .base_query import BaseQuery


class BaseModel(object):

    query_class = BaseQuery  # type: ClassVar[BaseQuery]

    query = None            # type: ClassVar[Optional[BaseQuery]]


